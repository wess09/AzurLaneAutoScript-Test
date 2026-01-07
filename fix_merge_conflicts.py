#!/usr/bin/env python3
"""
修复 template.json 中的 Git 合并冲突
"""
import re

def fix_merge_conflicts(filepath):
    """读取文件并移除 Git 合并冲突标记"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 统计冲突数量
    conflict_count = content.count('<<<<<<< HEAD')
    print(f"发现 {conflict_count} 个合并冲突")
    
    # 移除合并冲突标记,保留 sfdaoyu/island 分支的内容(新内容)
    # 模式: <<<<<<< HEAD\n...旧内容...\n=======\n...新内容...\n>>>>>>> sfdaoyu/island
    
    # 使用正则表达式匹配并替换
    pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> sfdaoyu/island'
    
    def replace_conflict(match):
        # 保留新内容(group 2)
        return match.group(2)
    
    # 替换所有冲突,使用 DOTALL 标志让 . 匹配换行符
    fixed_content = re.sub(pattern, replace_conflict, content, flags=re.DOTALL)
    
    # 检查是否还有冲突标记
    if '<<<<<<< HEAD' in fixed_content or '=======' in fixed_content or '>>>>>>> sfdaoyu/island' in fixed_content:
        print("警告: 仍然存在冲突标记,需要手动检查")
        return False
    
    # 写回文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"成功修复 {conflict_count} 个合并冲突")
    return True

if __name__ == '__main__':
    filepath = './config/template.json'
    success = fix_merge_conflicts(filepath)
    if success:
        print("修复完成!")
    else:
        print("修复失败,请手动检查文件")

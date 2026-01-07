
import re
import json

file_path = r"C:\Users\Azur\Desktop\项目\AzurLaneAutoScript\module\config\i18n\ja-JP.json"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement for Conflict 1
pattern1 = re.compile(r'<<<<<<< HEAD\s+?"StayInZone": \{[\s\S]+?>>>>>>> sfdaoyu/island', re.MULTILINE)
repl1 = '''    "StayInZone": {
      "name": "指定海域计划作战",
      "help": "雪风大人温馨提示:打开这个功能并指定海域后，将会在指定海域进行计划作战，不会再回到港口nanoda!侵蚀三推荐NA海域东南B，侵蚀五推荐卡利比安海B或者C nanoda!"
    },
    "APPreserveUntilReset": {
      "name": "OpsiMeowfficerFarming.APPreserveUntilReset.name",
      "help": "OpsiMeowfficerFarming.APPreserveUntilReset.help"'''
content_new, n1 = pattern1.subn(repl1, content)
print(f"Replaced Conflict 1: {n1} times")

# Replacement for Conflict 2
pattern2 = re.compile(r'<<<<<<< HEAD\s+?"YellowCoinPreserve": \{[\s\S]+?>>>>>>> sfdaoyu/island', re.MULTILINE)
repl2 = '''    "OperationCoinsPreserve": {
      "name": "OpsiHazard1Leveling.OperationCoinsPreserve.name",
      "help": "OpsiHazard1Leveling.OperationCoinsPreserve.help"
    },
    "DoScanningDevice": {
      "name": "OpsiHazard1Leveling.DoScanningDevice.name",
      "help": "OpsiHazard1Leveling.DoScanningDevice.help"
    },
    "MinimumActionPointReserve": {
      "name": "保留 X 点行动力",
      "help": "搏一搏，单车变摩托，雪风大人已经把幸运分给指挥官了nanoda，上吧nanoda！"
    },
    "ExecuteFixedPatrolScan": {
      "name": "舰队强制移动",
      "help": "雪风大人温馨提示：开启后，将强制移动舰队以免找不到明石，指挥官你也不想因为找不到明石导致坠机nanoda？打开这个功能轻轻松松达到50万+海里每月nanoda，指挥官还在等什么nanoda!"
    },
    "Cl1Filter": {
      "name": "明石购买筛选",
      "help": "侵蚀一明石一般只购买体力nanoda"
    }
  },
  "OpsiSirenBug": {
    "_info": {
      "name": "OpsiSirenBug._info.name",
      "help": "OpsiSirenBug._info.help"
    },
    "SirenResearch_Enable": {
      "name": "OpsiSirenBug.SirenResearch_Enable.name",
      "help": "OpsiSirenBug.SirenResearch_Enable.help"
    },
    "SirenBug_Enable": {
      "name": "OpsiSirenBug.SirenBug_Enable.name",
      "help": "OpsiSirenBug.SirenBug_Enable.help"
    },
    "SirenBug_Type": {
      "name": "OpsiSirenBug.SirenBug_Type.name",
      "help": "OpsiSirenBug.SirenBug_Type.help",
      "dangerous": "dangerous",
      "safe": "safe"
    },
    "SirenBug_Zone": {
      "name": "OpsiSirenBug.SirenBug_Zone.name",
      "help": "OpsiSirenBug.SirenBug_Zone.help"
    },
    "DisableTaskSwitchDuringBug": {
      "name": "OpsiSirenBug.DisableTaskSwitchDuringBug.name",
      "help": "OpsiSirenBug.DisableTaskSwitchDuringBug.help",
      "True": "True",
      "False": "False"
    }
  },
  "OpsiCheckLeveling": {
    "_info": {
      "name": "OpsiCheckLeveling._info.name",
      "help": "OpsiCheckLeveling._info.help"
    },
    "TargetLevel": {
      "name": "OpsiCheckLeveling.TargetLevel.name",
      "help": "OpsiCheckLeveling.TargetLevel.help"
    },
    "LastRun": {
      "name": "OpsiCheckLeveling.LastRun.name",
      "help": "OpsiCheckLeveling.LastRun.help"
    },
    "DelayAfterFull": {
      "name": "OpsiCheckLeveling.DelayAfterFull.name",
      "help": "OpsiCheckLeveling.DelayAfterFull.help"
    }
  },
  "OpsiScheduling": {
    "_info": {
      "name": "OpsiScheduling._info.name",
      "help": "OpsiScheduling._info.help"
    },
    "EnableSmartScheduling": {
      "name": "OpsiScheduling.EnableSmartScheduling.name",
      "help": "OpsiScheduling.EnableSmartScheduling.help"
    },
    "ActionPointNotifyLevels": {
      "name": "OpsiScheduling.ActionPointNotifyLevels.name",
      "help": "OpsiScheduling.ActionPointNotifyLevels.help"'''
content_new, n2 = pattern2.subn(repl2, content_new)
print(f"Replaced Conflict 2: {n2} times")

# Replacement for Conflict 3
pattern3 = re.compile(r'<<<<<<< HEAD\s+?"DashboardON": "ダッシュボード ON",\s+"DashboardOFF": "ダッシュボード OFF",\s+=======\s+"DashboardON": "Gui.Button.DashboardON",\s+"DashboardOFF": "Gui.Button.DashboardOFF",\s+>>>>>>> sfdaoyu/island', re.MULTILINE)
# Simple string replacement might be safer if regex is tricky with quotes/spaces
target3 = '''<<<<<<< HEAD
      "DashboardON": "ダッシュボード ON",
      "DashboardOFF": "ダッシュボード OFF",
=======
      "DashboardON": "Gui.Button.DashboardON",
      "DashboardOFF": "Gui.Button.DashboardOFF",
>>>>>>> sfdaoyu/island'''
repl3 = '''      "DashboardON": "ダッシュボード ON",
      "DashboardOFF": "ダッシュボード OFF",'''

if target3 in content_new:
    content_new = content_new.replace(target3, repl3)
    n3 = 1
else:
    # Try regex if exact match fails
    pattern3 = re.compile(r'<<<<<<< HEAD\s+?"DashboardON"[\s\S]+?>>>>>>> sfdaoyu/island', re.MULTILINE)
    content_new, n3 = pattern3.subn(repl3, content_new)

print(f"Replaced Conflict 3: {n3} times")

# Scan for any other conflicts
remaining = list(re.finditer(r'<<<<<<< HEAD', content_new))
if remaining:
    print(f"Warning: {len(remaining)} conflicts REMAINING!")
    for m in remaining:
        print(f"Found at {m.start()}")
        print(content_new[m.start():m.start()+200])
else:
    try:
        json.loads(content_new)
        print("JSON validation successful.")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_new)
        print("File updated successfully.")
    except json.JSONDecodeError as e:
        print(f"JSON validation failed: {e}")
        lines = content_new.splitlines()
        print(f"Error line {e.lineno}: {lines[e.lineno-1]}")

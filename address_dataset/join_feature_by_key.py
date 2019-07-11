import os
import sys
ori_file, new_file = sys.argv[1:3]
# ori_file = "other/ori_data"
# new_file = "other/new_f"

feature = dict()

with open(new_file,"r", encoding='utf-8') as f:
    for line in f:
        fields = line.strip().split(' ')
        key = fields[0] + "_" + fields[1]
#         if len(fields)<3:
#             print(key)
#         if key == "1820400113_20180926":
#             continue
        feature[key] = fields[2]

with open(ori_file, "r", encoding='utf-8') as f:
    for line in f:
        fields = line.strip().split(' ')
        key = fields[0] + "_" + fields[1]
        if key in feature:
            print(line.strip() + " " + "卡状态："+feature[key])
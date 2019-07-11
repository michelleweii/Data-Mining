import os
import sys
import re
# 1替换为逾期，其他符号替换为正常，这个字段的名字：zxsCreCardRepayRecord24m
# 24条由+号连接转为1条
# 然后根据key和date进行
# i=0
for src in sys.stdin:
#     i+=1
#     print(i)
    query_new = src.split('\t')[0]+' '+src.split('\t')[1]+' '
    zxsCreCardRepayRecord24m = src.split('\t')[-2]
#     print("zxs:",zxsCreCardRepayRecord24m)
    zxs24m = zxsCreCardRepayRecord24m.split('+')
    num = len(zxs24m)
    zxs24m = [i.strip() for i in zxs24m]
    zxs24m = [i.strip('|') for i in zxs24m]
    num = len(zxs24m)
    max_len = 24
    field = []
    for item in zxs24m:
        item = item.replace("N1","1").replace(" ","")
#         print(item)
        list_item = list(item)
        # print(len(list_item))
        if len(field) == 0:
            field = list_item + list("@" * (max_len-len(list_item)))
            # print(len(field))
            # print(field)
        else:
            if "1" in item:
                idx = [i.start() for i in re.finditer('1', item)]
                for i in idx:
                    field[i]= "1"
                # print("trans:",field)
            if "2" in item:
                idx = [i.start() for i in re.finditer('1', item)]
                for i in idx:
                    field[i]= "2"
    # print(field)
    field = "".join(field)
#         print(field)
    if field.count("@") == max_len:
        field = "缺"
    else:
        field = field.replace("*","正").replace("N","正").replace("/","正").replace("#","正").\
        replace("C","正").replace("@","正").replace(" ","")
        # print(field)
        field = field.replace("1","壹")
        field = field.replace("2","贰")

        if "-9999" in field:
            field = "正" * num

    query_new += field
    print(query_new)
"""
20190711
Michelleweii
"""
import numpy as np
src1 = "1812164263	20190201	 31	 31	 0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|0|+|-9999|+|-9999	 \
01	 正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|正常|+|-9999|+|-9999	 \
44000|+|44000|+|23781|+|112000|+|112000|+|500|+|15000|+|100398|+|50000|+|15000|+|5000|+|15500|+|1723|+|20000|+|10524|+|0	\
N N N N N N N N N N N N N N N N N N N N N N N N|+|* * * * * * * * * * * * * * * * * * * * * * * *|+ \
|N N N N N N N N 1 N N N N N N N N N N N N N N N|+|* * * * * * * * * * * * * * * * * * * * * * * *|+ \
|N N N N N N N N N N N N N N N N N N N N N N N N|+|* N * * N * * * * * * * * * * * * * * * * * * *|+ \
|N N N N N N N N N N N N N N N N N N N N N N N N|+|N N N N N N N N N N N N N N N N N N N N N N N N|+ \
|N N N N N N N N N N N N N N N N N N N N N * N N|+|* * * * * * * * * * * * * * * * * * * * * * * *|+\
|/ # N N N N N * N * N N N N N * N N * * N N N N|+|/ / / / / / / / / / * N N N N N N N N N N N N N|+ \
|/ / / / / / / / / / / N N N N N N N N N N N N N|+|/ / / / / / / / / / / / * * * N N N N N N N N N|+|-9999|+|-9999	 \
44000|+|0|+|23781|+|0|+|112000|+|500|+|15000|+|100398|+|50000|+|0|+|20000|+|15500|+|1723|+|0|+|10524|+|0"

zxsCreCardRepayRecord24m22 = " 1 1 1 1 1 1 N N1 N N 1 2 2 1 1 N N N N N N N N N|+\
|N N N N N N N N N N N N N N N N N N N N N N N N|+\
|N N N N N N N N N N N N N N N N N N 1 1 1 2 N N|+\
|N N N1 N N N N N N 1 N N N N N N N N N N N N N|+\
|* * * * * * * * * * * * * * * * * * * * * * * *|+|* * * * * * * * * * * * * * * * * * * * * * * *|+\
|N N N N N N N N N N N N N N N N N N N N N N N N|+|* * * * * * * * * * * * * * * * * * * * * * * *|+\
|* * * * * * * * * * * * * * * * * * * * * * * *|+|* * * * * * * * * ** * * * * * * * * * * * * *|+\
|N N N N N N N N N N N N N N N N N N N N N N N N|+|* * N N N N N N N N N N N N N N N N N N N N N N|+|-9999|+|-9999"

zxsCreCardRepayRecord24ml = "N N N N N N N N N * N * N * N * N * * 1 N * 1|+\
|N N N N * N N N N N N N N N N N N 1 N N N 1 N N|+|/ / / / / / / / / // * N N 1 N N 1 N N N N N N|+\
|* * * * * * * * * * * * * * * * * * * * * * * *|+|* * * * * * * * * * * * * * * * * * * * * * * *|+\
|/ / / / / / / / / / / / / * N N N N N N N N N "
zxsCreCardRepayRecord24ms= "-9999"
zxsCreCardRepayRecord24mda = " "
zxsCreCardRepayRecord24m = "/ / / / / / / / / / / / / / / / / / / * * * * *|+|/ / / / / / / / / / / / / / / / / / / * * N N N|+|/ / / / / / / / / / / / / / / / / / / / * N N N|+|/ / / / / / / / / / / / / / / / / / / / * * N N|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * N N N|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / * * * *|+|/ / / / / / / / / / / / / / / / / / / / / * N N|+|/ / / / / / / / / / / / / / / / / / / / / * N N|+|/ / / / / / / / / / / / / / / / / / / / / * * *|+|/ / / / / / / / / / / / / / / / / / / / / * N N|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999|+|-9999"
def merge_col(col):
    if "G" in col[0]:
        return "拾"
        # print("拾")
    elif "7" in col[0]:
        # print("柒")
        return "柒"
    elif "6" in col[0]:
        # print("陆")
        return "陆"
    elif "5" in col[0]:
        # print("伍")
        return "伍"
    elif "4" in col[0]:
        # print("肆")
        return "肆"
    elif "3" in col[0]:
        # print("弎")
        return "弎"
    elif "2" in col[0]:
        # print("贰")
        return "贰"
    elif "1" in col[0]:
        # print("壹")
        return "壹"
    elif "C" in col[0]:
        # print("玖")
        return "玖"
    elif "D" in col[0]:
        return "捌"
    elif "Z" in col[0]:
        return "捌"
    else:
        return "零"

zxs24m = zxsCreCardRepayRecord24m.split('+')
zxs24m = [i.strip() for i in zxs24m]
zxs24m = [i.strip('|') for i in zxs24m]
len_zxs24m = len(zxs24m)
# print("len:",len_zxs24m)
max_col = 24
content = []
field = ""
if zxs24m[0] == "-9999":
    field = "零"
    print(field)
elif zxs24m[0] == '':
    field = "缺"
else:
    for item in zxs24m:
        # print(item)
        if ("-9999" in item) and len_zxs24m!=1:
            item = "N" * len_zxs24m
        if "N1" in item:
            item = item.replace("N1","1")
        item = item.replace(" ","")
        if len(item) < max_col:
            item += "@" * (max_col-len(item))
        content.append((list(item)))

    # content = np.array(content)
    # print(content.shape)
    # print(content)

    # print(col)
    # 读取所有content的每一列，max_col=len(content)
    for i in range(max_col):
        # print(i)
        col = [x[i] for x in content]
        # print(col)
        # col = content[:,i]
        # print(col)
        cur_char = merge_col(col)
    #     # print(merge_col(col))
        field += cur_char
    print(len(field),field)



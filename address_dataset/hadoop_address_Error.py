import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")

target = ["zxSpouseRcy24MCreCardMaxDelqPeriod","zxAccountCnt","zxMaxLoanBalanceAmt","zxMaxLoanAmt",\
"zxMaxSalary","zxMinSalary","zxCurrDelqPeriodSum"]
target = sorted(target)
#print target
dict_c = {}

for line in sys.stdin:
        fields = line.strip().split('\t')
        key = fields[0]
        key = key.split("_")[0]
        date = fields[1]
        feature_tmp = fields[2]
        query = key + "\t" + date
        try:
            for item in feature_tmp.split(','):
                    keyi,valuei = item.split(':')[0],item.split(':')[-1]
                    keyi = keyi[2:-1]
                    #print keyi
                    if keyi in target:
                            dict_c[keyi] = valuei

            if len(dict_c) != len(target):
                for i in target:
                    if i not in dict_c.keys():
                             dict_c[i] = "u'None'"
            #print "*"*5
            #print sorted(dict_c)
            for k in sorted(dict_c):
            #for k,v in dict_c.items():
                    query += "\t" + dict_c[k].replace('"','')
            print query
        except:
            print key
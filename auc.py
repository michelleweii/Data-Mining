import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.stats import ks_2samp
from sklearn.metrics import roc_curve,auc # 和上面的关系是？？？两次值计算出来的不一样
import os

y_pred = []
y = []

print(os.path.exists('./input/eval_set'))

with open("./input/eval_set","r") as f:
    content = f.readlines()
    for line in content:
        y_pred.append(line.strip().split(' ')[0])
        y.append(line.strip().split(' ')[1])


y_pred = np.array(y_pred).astype('float64')
y = np.array(y).astype('float64')
#
# print(y_pred)
# print(y)
# print(np.array(y_pred).dtype)
# print(np.array(y).dtype)

ks = ks_2samp(y, y_pred)
print("ks:",ks.statistic)

auc = roc_auc_score(np.array(y),np.array(y_pred))
print("auc",auc)


"""
文件内容 pred,ture
0.18038543 0
0.063440904 0
0.06621654 0
0.10528016 0
0.055965718 0
0.09200314 1
"""
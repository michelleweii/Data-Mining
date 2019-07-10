# coding: utf-8
import numpy as np
from math import gcd
import numpy as np
from sklearn.metrics import roc_auc_score
from scipy.stats import ks_2samp
# from sklearn.metrics import roc_curve,auc # 和上面的关系是？？？两次值计算出来的不一样
import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import os

# df1 = DataFrame()
# df1['pred'] = data2
def compute_ks(data1,data2):
    df1 = DataFrame()
    df1['pred'] = data2
    df1['label'] = data1
    # 按照样本为正样本的概率值升序排序，也即坏样本的概率从高到低排序
    sorted_list = df1.sort_values(['pred'], ascending=[True])
    # print(sorted_list)
    """
            pred  label
17  0.055966    0.0
8   0.056266    0.0
14  0.063441    0.0
15  0.066217    0.0
0   0.070942    0.0
4   0.074102    0.0
3   0.087055    0.0
2   0.090387    0.0
18  0.092003    1.0
6   0.098286    0.0
16  0.105280    0.0
10  0.107256    0.0
12  0.123415    0.0
5   0.137829    0.0
7   0.139731    0.0
1   0.159905    0.0
13  0.180385    0.0
9   0.203199    0.0
11  0.217903    0.0
    """
    total_good = sorted_list['label'].sum() # label为1的样本有多少个，真实为1的样本
    # print(sorted_list['label'])
    # print(total_good)
    total_bad = sorted_list.shape[0] - total_good # label为0的样本有多少个，真实为0的样本

    max_ks = 0.0
    good_count = 0.0
    bad_count = 0.0
    for index, row in sorted_list.iterrows(): #按照标签和每行拆开
        # print(index)
        # print('-'*5)
        # print(row)
        """
        index: 17
        row:
            pred     0.055966
            label    0.000000
        """
        if row['label'] == 0:
            bad_count += 1
        else:
            good_count += 1
        val = abs(bad_count/total_bad - good_count/total_good)
        max_ks = max(max_ks, val)
    return max_ks

# def cal_ks(data1,data2): # label,pred
#     data1 = np.sort(data1)
#     data2 = np.sort(data2)
#     n1 = data1.shape[0]
#     n2 = data2.shape[0]
#     if min(n1, n2) == 0:
#         raise ValueError('Data passed to ks_2samp must not be empty')
#     data_all = np.concatenate([data1, data2])
#     # print('data_all',len(data_all))
#     # using searchsorted solves equal data problem
#     # 数组的插入：np.searchsorted(a, b)
#     # 将b插入原有序数组a，并返回插入元素的索引值
#
#     cdf1 = np.searchsorted(data1, data_all, side='right')/n1
#     # print('cdf1',cdf1)
#     # print(len(cdf1))
#     cdf2 = np.searchsorted(data2, data_all, side='right')/n2
#     # print('cdf2',cdf2)
#     cddiffs = cdf1 - cdf2
#     # print('cdd',cddiffs)
#     minS = -np.min(cddiffs)
#     # print('minS',minS)
#     maxS = np.max(cddiffs)
#     # print('maxS',maxS)
#     g = gcd(n1, n2) # 最大公约数
#     # print(n1,n2,g)
#     lcm = (n1 // g) * n2
#     # print('lcm',lcm)
#     h = int(np.round(max(minS, maxS) * lcm))
#     # print('h',h)
#     d = h * 1.0 / lcm
#     return d

def cal_auc(labels, preds):
    """
    先排序，然后统计有多少正负样本对满足：正样本预测值>负样本预测值, 再除以总的正负样本对个数
    复杂度 O(NlogN), N为样本数
    """
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pair = n_pos * n_neg

    labels_preds = zip(labels, preds)
    labels_preds = sorted(labels_preds, key=lambda x: x[1])
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(len(labels_preds)):
        if labels_preds[i][0] == 1:
            satisfied_pair += accumulated_neg
        else:
            accumulated_neg += 1

    return satisfied_pair / float(total_pair)

def approximate_auc(labels, preds, n_bins=100):
    """
    近似方法，将预测值分桶(n_bins)，对正负样本分别构建直方图，再统计满足条件的正负样本对
    复杂度 O(N)
    这种方法有什么缺点？怎么分桶？

    """
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pair = n_pos * n_neg

    pos_histogram = [0 for _ in range(n_bins)]
    neg_histogram = [0 for _ in range(n_bins)]
    bin_width = 1.0 / n_bins
    for i in range(len(labels)):
        nth_bin = int(preds[i] / bin_width)
        if labels[i] == 1:
            pos_histogram[nth_bin] += 1
        else:
            neg_histogram[nth_bin] += 1

    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(n_bins):
        satisfied_pair += (pos_histogram[i] * accumulated_neg + pos_histogram[i] * neg_histogram[i] * 0.5)
        accumulated_neg += neg_histogram[i]

    return satisfied_pair / float(total_pair)


import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve
from scipy.stats import ks_2samp


def ks_calc_cross(data, pred, y_label):
    '''
    功能: 计算KS值，输出对应分割点和累计分布函数曲线图
    输入值:
    data: 二维数组或dataframe，包括模型得分和真实的标签
    pred: 一维数组或series，代表模型得分（一般为预测正类的概率）
    y_label: 一维数组或series，代表真实的标签（{0,1}或{-1,1}）
    输出值:
    'ks': KS值，'crossdens': 好坏客户累积概率分布以及其差值gap
    '''
    crossfreq = pd.crosstab(data[pred[0]], data[y_label[0]])
    crossdens = crossfreq.cumsum(axis=0) / crossfreq.sum()
    crossdens['gap'] = abs(crossdens[0] - crossdens[1])
    ks = crossdens[crossdens['gap'] == crossdens['gap'].max()]
    return ks, crossdens

def calc_ks(y_true, y_prob, n_bins=10):
    percentile = np.linspace(0, 100, n_bins + 1).tolist()
    bins = [np.percentile(y_prob, i) for i in percentile]
    bins[0] = bins[0] - 0.01
    bins[-1] = bins[-1] + 0.01
    binids = np.digitize(y_prob, bins) - 1
    y_1 = sum(y_true == 1)
    y_0 = sum(y_true == 0)
    bin_true = np.bincount(binids, weights=y_true, minlength=len(bins))
    bin_total = np.bincount(binids, minlength=len(bins))
    bin_false = bin_total - bin_true
    # print('bins',bin_false)
    # bins [19779. 19705. 19633. 19617. 19599. 19541. 19523. 19472. 19380. 19115.
    #      0.]
    true_pdf = bin_true / y_1
    false_pdf = bin_false / y_0
    true_cdf = np.cumsum(true_pdf)
    false_cdf = np.cumsum(false_pdf)
    ks_list = np.abs(true_cdf - false_cdf).tolist()
    ks = max(ks_list)
    return ks

def ks_calc_auc(data, pred, y_label):
    '''
    功能: 计算KS值，输出对应分割点和累计分布函数曲线图
    输入值:
    data: 二维数组或dataframe，包括模型得分和真实的标签
    pred: 一维数组或series，代表模型得分（一般为预测正类的概率）
    y_label: 一维数组或series，代表真实的标签（{0,1}或{-1,1}）
    输出值:
    'ks': KS值
    '''
    fpr, tpr, thresholds = roc_curve(data[y_label[0]], data[pred[0]])
    ks = max(tpr - fpr)
    return ks


def ks_calc_2samp(data, pred, y_label):
    '''
    功能: 计算KS值，输出对应分割点和累计分布函数曲线图
    输入值:
    data: 二维数组或dataframe，包括模型得分和真实的标签
    pred: 一维数组或series，代表模型得分（一般为预测正类的概率）
    y_label: 一维数组或series，代表真实的标签（{0,1}或{-1,1}）
    输出值:
    'ks': KS值，'cdf_df': 好坏客户累积概率分布以及其差值gap
    '''
    Bad = data.loc[data[y_label[0]] == 1, pred[0]]
    Good = data.loc[data[y_label[0]] == 0, pred[0]]
    data1 = Bad.values
    data2 = Good.values
    n1 = data1.shape[0]
    n2 = data2.shape[0]
    data1 = np.sort(data1)
    data2 = np.sort(data2)
    data_all = np.concatenate([data1, data2])
    cdf1 = np.searchsorted(data1, data_all, side='right') / (1.0 * n1)
    cdf2 = (np.searchsorted(data2, data_all, side='right')) / (1.0 * n2)
    ks = np.max(np.absolute(cdf1 - cdf2))
    cdf1_df = pd.DataFrame(cdf1)
    cdf2_df = pd.DataFrame(cdf2)
    cdf_df = pd.concat([cdf1_df, cdf2_df], axis=1)
    cdf_df.columns = ['cdf_Bad', 'cdf_Good']
    cdf_df['gap'] = cdf_df['cdf_Bad'] - cdf_df['cdf_Good']
    return ks, cdf_df


def main():
    y_pred = {}
    y = {}
    # print(os.path.exists('./input/eval_set'))
    with open("./input/total_mob2_uniq", "r",encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            idd,date,label = line.strip().split(' ')[:3]
            y[idd] = float(label)

    with open("./input/201803.data_mob2.score", "r", encoding='utf8') as f:
    # with open("./input/total_mob2_uniq", "r",encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            idd,date,label = line.strip().split(' ')
            y_pred[idd] = float(label)

    # print('ypredori:',y_pred)
    data1 = [] # label
    data2 = [] # pred
    for key_pred,val_pred in y_pred.items():
        if key_pred in y.keys():
            data2.append(val_pred)
            data1.append(y[key_pred])
    # print("y_true:",data1)
    # print('y_pred:',data2)

    # y = sorted(y)
    # y_pred = sorted(y_pred)
    # for key in y:
    #     print(key)
    #     if key not in y_pred:
    #         del y[key]
    #
    # print(len(y))
    # print(len(y_pred))
    # for val1 in y.values():
    #     data1.append(val1)
    # for val2 in y_pred.values():
    #     data1.append(val2)

    print(len(data1))
    print(len(data2))


    # y_pred = np.array(y_pred).astype('float64')
    # y = np.array(y).astype('float64')
    print('aaa：',calc_ks(np.asarray(data1),np.asarray(data2)))
    # print('ks_error:',cal_ks(data1,data2))
    print('auc:',cal_auc(data1,data2))
    # print('approximate_auc:',approximate_auc(data1,data2))
    print('ks_new:',compute_ks(data1,data2))

    print('-'*25)
    # ks = ks_2samp(data1,data2)
    # print("ks:", ks)

    auc = roc_auc_score(data1,data2)
    print("auc", auc)

    data = {'y_label':data1,'pred':data2}
    data = pd.DataFrame(data)

    ks1, crossdens = ks_calc_cross(data, ['pred'], ['y_label'])

    ks2 = ks_calc_auc(data, ['pred'], ['y_label'])

    ks3 = ks_calc_2samp(data, ['pred'], ['y_label'])

    get_ks = lambda y_pred, y_true: ks_2samp(y_pred[y_true == 1], y_pred[y_true != 1]).statistic
    ks4 = get_ks(data['pred'], data['y_label'])
    print('KS1:', ks1['gap'].values)
    print('KS2:', ks2)
    print('KS3:', ks3[0])
    print('KS4:', ks4)

if __name__ == '__main__':
    main()

import numpy as np
from math import gcd
import os


def cal_ks(data1,data2):
    data1 = np.sort(data1)
    data2 = np.sort(data2)
    n1 = data1.shape[0]
    n2 = data2.shape[0]
    if min(n1, n2) == 0:
        raise ValueError('Data passed to ks_2samp must not be empty')
    data_all = np.concatenate([data1, data2])
    # using searchsorted solves equal data problem
    cdf1 = np.searchsorted(data1, data_all, side='right') / n1
    cdf2 = np.searchsorted(data2, data_all, side='right') / n2
    cddiffs = cdf1 - cdf2
    minS = -np.min(cddiffs)
    maxS = np.max(cddiffs)
    g = gcd(n1, n2)
    lcm = (n1 // g) * n2
    h = int(np.round(max(minS, maxS) * lcm))
    d = h * 1.0 / lcm
    return d

def naive_auc(labels, preds):
    """
    最简单粗暴的方法
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

def main():
    y_pred = []
    y = []
    # print(os.path.exists('./input/eval_set'))
    with open("./input/eval_set", "r") as f:
        content = f.readlines()
        for line in content:
            y_pred.append(line.strip().split(' ')[0])
            y.append(line.strip().split(' ')[1])

    y_pred = np.array(y_pred).astype('float64')
    y = np.array(y).astype('float64')
    print(cal_ks(y,y_pred))
    print(naive_auc(y,y_pred))
    # print(approximate_auc(y,y_pred))


if __name__ == '__main__':
    main()

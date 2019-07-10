import numpy as np
"""
PSI = sum（（实际占比-预期占比）* ln（实际占比/预期占比））
举例：
比如训练一个logistic回归模型，预测时候会有个概率输出p。
测试集上的输出设定为p1吧，将它从小到大排序后10等分，如0-0.1,0.1-0.2,......。
现在用这个模型去对新的样本进行预测，预测结果叫p2，按p1的区间也划分为10等分。
实际占比就是p2上在各区间的用户占比，预期占比就是p1上各区间的用户占比
"""
# git源代码

def calculate_psi(expected, actual, buckettype='bins', buckets=10, axis=0):
    '''Calculate the PSI (population stability index) across all variables
    Args:
       expected: numpy matrix of original values
       actual: numpy matrix of new values, same size as expected
       buckettype: type of strategy for creating buckets, bins splits into even splits, quantiles splits into quantile buckets
       buckets: number of quantiles to use in bucketing variables
       axis: axis by which variables are defined, 0 for vertical, 1 for horizontal
    Returns:
       psi_values: ndarray of psi values for each variable
    Author:
       Matthew Burke
       github.com/mwburke
       worksofchart.com
    '''

    def psi(expected_array, actual_array, buckets):
        '''Calculate the PSI for a single variable
        Args:
           expected_array: numpy array of original values
           actual_array: numpy array of new values, same size as expected
           buckets: number of percentile ranges to bucket the values into
        Returns:
           psi_value: calculated PSI value
        '''

        def scale_range (input, min, max):
            input += -(np.min(input))
            input /= np.max(input) / (max - min)
            input += min
            return input


        breakpoints = np.arange(0, buckets + 1) / (buckets) * 100

        if buckettype == 'bins':
            breakpoints = scale_range(breakpoints, np.min(expected_array), np.max(expected_array))
        elif buckettype == 'quantiles':
            breakpoints = np.stack([np.percentile(expected_array, b) for b in breakpoints])



        expected_percents = np.histogram(expected_array, breakpoints)[0] / len(expected_array)
        actual_percents = np.histogram(actual_array, breakpoints)[0] / len(actual_array)

        def sub_psi(e_perc, a_perc): # test,base
            '''Calculate the actual PSI value from comparing the values.
               Update the actual value to a very small number if equal to zero
            '''
            if a_perc == 0:
                a_perc = 0.0001
            if e_perc == 0:
                e_perc = 0.0001

            value = (e_perc - a_perc) * np.log(e_perc / a_perc)
            return(value)

        psi_value = np.sum(sub_psi(expected_percents[i], actual_percents[i]) for i in range(0, len(expected_percents)))

        return(psi_value)

    if len(expected.shape) == 1:
        psi_values = np.empty(len(expected.shape))
    else:
        psi_values = np.empty(expected.shape[axis])

    for i in range(0, len(psi_values)):
        if len(psi_values) == 1:
            psi_values = psi(expected, actual, buckets)
        elif axis == 0:
            psi_values[i] = psi(expected[:,i], actual[:,i], buckets)
        elif axis == 1:
            psi_values[i] = psi(expected[i,:], actual[i,:], buckets)

    return(psi_values)

if __name__ == '__main__':
    rs = np.random.RandomState(5)
    initial = rs.normal(size=100)
    new = rs.normal(loc=0.2, size=120)
    # print(type(initial))
    # print(len(initial))
    # print(initial)
    # print(len(new))
    # print(new)
    # calculate_psi(initial,new)
    # print(calculate_psi(initial, new, buckettype='quantiles', buckets=10, axis=1))

    y_3_based = []
    y_4 = []
    y_5 = []
    y_6 = []
    y_7 = []
    with open("./input/201803.data_mob2.score", "r",encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            y_3_based.append(float(line.strip().split(' ')[2]))
    with open("./input/201804.data_mob2.score", "r", encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            y_4.append(float(line.strip().split(' ')[2]))

    with open("./input/201805.data_mob2.score", "r", encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            y_5.append(float(line.strip().split(' ')[2]))
    with open("./input/201806.data_mob2.score", "r", encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            y_6.append(float(line.strip().split(' ')[2]))
    with open("./input/201807.data_mob2.score", "r", encoding='utf8') as f:
        content = f.readlines()
        for line in content:
            y_7.append(float(line.strip().split(' ')[2]))

    # print(y_3_based)
    # print(y_4)
    # val1 = calculate_psi(np.asarray(y_3_based), np.asarray(y_4), buckettype='quantiles', buckets=10, axis=1)
    # print("base:3, test:4 -- psi:", val1)
    val4 = calculate_psi(np.asarray(y_3_based), np.asarray(y_4))
    print("base:3, test:4 -- psi:", val4)
    val5 = calculate_psi(np.asarray(y_3_based), np.asarray(y_5))
    print("base:3, test:5 -- psi:", val5)
    val6 = calculate_psi(np.asarray(y_3_based), np.asarray(y_6))
    print("base:3, test:6 -- psi:", val6)
    val7 = calculate_psi(np.asarray(y_3_based), np.asarray(y_7))
    print("base:3, test:7 -- psi:", val7)
    # print(np.arange(0, 10 + 1)/10)
    # [ 0  1  2  3  4  5  6  7  8  9 10]
    # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
    # [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]

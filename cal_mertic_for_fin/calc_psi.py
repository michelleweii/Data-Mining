import numpy as np
# 简单版本，去掉了一些内容
def calculate_psi(expected, actual, buckets=10): # test, base
    def psi(expected_array, actual_array, buckets):
        def scale_range(input, min, max):
            input += -(np.min(input))
            input /= np.max(input) / (max - min)
            input += min
            return input
        # 按照概率值分10段
        breakpoints = np.arange(0, buckets + 1) / (buckets) * 100
        breakpoints = scale_range(breakpoints, np.min(expected_array), np.max(expected_array))
        expected_percents = np.histogram(expected_array, breakpoints)[0] / len(expected_array)
        # print(expected_percents)
        actual_percents = np.histogram(actual_array, breakpoints)[0] / len(actual_array)

        def sub_psi(test, base): # test,base
            if base == 0:
                base = 0.0001
            if test == 0:
                test = 0.0001
            value = (test - base) * np.log(test / base)
            return(value)
        psi_value = np.sum(sub_psi(expected_percents[i], actual_percents[i]) for i in range(0, len(expected_percents)))
        return(psi_value)

    if len(expected.shape) == 1:
        psi_values = np.empty(len(expected.shape))
    else:
        psi_values = np.empty(expected.shape[0])

    for i in range(0, len(psi_values)):
        if len(psi_values) == 1:
            psi_values = psi(expected, actual, buckets)
        else:
            psi_values[i] = psi(expected[:,i], actual[:,i], buckets)
    return(psi_values)

if __name__ == '__main__':
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


    val4 = calculate_psi(np.asarray(y_3_based), np.asarray(y_4))
    print("base:3, test:4 -- psi:", val4)
    val5 = calculate_psi(np.asarray(y_3_based), np.asarray(y_5))
    print("base:3, test:5 -- psi:", val5)
    val6 = calculate_psi(np.asarray(y_3_based), np.asarray(y_6))
    print("base:3, test:6 -- psi:", val6)
    val7 = calculate_psi(np.asarray(y_3_based), np.asarray(y_7))
    print("base:3, test:7 -- psi:", val7)


import numpy as np
import pandas as pd
# 按照如下的元数据内容创建数据框
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
# 将上述的数据框分别命名为data1, data2, data3
data1 = pd.DataFrame(raw_data_1, columns = ['subject_id', 'first_name', 'last_name'])
data2 = pd.DataFrame(raw_data_2, columns = ['subject_id', 'first_name', 'last_name'])
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])

# 将data1和data2两个数据框按照行的维度进行合并，命名为all_data
all_data = pd.concat([data1,data2])
print(all_data)

# 将data1和data2两个数据框按照列的维度进行合并，命名为all_data_col
all_data_col = pd.concat([data1, data2], axis = 1)
print(all_data_col)

# 打印data3
print(data3)

# 按照subject_id的值对all_data和data3作合并
a = pd.merge(all_data,data3,on='subject_id')
print(a)

# 对data1和data2按照subject_id作连接
b = pd.merge(data1,data2,on='subject_id',how='inner')
print(b)

# 找到 data1 和 data2 合并之后的所有匹配结果
c = pd.merge(data1, data2, on='subject_id', how='outer')
print(c)
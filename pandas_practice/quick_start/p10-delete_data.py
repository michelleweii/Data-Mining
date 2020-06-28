# 运行以下代码
import pandas as pd
import numpy as np
path10 ='../quick_start/exercise_data/iris.csv'   # iris.csv
iris = pd.read_csv(path10)
print(iris.head())
# 创建数据框的列名称
iris = pd.read_csv(path10,names = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())

#  数据框中有缺失值吗？
print(pd.isnull(iris).sum())

# 将列petal_length的第10到19行设置为缺失值
iris.iloc[10:20,2:3]  = np.nan
print(iris.head(20))

# 将缺失值全部替换为1.0
iris.petal_length.fillna(1,inplace=True)
print(iris.head(20))

# 删除列class
del iris['class']
print(iris.head())

# 将数据框前三行设置为缺失值
iris.iloc[0:3,:]=np.nan
print(iris.head())

# 删除有缺失值的行
iris = iris.dropna(how='any')
print(iris.head())

# 重新设置索引
iris = iris.reset_index(drop = True)
print(iris.head())

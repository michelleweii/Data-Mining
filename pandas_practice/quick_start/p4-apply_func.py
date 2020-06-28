# 运行以下代码
import numpy as np
import pandas as pd
# 运行以下代码
path4 = '../quick_start/exercise_data/US_Crime_Rates_1960_2014.csv'    # "US_Crime_Rates_1960_2014.csv"

# 运行以下代码
crime = pd.read_csv(path4)
crime.head()
# 每一列(column)的数据类型是什么样的？
print(crime.info())
# Year的数据类型为int64，但是pandas有一个不同的数据类型去处理时间序列(time series)
# 将Year的数据类型转换为 datetime64
crime.Year = pd.to_datetime(crime.Year, format='%Y')
print(crime.info())
# 将列Ytiear设置为数据框的索引
crime = crime.set_index('Year',drop=True)
print(crime.head())

# 删除名为Total的列
del crime['Total']
print("crime.info()如下：")
print(crime.info())
print("resample:")
print(crime.resample('10AS').sum())

# 按照Year对数据框进行分组并求和
crimes = crime.resample('10AS').sum() # resample a time series per decades
population = crime['Population'].resample('10AS').max()
# 更新 "Population"
crimes['Population'] = population
print(crimes)

# 何时是美国历史上生存最危险的年代？
print(crime.idxmax(0))
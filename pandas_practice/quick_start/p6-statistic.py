# https://zhuanlan.zhihu.com/p/76929640
import pandas as pd
import datetime
# 运行以下代码
path6 = "../quick_start/exercise_data/wind.data"  # wind.data
data = pd.read_table(path6, sep = "\s+", parse_dates = [[0,1,2]])
print(data.head())

# 2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)

# apply the function fix_century on the column and replace the values to the right ones
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# data.info()
print(data.head())

#  将日期设为索引，注意数据类型，应该是datetime64[ns]
# transform Yr_Mo_Dy it to date type datetime64
data["Yr_Mo_Dy"] = pd.to_datetime(data["Yr_Mo_Dy"])
# set 'Yr_Mo_Dy' as the index
data = data.set_index('Yr_Mo_Dy')  # 原来是一个列，现在变成一行（index）了

print(data.head())

# 对应每一个location，一共有多少数据值缺失
print(data.isnull().sum())

# 对应每一个location，一共有多少完整的数据值
print(data.shape[0]-data.isnull().sum())

# 对于全体数据，计算风速的平均值
print(data.mean())
"""
RPT    12.362987
VAL    10.644314
ROS    11.660526
KIL     6.306468
SHA    10.455834
BIR     7.092254
DUB     9.797343
CLA     8.495053
MUL     8.493590
CLO     8.707332
BEL    13.121007
MAL    15.599079
dtype: float64

Process finished with exit code 0
"""
print(data.mean().mean())
# 10.227982360836924

# 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差
loc_stats = pd.DataFrame()

loc_stats['min'] = data.min() # min
loc_stats['max'] = data.max() # max
loc_stats['mean'] = data.mean() # mean
loc_stats['std'] = data.std() # standard deviations
print(loc_stats)

# 创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差
# create the dataframe
day_stats = pd.DataFrame()

# this time we determine axis equals to one so it gets each row.
day_stats['min'] = data.min(axis = 1) # min
day_stats['max'] = data.max(axis = 1) # max
day_stats['mean'] = data.mean(axis = 1) # mean
day_stats['std'] = data.std(axis = 1) # standard deviations

print(day_stats.head())

# 对于每一个location，计算一月份的平均风速
# (注意，1961年的1月和1962年的1月应该区别对待)
# creates a new column 'date' and gets the values from the index
data['date'] = data.index

# creates a column for each value from date
data['month'] = data['date'].apply(lambda date: date.month)
data['year'] = data['date'].apply(lambda date: date.year)
data['day'] = data['date'].apply(lambda date: date.day)

# gets all value from the month 1 and assign to janyary_winds
january_winds = data.query('month == 1')

# gets the mean from january_winds, using .loc to not print the mean of month, year and day
january_winds.loc[:,'RPT':"MAL"].mean()
print(january_winds.head())

#  对于数据记录按照年为频率取样
print(data.query('month == 1 and day == 1'))
# 对于数据记录按照月为频率取样
print(data.query('day==1'))
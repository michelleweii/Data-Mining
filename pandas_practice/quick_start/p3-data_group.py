import pandas as pd
path3 ='../quick_start/exercise_data/drinks.csv'    #'drinks.csv'
# 将数据框命名为drinks
drinks = pd.read_csv(path3)
print(drinks.head())

# 哪个大陆(continent)平均消耗的啤酒(beer)更多？
a = drinks.groupby('continent').beer_servings.mean()
b = drinks.groupby('continent')
print(a)
# print(b) # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000235D32E0C88>

print('*'*20)
# 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
print(drinks.groupby('continent').wine_servings.describe())

# 打印出每个大陆每种酒类别的消耗平均值
c = drinks.groupby('continent').mean()
print("打印出每个大陆每种酒类别的消耗平均值")
print(c)

# 打印出每个大陆每种酒类别的消耗中位数
d = drinks.groupby('continent').median()
print(d)

# 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
print("打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值")
e = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])
print(e)
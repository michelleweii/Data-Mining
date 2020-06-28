# 运行以下代码
import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

path9 = '../quick_start/exercise_data/Apple_stock.csv'   # Apple_stock.csv
apple = pd.read_csv(path9)
print(apple.head())
print(apple.dtypes)
# 将Date这个列转换为datetime类型
apple.Date = pd.to_datetime(apple.Date)
print(apple['Date'].head())

# 将Date设置为索引
apple = apple.set_index('Date')
print(apple.head())

# 有重复的日期吗？
print(apple.index.is_unique)
# 将index设置为升序
apple = apple.sort_index(ascending = True)
print(apple.head())

# 找到每个月的最后一个交易日(business day)
apple_month = apple.resample('BM')
print(apple_month.mean().head())

# 数据集中最早的日期和最晚的日期相差多少天？
print((apple.index.max() - apple.index.min()).days)

# 在数据中一共有多少个月？
apple_months = apple.resample('BM').mean()
print(apple_months)
print(len(apple_months.index))

# 按照时间顺序可视化Adj Close值
## makes the plot and assign it to a variable
appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)
fig.show()
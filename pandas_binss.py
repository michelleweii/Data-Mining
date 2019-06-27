import numpy as np
import pandas as pd
from pandas import DataFrame # 一般数据就都是二维的，不会是series了

score_list = np.random.randint(25, 100, size=20)
print(score_list)

df1 = DataFrame()
df1['Score'] = score_list
print(df1.head())
"""
   Score
0     45
1     52
2     74
3     70
4     53
"""
# pd.util.testing.rands(3) for i in range(20)可以生成20个随机3位字符串
df1['Student'] = [pd.util.testing.rands(3) for i in range(20)]
print(df1.head())
"""
   Score Student
0     85     Dqh
1     60     AaZ
2     50     O0R
3     71     8lk
4     62     Afd
5     26     Dsh
"""

# 指定一个分箱原则，规定：0-59为不及格，59-70为一般，70-80为良好，80-100位优秀
bins = [0,59,70,80,100]
# 利用pandas中的cut方法，指定分箱规则和对象，结果将获得一个Categories对象
print(pd.cut(df1['Score'],bins).head())

"""
0      (0, 59]
1    (80, 100]
2      (0, 59]
3      (0, 59]
4      (0, 59]
Name: Score, dtype: category
Categories (4, interval[int64]): [(0, 59] < (59, 70] < (70, 80] < (80, 100]]
"""

# 将这个对象作为新的一列加入df1中
df1['Categories'] = pd.cut(df1['Score'],bins)
print(df1.head())
"""
   Score Student Categories
0     83     59q  (80, 100]
1     95     Hau  (80, 100]
2     62     jRj   (59, 70]
3     76     c0r   (70, 80]
4     60     WE4   (59, 70]
"""
# 指定label参数为每个区间赋一个标签
df1['Categories'] = pd.cut(df1['Score'],bins,labels=['low','ok','good','great'])
print(df1.head())
"""
   Score Student Categories
0     30     xPe        low
1     82     FpO      great
2     94     NiV      great
3     25     RMP        low
4     47     R8F        low
"""

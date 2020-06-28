import pandas as pd
path2 = "../quick_start/exercise_data/Euro2012_stats.csv"      # Euro2012_stats.csv
# 将数据集命名为euro12
euro12 = pd.read_csv(path2)
print(euro12)
# 只选取 Goals 这一列
print(euro12.Goals)
# 有多少球队参与了2012欧洲杯？
print(euro12.shape[0])
# 该数据集中一共有多少列(columns)?
print(euro12.info())
# 将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)
# 对数据框discipline按照先Red Cards再Yellow Cards进行排序
a = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)
print("rank_result:{}".format(a))

# 计算每个球队拿到的黄牌数的平均值
print(round(discipline['Yellow Cards'].mean()))

# 找到进球数Goals超过6的球队数据 euro12[euro12.Goals>6]
print(euro12[euro12.Goals>6])

#  选取以字母G开头的球队数据 euro12[euro12.Team.str.startswith('G')]
print(euro12[euro12.Team.str.startswith('G')])

# 选取前7列
print(euro12.iloc[:,0:7])

# 选取除了最后3列之外的全部列
print(euro12.iloc[: , :-3])

# 找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
print(euro12.Team.isin(['England', 'Italy', 'Russia']))
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])
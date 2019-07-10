# 先创建一个简单的 DataFrame 实例
# 用一组数据记录各自的得分情况
import pandas as pd, numpy as np
players = ['Garsol','Hardon','Bill','Duran','James','Barter']
scores = [22,34,12,31,26,19]
teams = ['West','West','East','West','East','East']
df = pd.DataFrame({'player':players,'score':scores,'team':teams})
"""
print(df)
   player  score  team
0  Garsol     22  West
1  Hardon     34  West
2    Bill     12  East
3   Duran     31  West
4   James     26  East
5  Barter     19  East

"""
# 可以看出 team 这一列，其实只有两种值：East 和 West，可以将 team 列的类型设定为 category
# 静态
df.team.astype('category')
# print(df.team.astype('category'))
"""
0    West
1    West
2    East
3    West
4    East
5    East
Name: team, dtype: category
Categories (2, object): [East, West]
# df.team 的变量类型变成了category
"""
df['which_team'] = df.team.astype('category')
print(df.which_team.values.value_counts()) # Here
# 动态
# print(pd.Series(scores))
# """
# 0    22
# 1    34
# 2    12
# 3    31
# 4    26
# 5    19
# """
"""
East    3
West    3
dtype: int64
"""
d = pd.Series(scores).describe()
score_ranges = [d['min']-1,d['mean'],d['max']+1]
# print(score_ranges) # [11.0, 24.0, 35.0]
score_labels = ['Role','Star']
# 用pd.cut(ori_data, bins, labels) 方法
# 以bins设定的画界点来将 ori_data 归类，然后用labels中对应的label来作为分类名
# 将高于平均分的划为 Star，低于平均分的划为 Role。
df['level'] = pd.cut(df['score'],score_ranges,labels=score_labels)
print('df :')
print(df)
"""
   player  score  team level
0  Garsol     22  West  Role
1  Hardon     34  West  Star
2    Bill     12  East  Role
3   Duran     31  West  Star
4   James     26  East  Star
5  Barter     19  East  Role
"""
print('\n对比一下 Category 类型的数据和普通的 DataFrame中的列有什么区别')
print('\ndf[\'team\'] 是普通的 DataFrame列')
print(df['team'])
"""
df['team'] 是普通的 DataFrame列
0    West
1    West
2    East
3    West
4    East
5    East
Name: team, dtype: object
"""
print('\ndf[\'level\'] 是 Category 类型的')
print(df['level'])
"""
df['level'] 是 Category 类型的
0    Role
1    Star
2    Role
3    Star
4    Star
5    Role
Name: level, dtype: category
Categories (2, object): [Role < Star]
"""
print('\n可以看出 df[\'level\']有点像是集合，输出信息会去重后列出组成元素')
print(df['level'].get_values())
# ['Role' 'Star' 'Role' 'Star' 'Star' 'Role']
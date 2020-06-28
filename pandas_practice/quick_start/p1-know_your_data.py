import pandas as pd

# 导入数据集
path1 = "../quick_start/exercise_data/chipotle.tsv"    # chipotle.tsv
# 将数据集存入一个名为chipo的数据框内
chipo = pd.read_csv(path1, sep = '\t')
# 查看前10行内容
print(chipo.head(10))
# 数据集中有多少个列(columns)
print(chipo.shape[1])
#  打印出全部的列名称
print(chipo.columns)
# 数据集的索引是怎样的
print(chipo.index)
# 被下单数最多商品(item)是什么?
c = chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity':sum})
c.sort_values(['quantity'],ascending=False,inplace=True)
print(c.head())
# 在item_name这一列中，一共有多少种商品被下单？
print(chipo['item_name'].nunique())
# 在choice_description中，下单次数最多的商品是什么？
print(chipo['choice_description'].value_counts().head())
# 一共有多少商品被下单？
total_items_orders = chipo['quantity'].sum()
print(total_items_orders)
# 将item_price转换为浮点数，原来是一个str
dollarizer = lambda x:float(x[1:-1]) # 从index为1到最后的数据取出来
chipo['item_price'] = chipo['item_price'].apply(dollarizer)
print(chipo['item_price'].head())
# 在该数据集对应的时期内，收入(revenue)是多少
chipo['sub_total'] = round(chipo['item_price']*chipo['quantity'],2)
print(chipo['sub_total'].sum()) # 39237.02
# 在该数据集对应的时期内，一共有多少订单？
print(chipo['order_id'].nunique())
# 每一单(order)对应的平均总价是多少？
a = chipo[['order_id','sub_total']].groupby(by=['order_id']
).agg({'sub_total':'sum'})['sub_total'].mean()
print('meanvalue:{}'.format(a))
#一共有多少种不同的商品被售出？
print(chipo['item_name'].nunique())
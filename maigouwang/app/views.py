from django.shortcuts import render
import pandas as pd
from app.models import *

# Create your views here.
"""
数据预处理
"""
pd.set_option('display.max_columns', None)
mysql_data = Data.objects.all().values()
df = pd.DataFrame(mysql_data)
row = df.index.size  # 数据量
# 对狗狗品种进行分组 查看什么品种的狗狗最多
dog_data = df.groupby("dog_breed", as_index=False).agg(
    count=pd.NamedAgg(column="id", aggfunc="count", ))
df['dog_price'] = df['dog_price'].astype(int)

dog_data_mean = df.groupby('dog_breed', as_index=False).mean()  # 求平均数
dog_data_max = df.groupby('dog_breed', as_index=False).max()  # 求最大值
dog_data_min = df.groupby('dog_breed', as_index=False).min()  # 求最小值 都是价格
dog_data_median = df.groupby('dog_breed', as_index=False).median()  # 求中位数值 都是价格
dog_data_size = df.groupby('dog_breed', as_index=False).size()

dog_data_mean_list_1 = list(dog_data_mean['dog_price'][:4])
dog_data_mean_list = []
for i in dog_data_mean_list_1:
    dog_data_mean_list.append(int(i))

dog_data_max_list = list(dog_data_max['dog_price'][:4])
dog_data_min_list = list(dog_data_min['dog_price'][:4])
dog_data_median_list = list(dog_data_median['dog_price'][:4])
dog_data_size_list = list(dog_data_median['dog_price'][:4])

#
# print(dog_data_max)
# print(dog_data_min)

dog_data = dog_data.sort_values(by="count", ascending=False)  # 排序
dog_breed_list = list(dog_data['dog_breed'][:20])
dog_breed_dict = {'dog_breed': list(dog_data['dog_breed']), 'count': list(dog_data['count'])}
print('------------------------')
dog_breed_quantity = dog_data.index.size  # 狗狗种类数量
"""
print(dog_data.head(20))
print(dog_breed_list)
输出结果
dog_breed  count
3        博美犬    133
44       金毛犬    126
13     拉布拉多犬    116
7        哈士奇    115
26     法国斗牛犬    114
27       泰迪犬    112
19       柯基犬    110
23       比熊犬    109
37       萨摩耶     90
45   阿拉斯加雪橇犬     88
43     边境牧羊犬     83
20        柴犬     82
11     德国牧羊犬     70
46       雪纳瑞     69
47        马犬     60
6        吉娃娃     50
10       巴哥犬     42
18       松狮犬     39
31       约克夏     30
4       卡斯罗犬     28
['博美犬', '金毛犬', '拉布拉多犬', '哈士奇', '法国斗牛犬', '泰迪犬', '柯基犬', '比熊犬', '萨摩耶', '阿拉斯加雪橇犬']
"""
# 利用售卖地址分类 查看哪个城市买狗的最多
dog_salesLocation_data = df.groupby("salesLocation", as_index=False).agg(
    count=pd.NamedAgg(column="id", aggfunc="count", ))
dog_salesLocation_data = dog_salesLocation_data.sort_values(by="count", ascending=False)  # 排序
dog_salesLocation_quantity = dog_salesLocation_data.index.size  # 查看一共有多少个城市
dog_salesLocation_list = list(dog_salesLocation_data['salesLocation'])
dog_salesLocation_list_data = list(dog_salesLocation_data['count'])
print(dog_salesLocation_list[:5])
print(dog_salesLocation_list_data[:5])
print(dog_salesLocation_data.head(20))
# 利用狗狗的年龄分组查看最多年龄占有多少
dog_age_data = df.groupby("dog_age", as_index=False).agg(
    count=pd.NamedAgg(column="id", aggfunc="count", ))
dog_age_data = dog_age_data.sort_values(by="count", ascending=False)  # 排序
dog_age_data_quantity = dog_age_data.index.size  # 查看一共有多少个年龄分布
dog_age_data_list = list(dog_age_data['dog_age'][:5])  # 输出前五名
dog_age_data_list_data = list(dog_age_data['count'][:5])  # 输出前五名数据
print(dog_age_data_list)
print(dog_age_data_list_data)

data = {
    'data_quantity': row,
    'dog_breed_quantity': dog_breed_quantity,
    'dog_salesLocation_quantity': dog_salesLocation_quantity,
    'dog_breed_dict': dog_breed_dict,
    'dog_salesLocation_list': dog_salesLocation_list,  # 地点前五
    'dog_salesLocation_list_data': dog_salesLocation_list_data,  # 前五的数据占有量
    'dog_age_data_list': dog_age_data_list,  # 宠物狗年龄分布
    'dog_age_data_list_data': dog_age_data_list_data,  # 宠物狗年龄数据
    'dog_data_mean_list':dog_data_mean_list,
    'dog_data_max_list':dog_data_max_list,
    'dog_data_min_list':dog_data_min_list,
    'dog_data_median_list':dog_data_median_list,
    'dog_data_size_list':dog_data_size_list,

}


def app(request):
    return render(request, 'index.html', data)

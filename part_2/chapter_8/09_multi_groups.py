#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 复数的组别 Groups。

@Time: 2023/6/26
@Author: Lingchen
@Prescription: P295.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips_10 = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True).sample(10, random_state=42)
print(tips_10)

# 事实上，可以在 .groupby() 过程中添加多个变量。
# 求 sex 和 time 的平均值。
bill_sex_time = tips_10.groupby(['sex', 'time'])
# print(bill_sex_time)

group_avg = bill_sex_time.mean()
print(group_avg)

# 使结果变平。
print(type(group_avg))

print(group_avg.columns)

print(group_avg.index)

# 如果想得到一个普通的平面数据帧，可以对结果调用 .reset_index() 方法。
group_method = tips_10.groupby(['sex', 'time']).mean().reset_index()
print(group_method)

# as_index = False
group_param = tips_10.groupby(['sex', 'time'], as_index=False).mean()
print(group_param)

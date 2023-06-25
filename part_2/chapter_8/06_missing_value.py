#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - missing 值处理。

@Time: 2023/6/25
@Author: Lingchen
@Prescription: P332.
"""
import logging
import seaborn as sns
import numpy as np

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 设置种子，使结果具有确定性。
np.random.seed(42)

# 从提示中抽取10行样本。
tips_10 = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True).sample(10)
print(tips_10)

# 随机选取4个'total_bill'值并将其变为缺失值。
tips_10.loc[
    np.random.permutation(tips_10.index)[:4],
    'total_bill'
] = np.NAN

print(tips_10)

# 这个结果为提供了每列中每个性别值的非缺失值的数量。
# 有三个缺失值为男性，一个缺失值是女性。
count_sex = tips_10.groupby('sex').count()
print(count_sex)


def fill_na_mean(x):
    """
    返回给定向量的平均值。
    :param x: 值。
    :return: 平均值。
    """
    avg = x.mean()
    return x.fillna(avg)


# 如果只看两个total_bill列，就会发现NaN缺失的值填充了不同的值
total_bill_group_mean = (
    tips_10.groupby('sex').total_bill.transform(fill_na_mean)
)

tips_10['fill_total_bill'] = total_bill_group_mean

print(tips_10[['sex', 'total_bill', 'fill_total_bill']])

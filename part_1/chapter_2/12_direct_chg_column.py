#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
直接修改 column (年龄计算)。

@Time: 2023/6/7
@Author: Lingchen
@Prescription: P97.
"""
import logging
import pandas as pd
from pandas.core import frame

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

scientists = pd.read_csv('../../data/scientists.csv')
print(scientists.head())

print(scientists['Age'])

# frac=1 告诉 pandas 随机选择100%的值
# randomstate 使得每次随机化都相同
scientists['Age'] = scientists['Age'].sample(frac=1, random_state=42)
print(scientists['Age'])

# 和上面操作等效。
scientists['Age'] = (
    scientists['Age']
    .sample(frac=1, random_state=42)
)
print(scientists['Age'])

# 我们试图随机打乱列，但当我们将值分配回数据帧时，它又恢复到原始顺序。
# 这是因为 Pandas 在许多操作中都会尝试自动加入.index值。

# 去年 index。
scientists['Age'] = (
    scientists['Age']
    .sample(frac=1, random_state=42)
    .values
)
print(scientists['Age'])

born_datatime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
died_datatime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')

# 我们可以创建一组新的列，其中包含对象（字符串）日期的 datetime 表示。
# 下面的示例使用python的多重赋值语法。
scientists['born_dt'], scientists['died_dt'] = (
    born_datatime,
    died_datatime
)
print(scientists)

# 使用日期时间算术重新计算“实际”年龄。
scientists['age_days'] = (
    scientists['died_dt'] - scientists['born_dt']
)

print(scientists)

# 可以将值转换为年份, 使用 astype 方法。
scientists['age_years'] = (
    scientists['age_days']
    .astype('timedelta64[Y]')
)
print(scientists)

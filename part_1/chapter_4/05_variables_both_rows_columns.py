#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 变量在列和行中。

@Time: 2023/6/17
@Author: Lingchen
@Prescription: P247.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

weather = pd.read_csv('../../data/weather.csv')
print(weather.head())
print(weather.iloc[:5, :11])

# 如果一列数据实际上包含两个变量而不是一个变量。
# 在这种情况下，我们必须将变量"透视"到单独的列中。
# 天气数据包括每天记录的最低 (tmin) 和最高 (tmax) 温度。
weather_melt = weather.melt(
    id_vars=['id', 'year', 'month', 'element'],
    var_name='day',
    value_name='temp'
)
print(weather_melt)

# 需要调整存储在元素列中的变量。
weather_tidy = weather_melt.pivot_table(
    index=['id', 'year', 'month', 'day'],
    columns='element',
    values='temp'
)

print(weather_tidy)

# 使层次结构列变平。
weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat)

# 在没有中间数据帧的情况下应用这些方法。
weather_tidy = (
    weather_melt.pivot_table(
        index=['id', 'year', 'month', 'day'],
        columns='element',
        values='temp'
    ).reset_index()
)
print(weather_tidy)

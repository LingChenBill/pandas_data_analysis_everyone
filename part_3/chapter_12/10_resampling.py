#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 再生。

@Time: 2023/7/5
@Author: Lingchen
@Prescription: P460.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv', parse_dates=['Date'])
print(ebola.head())
ebola.index = ebola['Date']

# 重采样将日期时间从一个频率转换为另一个频率。
# 可能发生三种类型的重采样：
# 降采样：从较高频率到较低频率（例如，每天到每月）
# 上采样：从较低频率到较高频率（例如，每月到每天）
# 无变化：频率不变（例如，每月的第一个星期四到每月的最后一个星期五）

# 将每日值缩减为每月值, 由于有多个值，我们需要聚合结果
# 这里我们将使用平均值。
down = ebola.resample('M').mean()
print(down.iloc[:, :5])

# 在这里，我们将对下采样值进行上采样。
# 注意缺失的日期是如何填充的，但它们被填充了缺失值。
up = down.resample('D').mean()
print(up.iloc[:, :5])

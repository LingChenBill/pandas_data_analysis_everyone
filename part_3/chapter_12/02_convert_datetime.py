#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 转换成日期。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P361.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 将对象类型转换为日期时间类型是通过 to_datatime 函数完成的。
# 让我们加载我们的 ebola 数据集，并将 Date 列转换为正确的日期时间对象。
ebola = pd.read_csv('../../data/country_timeseries.csv')
print(ebola.columns)

# 数据的左上角: 5行5列。
print(ebola.iloc[:5, :5])

# 第一个 Date 列包含日期信息，但 .info() 属性告诉它实际上是作为 Pandas 中的通用字符串对象编码的。
print(ebola.info())

# 创建一个新列 date_dt，用于将"日期"列转换为日期时间。
ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola.info())

# to_datetime() 函数有一个名为 format 的参数，它允许您手动指定希望分析的日期的格式。
# 由于我们的日期是月/日/年格式，我们可以传入字符串%m/%d/%Y。
ebola['date_dt'] = pd.to_datetime(ebola['Date'], format='%m/%d/%Y')
print(ebola.info())

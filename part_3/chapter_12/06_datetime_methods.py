#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 日期方法。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P434.
"""
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

banks = pd.read_csv('../../data/banklist.csv')
print(banks.head())
print(banks.columns)

banks_d = pd.read_csv('../../data/banklist.csv', parse_dates=['Closing Date', 'Updated Date'])
print(banks_d.info())

# 可以通过获得银行倒闭的季度和年份来解析日期。
banks_d = banks_d.assign(
    closing_quarter=banks_d['Closing Date'].dt.quarter,
    closing_year=banks_d['Closing Date'].dt.year
)

closing_year = banks_d.groupby(['closing_year']).size()

# 可以计算出每年每个季度有多少家银行倒闭。
closing_year_q = (
    banks_d
    .groupby(['closing_year', 'closing_quarter'])
    .size()
)

# 绘图。
fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()

fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()

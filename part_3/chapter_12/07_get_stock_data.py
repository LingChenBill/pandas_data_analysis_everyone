#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 获取库存数据。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P438.
"""
import logging
import pandas as pd
# import pandas_datareader.data as web

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 该端口已经弃用。
# tesla = web.DataReader('TSLA', 'yahoo')
# print(tesla)

# 库存数据已保存。
# 所以不需要再依赖互联网了, 相反，可以加载与文件相同的数据集。
tesla = pd.read_csv('../../data/tesla_stock_yahoo.csv', parse_dates=['Date'])
print(tesla)

# 如果只想从我们的股价数据集中获得2010年6月的数据，可以使用布尔子集。
print(
    tesla.loc[
        (tesla.Date.dt.year == 2010) & (tesla.Date.dt.month == 6)
    ]
)

# 当处理日期时间数据时，通常需要将日期时间对象设置为数据帧的索引。
tesla.index = tesla['Date']
print(tesla.index)

# 将索引设置为日期对象后，现在可以直接使用日期对行进行子集。
# 例如，可以根据 年份 对数据进行子集设置。
# 不提倡，后续版本可能不支持。
# print(tesla['2015'])

# print(tesla['2010-06'])

# 时间增量索引。
tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
tesla.index = tesla['ref_date']
print(tesla)

# 根据这些增量选择我们的数据。
print(tesla['0 days': '10 days'])

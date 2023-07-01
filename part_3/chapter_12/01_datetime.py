#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - datetime。

@Time: 2023/7/1
@Author: Lingchen
@Prescription: P360.
"""
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 使用datetime获取当前日期和时间。
now = datetime.now()
print(f'Last time this chapter was rendered for print: {now}')

t1 = datetime.now()
t2 = datetime(1970, 1, 1)
print(t1)
print(t2)

diff = t1 - t2
print(diff)

# 日期计算的数据类型是时间增量 timedelta。
print(type(diff))

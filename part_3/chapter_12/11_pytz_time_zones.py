#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 时区。

@Time: 2023/7/5
@Author: Lingchen
@Prescription: P462.
"""
import logging
import pytz
import re
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 图书馆中有许多时区可用。
print(len(pytz.all_timezones))

# US时区。
regex = re.compile(r'^US')
selected_files = filter(regex.search, pytz.common_timezones)
print(list(selected_files))

# 如果肯尼迪机场和洛杉矶国际机场之间的航班于上午 7：00 从纽约起飞，并于上午 9：57 降落在洛杉矶。
# 可以用正确的时区对这些时间进行编码。

# 7AM 东区。
depart = pd.Timestamp('2017-08-29 07:00', tz='US/Eastern')
print(depart)

arrive = pd.Timestamp('2017-08-29 09:57')
print(arrive)

# 可以对时区进行编码的另一种方法是 .tz_localize 在 "空"时间戳。
arrive = arrive.tz_localize('US/Pacific')
print(arrive)

# 可以将到达时间转换回东部时区，看看航班到达时东海岸的时间。
print(arrive.tz_convert('US/Eastern'))

# 在时区上执行操作。
# 在这里，我们查看时间之间的差异，以获得飞行时间。
duration = arrive - depart
print(duration)

#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 日期平移值处理。

@Time: 2023/7/2
@Author: Lingchen
@Prescription: P388.
"""
import logging
import pandas as pd
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

ebola = pd.read_csv('../../data/country_timeseries.csv', parse_dates=['Date'])
print(ebola.head())

# 可能希望将日期更改某个值，这有几个原因。
# 例如，可能需要更正数据中的某种测量错误。或者，可能希望标准化数据的开始日期，以便比较趋势。
ebola.index = ebola['Date']

# 尽管我们的 埃博拉 病毒数据并不“整洁”，但目前格式的数据的好处之一是，它可以让我们绘制疫情图。
fig, ax = plt.subplots()
ax = ebola.plot(ax=ax)
ax.legend(fontsize=10, loc=2, borderaxespad=0.0)
plt.show()

# 当我们观察疫情时，一个有用的信息是疫情相对于其他国家的传播速度。
# 让我们看看埃博拉数据集中的几列。
ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))

# 希望所有日期都从一个共同的0天开始。
# 这个过程有多个步骤:
# (1) 由于没有列出每个日期，我们需要创建数据集中所有日期的日期范围。
# (2) 需要计算数据集中最早的日期与每列中最早的有效（非NaN）日期之间的差异。
# (3) 我们可以将每个列移动这个计算值。
ebola = pd.read_csv(
    '../../data/country_timeseries.csv',
    index_col='Date',
    parse_dates=['Date']
)
print(ebola.iloc[:, :4])

# 需要创建日期范围来填充数据中所有缺失的日期。
# 然后，当向下移动日期值时，数据将移动的天数将与将移动的行数相同。
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
print(new_idx)

# 查看我们的 new_idx，发现日期没有按照我们想要的顺序。
# 要解决这个问题，我们可以颠倒索引的顺序。
new_idx = reversed(new_idx)
print(new_idx)

# 可以正确地 .reindex() 我们的数据。如果数据集中不存在索引，这将创建 NaN 值的行。
ebola = ebola.reindex(new_idx)
print(ebola.iloc[:, :4])

# .last_valid_index()，它返回最后一个非缺失或非 null 值的标签（索引）。
# 一个名为.first_valid_index的类似方法返回第一个非缺失和非null值。
# 由于想在所有列中执行此计算，因此可以使用 .apply() 方法。
last_valid = ebola.apply(pd.Series.last_valid_index)
print(last_valid)

earliest_date = ebola.index.min()
print(earliest_date)

# 从每个上次有效日期中减去此日期。
shift_values = last_valid - earliest_date
print(shift_values)

# 可以遍历每一列，使用 .shift() 方法将列下移 shift_values 中相应的值。
# 请注意，shift_values 中的值都是正的。如果它们是负的（如果我们翻转减法的顺序），则此操作会将值上移。
ebola_dict = {}

for idx, col in enumerate(ebola):
    d = shift_values[idx].days
    shifted = ebola[col].shift(d)
    ebola_dict[col] = shifted

print(ebola_dict)

# 每列的最后一行现在都有一个值；也就是说，列已经适当地下移了。
ebola_shift = pd.DataFrame(ebola_dict)
print(ebola_shift.tail())

# 由于每行的指数不再有效，我们可以删除它们，然后指定正确的指数，即当天。
# 请注意，当天不再代表整个疫情爆发的第一天，而是特定国家疫情爆发的第一天。
ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Day'], axis='columns')
print(ebola_shift.tail())

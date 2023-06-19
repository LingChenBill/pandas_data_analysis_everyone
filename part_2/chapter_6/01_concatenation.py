#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - dict 数据连接。

@Time: 2023/6/19
@Author: Lingchen
@Prescription: P275.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

df1 = pd.read_csv('../../data/concat_1.csv')
df2 = pd.read_csv('../../data/concat_2.csv')
df3 = pd.read_csv('../../data/concat_3.csv')

print(df1)
print(df2)
print(df3)

# .index 指的是数据帧左侧的标签，默认情况下，它们将从0开始编号。
print(df1.index)

# 这是指数据帧的列名。
print(df1.columns)

# 为了完整起见，数据帧的主体可以表示为带有 .values 的 numpy 数组。
print(df1.values)

# 将数据帧堆叠(即串联)在一起使用 panda 中的 concat() 函数。
# 所有要串联的数据帧都在列表中传递。
row_concat = pd.concat([df1, df2, df3])
print(row_concat)

# 获取数据帧的第四行的子集。
print(row_concat.iloc[3, :])

# 创建一个新的列。
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(new_row_series)

# 尝试将新行添加到数据帧。
# series 没有匹配的列，所以我们的 new_row 被添加到一个新列中。
# 其余的值被连接到数据帧的底部，原始索引值被保留。
print(pd.concat([df1, new_row_series]))

# 需要将我们的系列转换为一个数据帧。
# 这个数据帧包含一行数据，列名是数据将绑定到的列名。
new_row_df = pd.DataFrame(
    data=[['n1', 'n2', 'n3', 'n4']],
    columns=['A', 'B', 'C', 'D']
)
print(new_row_df)

# 连接df。
print(pd.concat([df1, new_row_df]))

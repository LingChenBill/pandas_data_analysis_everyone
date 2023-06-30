#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 字符串方法。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P399.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# join() 方法获取一个容器（例如列表）并返回一个新字符串，该字符串组合了列表中的每个元素。

# 例如，假设我们想用度、分、秒（DMS）表示法组合坐标。

d1 = '40°'
m1 = "46'"
s1 = '52.837"'
u1 = 'N'

d2 = '73°'
m2 = "58'"
s2 = '26.302"'
u2 = 'W'

# 通过对空格字符串使用 .join() 方法，用空格 ' ' 连接所有值。
coords = ' '.join([d1, m1, s1, u1, d2, m2, s2, u2])
print(coords)

# 如果有要使用自己的分隔符分隔的字符串列表（例如，带\t的制表符和逗号），此方法也很有用。
print(coords.split(' '))

multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.”
"""
print(multi_str)

multi_str_split = multi_str.splitlines()
print(multi_str_split)

# 假设我们只是想从"警卫"那里得到文本。
# 这是两个人的谈话，所以"警卫"每隔一句话就说一次。
guard = multi_str_split[::2]
print(guard)

# 有几种方法可以从"警卫"那里获得台词。
# 一种方法是对字符串使用 .replace() 方法，并对带有空字符串''的Guard:
# 字符串使用 .replace() 方法。
# 然后我们可以使用 .splitlines() 方法。
guard = multi_str.replace('Guard: ', '').splitlines()[::2]
print(guard)

#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 获取字符串子串。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P396.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

word = 'grail'
sent = 'a scratch'

print(word)
print(sent)

# 由于 Python 是右侧独占的，需要指定一个比上一个索引大一的索引位置。
# 请注意，最后一个索引是一个小于为 len 返回的数字。
s_len = len(sent)
print(s_len)

print(sent[2:s_len])

# 此任务的另一个快捷方式是省略：左侧或右侧的数据。
# 如果 : 的左侧为空，则切片将从左侧开头到右侧索引的结束（不包括在内）。
# 如果 : 右侧为空，那么切片将从左侧索引开始并结束于字符串的结尾。
print(word[0:3])

# 左侧为空。
print(word[:3])

print(sent[2:len(sent)])

# 右侧为空。
print(sent[2:])

# 指定整个字符串将两个值都保留为空。
print(sent[:])
print(sent[0:len(sent)])

# 切片时的最后一个符号允许您以增量进行切片。
# 为此，可以使用第二个冒号 : 来提供第三个数字。
# 第三个数值允许指定要提取值的增量。

# 逐2，每隔一个字符。
print(sent[::2])

print(sent[::3])

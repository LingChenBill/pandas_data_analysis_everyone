#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 字符串-切片。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P393.
"""
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

word = 'grail'
sent = 'a scratch'

print(word)
print(sent)

# 字符串可以被认为是字符的容器。
# 可以像任何其他 Python 容器一样对字符串进行子集设置。

# 要获得字符串的第一个字母，我们可以使用方括号表示法[]。
# 这种表示法与我们在第1.3节中查看各种数据片段时使用的方法相同。
print(word[0])
print(sent[3])

# 可以使用切片表示法从字符串中获取范围--它包含左侧，右侧除外。
# 获取前3个字符。
# 注意索引3实际上是第4个字符。
print(word[0:3])

# 传入负索引实际上是从容器的末尾开始计数。
print(sent[-1])

print(sent[-9:-8])

# 可以将非负数与负数组合使用。
# a
print(sent[0:-8])

# 当对第二个值使用负索引时，实际上无法获得最后一个字母。
# scratc
print(sent[2:-1])

print(sent[-7:-1])

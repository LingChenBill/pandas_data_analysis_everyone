#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 汇编模式。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P416.
"""
import logging
import re

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# Python 的 re 模块允许 compile() 一个模式，以便重用它。
# 这可以带来性能优势，尤其是在数据集很大的情况下。

# 匹配10位数字的模式。
p = re.compile('\d{10}')
s = '1234567890'

# 注意: 对编译后的模式调用 match。
# 不使用 re.match 函数。
m = p.match(s)
print(m)

p = re.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)

m = p.findall(s)
print(m)

p = re.compile('\w+\s?\w+:\s?')
s = "Guard: You're using coconuts!"

m = p.sub(string=s, repl='')
print(m)

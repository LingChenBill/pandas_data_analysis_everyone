#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - regex library。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P418.
"""
import logging
import regex

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 使用 regex 库的再示例。
p = regex.compile('\d+')
s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)

m = p.findall(s)
print(m)

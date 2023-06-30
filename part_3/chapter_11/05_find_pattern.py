#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 查找一个匹配。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P414.
"""
import logging
import re

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 可以使用 findall() 函数来查找模式中的所有匹配项。
# 让编写一个匹配数字的模式，并使用它来查找字符串中的所有数字。

s = (
    "14 Ncuti Gatwa, "
    "13 Jodie Whittaker, war John Hurt, 12 Peter Capaldi, "
    "11 Matt Smith, 10 David Tennant, 9 Christopher Eccleston"
)
print(s)

# 匹配一个或多个数字的模式。
p = '\d+'

m = re.findall(pattern=p, string=s)
print(m)

# 使用正则表达式，可以推广模式，这样就可以从 Guard 那里得到行内容，也可以从 King Arthur 那里得到行内容。
multi_str = """Guard: What? Ridden on a horse?
King Arthur: Yes!
Guard: You're using coconuts!
King Arthur: What?
Guard: You've got ... coconut[s] and you're bangin' 'em together.
"""

p = (
    '\w+'           # 多个字符。
    '\s?'           # 可能有一个空格。
    '\w+'           # 多个字符。
    ':'             # :
    '\s?'           # 可能有一个空格。
)

s = re.sub(pattern=p, string=multi_str, repl='')
print(s)

# 可以通过使用带增量的字符串切片来获得任何一方的行。
guard = s.splitlines()[::2]
kinga = s.splitlines()[1::2]

print(guard)

print(kinga)

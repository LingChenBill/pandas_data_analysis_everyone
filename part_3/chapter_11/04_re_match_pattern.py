#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 正则匹配模式。

@Time: 2023/6/30
@Author: Lingchen
@Prescription: P408.
"""
import logging
import re

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 将使用 re 模块来编写要在字符串中匹配的正则表达式模式。
# 编写一个匹配10位数字的模式。
tele_num = '1234567890'

# 使用 match() 函数查看模式是否与字符串匹配。
m = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tele_num)
print(type(m))
print(m)

# 如果我们查看打印的匹配对象，我们会发现，
# 如果有匹配，span 标识匹配发生的字符串的索引，match 标识匹配的确切字符串。

# 如果只需要返回 True/False 值，可以运行内置的 bool() 函数来获取匹配对象的布尔值。
print(bool(m))

if m:
    print('match')
else:
    print('no match')

# 如果想提取一些匹配对象值，例如索引位置或匹配的实际字符串，可以在匹配对象上使用一些方法。
# 获取字符串匹配的第一个索引。
print(m.start())

# 获取字符串匹配的最后一个索引。
print(m.end())

# 获取字符串匹配的第一个和最后一个索引。
print(m.span())

# 获取匹配的字符串。
print(m.group())

tele_num_spaces = '123 456 7890'

m = re.match(pattern='\d{10}', string=tele_num_spaces)

# 可以判断出模式不匹配，因为 match 对象返回None。
# 如果我们再次运行If语句，它将打印 'no match'。
print(m)

if m:
    print('match')
else:
    print('no match')

# 可以将 RegEx 模式视为一个单独的变量, 因为它可能会变长使实际的匹配函数调用难以读取。
p = '\d{3}\s?\d{3}\s?\d{4}'
m = re.match(pattern=p, string=tele_num_spaces)
print(m)

# 区号也可以用括号和七个主数字之间的短划线括起来。
tele_num_space_paren_dash = '(123) 456-7890'

p = '\(?\d{3}\)?\s?\d{3}\s?-?\d{4}'
m = re.match(pattern=p, string=tele_num_space_paren_dash)
print(m)

# 最后，数字前面可能有一个国家代码。
cnty_tele_num_space_paren_dash = '+1 (123) 456-7890'

p = '\+?1\s?\(?\d{3}\)?\s?\d{3}\s?-?\s?\d{4}'
m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)

# 也可以对想要拆分成多行的非常长的URL使用这个技巧。
# 这也意味着可以将长模式字符串拆分为多行。
# 可以告诉 python 将所有单独的字符串视为一个值，
# 可以通过将语句包装在一对圆括号 () 周围来将其分配给变量。
# 为了代码可读性，可以加上注释，便于以后维护。
# '+1 (123) 456-7890'
p = (
    '\+?'           # 可能 + 开始。
    '1'             # 数字1。
    '\s?'           # 可能有一个空格。
    '\(?'           # 可能有一个左 (。
    '\d{3}'         # 3个数字。
    '\)?'           # 可能有一个右 )。
    '\s?'           # 可能有一个空格。
    '\d{3}'         # 3个数字。
    '\s?'           # 可能有一个空格。
    '-?'            # 可能有一个 -。
    '\s?'           # 可能有一个空格。
    '\d{4}'         # 4个数字。
)

print(p)

m = re.match(pattern=p, string=cnty_tele_num_space_paren_dash)
print(m)

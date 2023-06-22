#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 使用 assert 来验证。

@Time: 2023/6/22
@Author: Lingchen
@Prescription: P304.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

person = pd.read_csv('../../data/survey_person.csv')
site = pd.read_csv('../../data/survey_site.csv')
survey = pd.read_csv('../../data/survey_survey.csv')
visited = pd.read_csv('../../data/survey_visited.csv')

ps = person.merge(survey, left_on='ident', right_on='person')
print(ps)

print(ps.shape)

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

print(vs.shape)

ps_vs = ps.merge(
    vs,
    left_on=['quant'],
    right_on=['quant']
)
print(ps_vs)

print(ps_vs.shape)

# 可以使用 Python assert 语句来实现这一点。
# 当一个表达式的计算结果为 True 时，assert 不会返回任何内容，您的代码将继续到下一个表达式。
assert vs.shape[0] == 21

# 如果要断言的表达式的计算结果为 False，它将抛出 AssertionError，代码将停止。
# AssertionError
# assert ps_vs.shape[0] <= vs.shape[0]

# 每种类型的观测单元形成一个表格。

#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 合并数据集（包含缺失值）

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P360.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

visited = pd.read_csv('../../data/survey_visited.csv')
survey = pd.read_csv('../../data/survey_survey.csv')

print(visited)

print(survey)

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

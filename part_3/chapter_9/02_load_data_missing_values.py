#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 加载数据（包含缺失值）

@Time: 2023/6/27
@Author: Lingchen
@Prescription: P359.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

visited_file = '../../data/survey_visited.csv'

df = pd.read_csv(visited_file)
print(df)

df = pd.read_csv(visited_file, keep_default_na=False)
print(df)

df = pd.read_csv(visited_file, na_values=[""], keep_default_na=False)
print(df)

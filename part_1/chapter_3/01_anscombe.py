#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
可视化数据-安斯科姆四重奏

@Time: 2023/6/10
@Author: Lingchen
@Prescription: P120.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 加载本地数据。加载 library 中的数据会因为外网连接的原因出错。
anscombe = sns.load_dataset('anscombe', data_home='../../data/seaborn-data', cache=True)
print(anscombe)

#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - sklearn 线性回归。

@Time: 2023/7/19
@Author: Lingchen
@Prescription: P407.
"""
import logging
import seaborn as sns
from sklearn import linear_model

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

lr = linear_model.LinearRegression()

# 我们需要指定预测因子X和响应Y。为此，我们传入要用于模型的列。
# ValueError: Expected 2D array, got 1D array instead:
# predicted = lr.fit(X=tips['total_bill'], y=tips['tip'])

# AttributeError: 'Series' object has no attribute 'reshape'
# predicted = lr.fit(X=tips['total_bill'].reshape(-1, 1), y=tips['tip'])

predicted = lr.fit(
    X=tips['total_bill'].values.reshape(-1, 1), y=tips['tip']
)

# 为了获得 sklearn 中的系数，我们在拟合模型上调用 .coef_ 属性。
print(predicted.coef_)

# 为了获得截距，我们调用 .intercept_ 属性。
print(predicted.intercept_)

#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 多次回归。

@Time: 2023/7/19
@Author: Lingchen
@Prescription: P410.
"""
import logging
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn import linear_model

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 我们可以使用多元回归将多个预测因子放入模型中。
# 将多元回归模型拟合到数据集与拟合简单的线性回归模型非常相似。
# 使用公式界面，我们将其他协变量添加到右侧。
model = smf.ols(formula='tip ~ total_bill + size', data=tips).fit()

print(model.summary())

# sklearn 中多元回归的语法与这个库的简单线性回归语法非常相似。
# 为了向模型添加更多特征，我们传入了要使用的列。
lr = linear_model.LinearRegression()

# 因为我们正在执行多元回归, 我们不再需要重塑我们的 X 值。
predicted = lr.fit(X=tips[['total_bill', 'size']], y=tips['tip'])

print(predicted.coef_)
print(predicted.intercept_)

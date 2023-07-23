#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - Scikit-learn中的分类变量

@Time: 2023/7/23
@Author: Lingchen
@Prescription: P.
"""
import logging
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn import linear_model

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# Pandas 中的 get_dummies() 函数可以为我们创建数据帧的虚拟变量编码。
tips_dummy = pd.get_dummies(
    tips[['total_bill', 'size', 'sex', 'smoker', 'day', 'time']]
)
print(tips_dummy)

# 要删除引用变量，我们可以传入 drop_first=True。
x_tips_dummy_ref = pd.get_dummies(
    tips[['total_bill', 'size', 'sex', 'smoker', 'day', 'time']],
    drop_first=True
)
print(x_tips_dummy_ref)

lr = linear_model.LinearRegression()
predicted = lr.fit(X=x_tips_dummy_ref, y=tips['tip'])
print(predicted.intercept_)
print(predicted.coef_)

# 当试图从 sklearn 解释模型时，令人讨厌的事情之一是系数没有被标记。
# 省略标签是因为 numpy ndarray 无法存储这种类型的元数据。
# 如果我们希望我们的输出类似于 statsmodels 中的东西，我们需要手动存储标签并将系数附加到它们。
values = np.append(predicted.intercept_, predicted.coef_)

names = np.append('intercept', x_tips_dummy_ref.columns)

results = pd.DataFrame({
    'variable': names,
    'coef': values
})
print(results)

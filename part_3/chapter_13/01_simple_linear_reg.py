#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 简单的线性回归。

@Time: 2023/7/19
@Author: Lingchen
@Prescription: P404.
"""
import logging
import seaborn as sns
import statsmodels.formula.api as smf

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# 为了执行这个简单的线性回归，使用 ols() 函数，它计算普通的最小二乘值;
# 它是估计线性回归中的参数的一种方法。
# 回想一下，一条线的公式是 y = mx + b，其中 y 是我们的响应变量，x 是我们的预测变量，b 是截距，m 是斜率，即我们正在估计的参数。
# 公式表示法由两部分组成，用波浪号 ~ 分隔。
# 波浪号的左侧是响应变量，波浪号的右侧是预测变量。
model = smf.ols(formula='tip ~ total_bill', data=tips)

# 一旦我们指定了我们的模型，我们就可以使用 fit 方法将数据拟合到模型中。
results = model.fit()

print(results.summary())

# 在这里，我们可以看到模型的截距和 total_bill。
# 我们可以在直线的公式中使用这些参数，y = （0.105）x + 0.920。
# 为了解释这些数字，我们说：total_bill每增加一个单位（即，每增加一美元），小费就会增加0.105（即10.5美分）。
# 如果我们只想要系数，我们可以在结果上调用 .params 属性。
print(results.params)

# 置信区间包括小于 [0.025 0.975] 的值。我们也可以使用 .conf_int() 方法提取这些值。
print(results.conf_int())

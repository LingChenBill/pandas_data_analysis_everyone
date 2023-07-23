#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - scikit-learn中的独热编码

@Time: 2023/7/23
@Author: Lingchen
@Prescription: P.
"""
import logging

import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn import linear_model

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())

# Scikit-learn 有自己的数据处理方式，使用“管道”进行分析。
# 我们可以在管道中使用独热编码转换器来处理数据，而不是在拟合模型之前使用 pandas 在 scikit-learn 中处理数据。
categorical_features = ['sex', 'smoker', 'day', 'time']
categorical_transformer = OneHotEncoder(drop='first')

# 一旦我们有了我们想要的列和处理步骤，我们就可以将这些步骤传递给 ColumnTransformer()。
# 由于我们希望在最终模型中仍然具有数值变量，但没有为它们指定处理步骤，
# 因此我们传入 remainder=“passthrough” 以确保那些在转换器步骤中未指定的变量仍然进入最终模型。
preprocessor = ColumnTransformer(
    transformers= [
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='passthrough'
)

# 我们可以创建一个包含所有预处理步骤的 Pipeline()，然后创建我们想要的模型。
pipe = Pipeline(
    steps = [
        ('preprocessor', preprocessor),
        ('lr', linear_model.LinearRegression()),
    ]
)

pipe.fit(
    X=tips[['total_bill', 'size', 'sex', 'smoker', 'day', 'time']],
    y=tips['tip']
)

Pipeline(steps=[('preprocessor',
                 ColumnTransformer(remainder='passthrough',
                                   transformers=[('cat', OneHotEncoder(drop='first'),
                                                  ['sex', 'smoker', 'day', 'time'])])),
                 ('lr', linear_model.LinearRegression())])

print(type(pipe))

# 我们需要在额外的步骤中访问系数。
# 这是因为并非所有模型都有intercept_和coef_值，Pipeline() 是一个通用函数，适用于 sklearn 库中的任何模型。
coefficients = np.append(
    pipe.named_steps['lr'].intercept_, pipe.named_steps['lr'].coef_
)

labels = np.append(
    ['intercept'], pipe[:-1].get_feature_names_out()
)

coefs = pd.DataFrame(
    {
        'variable': labels,
        'coef': coefficients
    }
)
print(coefs)

# 请注意，这里的系数与 statsmodels 的值不完全相同，因为参考变量不同。

# 本章介绍了使用 statsmodels 和 sklearn 库拟合模型的基础知识。
# 在拟合模型时，经常使用添加特征和创建虚拟变量的概念。
# 到目前为止，我们已经专注于拟合线性模型，其中响应变量是连续变量。
# 在后面的章节中，我们将拟合响应变量不是连续变量的模型。

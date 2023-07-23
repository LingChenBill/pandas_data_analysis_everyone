#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 具有分类变量的模型。

@Time: 2023/7/23
@Author: Lingchen
@Prescription: P411.
"""
import logging
import seaborn as sns
import statsmodels.formula.api as smf

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

tips = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True)
print(tips.head())
print(tips.info())

print(tips.sex.unique())

# 如果我们有一列指示一个人是否是女性，那么我们知道这个人是否不是女性（在我们的数据中），那个人一定是男性。
# 在这种情况下，我们可以有效地删除为男性编码的虚拟变量，并且仍然具有相同的信息。
model = smf.ols(
    formula='tip ~ total_bill + size + sex + smoker + day + time',
    data=tips
).fit()

# 我们可以从摘要中看到，statsmodels 会自动创建虚拟变量，并删除引用变量以避免多重共线性。
print(model.summary())

# 对连续（即数字）参数的解释与以前相同。
# 但是，我们对分类变量的解释必须与参考变量（即从分析中删除的虚拟变量）相关。
# 例如，性别系数 [T.Female] 为 0.0324。我们根据参考值 Male 来解释此值;
# 也就是说，我们说当服务器的性别从男性“改变”为女性时，提示增加 0.324。对于日变量：
print(tips.day.unique())
# 我们看到我们的 .summary() 缺少 Thur，因此这是用于解释系数的参考变量。

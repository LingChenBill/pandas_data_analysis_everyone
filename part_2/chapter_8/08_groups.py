#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - Groups。

@Time: 2023/6/26
@Author: Lingchen
@Prescription: P290.
"""
import logging
import seaborn as sns

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

# 在执行其他方法之前，实际上可以保存 .groupby() 的结果。
tips_10 = sns.load_dataset('tips', data_home='../../data/seaborn-data', cache=True).sample(10, random_state=42)
print(tips_10)

# 仅保存分组对象。请注意，只是取回对象及其内存位置。
grouped = tips_10.groupby('sex')
print(grouped)

# 如果想真正看到计算出的组，我们可以调用 groups 属性。
print(grouped.groups)

# 包含多个变量的群计算。
# 请求原谅比请求许可更容易。
# 计算相关列的平均值。
avgs_grouped = grouped.mean()
print(avgs_grouped)

# 列举所有的列。
print(tips_10.columns)

# 获取 'Female' 组别。
female = grouped.get_group('Female')
print(female)

# 循环 组别 信息。
for sex_group in grouped:
    print(sex_group)

# 无法真正从分组对象中获取0元素。
# KeyError: 'Column not found: 0'
# print(grouped[0])

# 有一个双元素元组，其中第一个元素是表示 Male 键的 str（字符串），第二个元素是 Male 数据的 DataFrame。
for sex_group in grouped:
    print(f'the type is: {type(sex_group)}\n')

    print(f'the length is: {len(sex_group)}\n')

    first_element = sex_group[0]
    print(f'the first element is:{first_element}\n')

    print(f'it has a type of: {type(sex_group[0])}\n')

    second_element = sex_group[1]
    print(f'the second element is: \n{second_element}\n')
    print(f'it has a type of : {type(second_element)}\n')

    print(f'what we have:')
    print(sex_group)

    break

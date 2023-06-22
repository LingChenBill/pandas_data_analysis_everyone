#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 合并不同的数据集。

@Time: 2023/6/22
@Author: Lingchen
@Prescription: P296.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

person = pd.read_csv('../../data/survey_person.csv')
site = pd.read_csv('../../data/survey_site.csv')
survey = pd.read_csv('../../data/survey_survey.csv')
visited = pd.read_csv('../../data/survey_visited.csv')

print(person)
print(site)
print(survey)
print(visited)

# 如果想查看每个站点的日期以及该站点的纬度和经度信息，我们必须组合(并合并)多个数据帧。
# 我们可以使用 Pandas 中的 .merge() 方法来实现这一点。

visited_subset = visited.loc[[0, 2, 6], :]
print(visited_subset)

# 统计值的个数。
print(visited_subset['site'].value_counts())

# 一对一合并。
# 现在已经从两个独立的数据帧中创建了一个新的数据帧，其中的行是根据一组特定的列进行匹配的。
# 在SQL中，用于匹配的列被称为"键"。

# pandas.errors.MergeError: No common columns to perform merge on.
# Merge options: left_on=None, right_on=None, left_index=False, right_index=False
# o2o_merge = site.merge(visited_subset)

o2o_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(o2o_merge)

# 多对一合并。
print(visited['site'].value_counts())

print(site)
print(visited)

# 站点信息(名称、纬度和经度)是重复的，并与访问的数据相匹配。
m2o_merge = site.merge(visited, left_on='name', right_on='site')
print(m2o_merge)

# 所有执行合并的代码都使用相同的方法.merge() 。
# 唯一使结果不同的是左和/或右数据帧是否有重复的键。
# print(person)
# print(survey)

# 由于左右数据帧的键中都有重复的值，所以会发生多对多合并。
ps = person.merge(survey, left_on='ident', right_on='person')
print(ps)

# print(visited)

vs = visited.merge(survey, left_on='ident', right_on='taken')
print(vs)

print(ps['quant'].value_counts())

# 通过 list 来 merge。
ps_vs = ps.merge(
    vs,
    left_on=['quant'],
    right_on=['quant']
)

# 如果列名有冲突，Pandas 会自动为列名添加后缀。
# 在输出中，_x指的是左侧数据帧中的值，_y后缀来自右侧数据帧中。
print(ps_vs.loc[0, :])

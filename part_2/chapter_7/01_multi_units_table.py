#! /usr/bin/python3
# -*- coding:utf-8 -*-
"""
pandas - 表中的多个观测单位 (归一化)。

@Time: 2023/6/23
@Author: Lingchen
@Prescription: P264.
"""
import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

billboard = pd.read_csv('../../data/billboard.csv')
print(billboard.head())
print(billboard.columns)

billboard_long = billboard.melt(
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating'
)
print(billboard_long)

# 假设我们根据特定轨迹对数据进行子集划分。
print(billboard_long.loc[billboard_long.track == 'Loser'])
# print(billboard_long.loc[billboard_long['track'] == 'Loser'])

# 这个表格实际上包含两类数据：赛道信息和每周排名。

# 可以将年份、艺术家、曲目和时间放在一个新的数据帧中，每个唯一的值集都被分配一个唯一的ID。
# 然后，可以在第二个数据帧中使用这个唯一的ID，该数据帧表示输入的日期、歌曲、日期、周数和排名。
billboard_songs = billboard_long[
    ['year', 'artist', 'track', 'time']
]
print(billboard_songs.shape)

# 这个数据帧中有重复的条目，所以需要删除重复的行。
billboard_songs = billboard_songs.drop_duplicates()
print(billboard_songs.shape)

# 然后，可以为每一行数据分配一个唯一的值。
# 有很多方法可以做到这一点，我们取索引值并加1，这样它就不会以0开头。
billboard_songs['id'] = billboard_songs.index + 1
print(billboard_songs)

# 现在有了一个关于歌曲的单独数据框架，我们可以使用新创建的 id 列将歌曲与其每周排名相匹配。
billboard_ratings = billboard_long.merge(
    billboard_songs, on=['year', 'artist', 'track', 'time']
)

print(billboard_ratings)
print(billboard_ratings.columns)

# 在评级数据框架中将列子集设置为想要的列。
billboard_ratings = billboard_ratings[
    ['id', 'date.entered', 'week', 'rating']
]
print(billboard_ratings)

# 通常，需要将多个规范化的数据集组合成一个整洁的数据集。

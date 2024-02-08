#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2024/2/7 17:41
# @Author : sunwenxiao
# @File : find_midi.py
# @Software: PyCharm
import os
import json

font = ''
start_time_by_font = ''
end_time_by_font = ''
wrong_line = []
midi_path = '/Users/sunwenxiao/Desktop/lyric.json'
with open(file=midi_path, mode='r', encoding='utf-8') as f:
    lyric_json = json.loads(f.read())
    song_name = lyric_json.get('meta').get('title')
    print(f'歌词名称为:{song_name}')
    for i in lyric_json.get('lines'):
        # 每行的歌词部分，包括歌词和每个字的起止时间
        lyric_by_line = i.get('words')

        # 通过每个字起始时间是否一样判断
        # print(f'每行歌词部分是：{lyric_by_line}')
        # err_song_font_line = ''
        # for j in lyric_by_line:
        #     font = j['text']
        #     start_time_by_font = j['start_time']
        #     end_time_by_font = j['end_time']
        #     if start_time_by_font == end_time_by_font:
        #         print(f'这句歌词错误，start_time和end_time一致了，歌词是{font}')
        #         err_song_font_line += font
        # if err_song_font_line != '':
        #     wrong_line.append(err_song_font_line)
        # print(wrong_line)

        # 通过将所有字的起止时间去重判断是否只有2个来判断
        err_song_font_line = ''
        start_time_list = []
        end_time_list = []
        for j in lyric_by_line:
            font = j['text']
            start_time_by_font = j['start_time']
            end_time_by_font = j['end_time']
            err_song_font_line += font.replace("\u200b", "")
            start_time_list.append(start_time_by_font)
            end_time_list.append(end_time_by_font)
        if len(set(start_time_list)) != len(start_time_list) and len(set(end_time_list)) != len(end_time_list):
            wrong_line.append(err_song_font_line)
        print(wrong_line)

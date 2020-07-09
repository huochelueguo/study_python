# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:02_pytojson.py
@Time:NAME.py@Time:2020/7/9 上午8:48
"""
# json.dumps()--dumps函数将python数据转换为json格式数据
# 相关参数：
# --skipkey：默认为False，当dict对象里的数据不是Python的基本数据类型；（str,unicode,int,long,float,bool,None）时，当skipkey为False，就会报错，如果skipkey为True，则可以跳过这类key；
# --indent：如果填0或者不填，则按照一行进行打印，否则按照indent的数值显示前面的空格（正整数形式）；
# --separators：分隔符，默认为“(‘,’,’:’)”，它表示key之间用“,”隔开，key和value之间用“:”隔开；
# --encoding：编码格式，默认值是UTF-8；
# -sort_keys：对key、value进行排序，默认值是False，即不排序；
# --ensure_ascii：默认为True，如果dict对象里含有none-ASCII的字符，则显示\uXX的格式，如果为False，则能正常显示出来（解决中文乱码问题）；

import json

dict1 = {'name': 'xiaoming', 'age': 20, 'height': 180, 'sport': 'bike'}
json_data = json.dumps(dict1, indent=4, ensure_ascii=False)
print(json_data)

# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_ini.py
@Time:NAME.py@Time:2020/7/17 上午9:31
"""
# pytest.ini 是 pytest的主配置文件，可以改变pytest的默认行为,指定pytest的运行方式（在cmd输入pytest后，会读取pytest.ini中的配置信息，按指定的方式去运行）
# 使用pytest --help可以查看pytest.ini的设置选项
# 文件存放位置：
# --- 一般一个工程下方一个pytest.ini文件
# --- 不要修改文件名
# addopts:更改默认命令行选项，输入配置后，每次执行pytest会读取该配置
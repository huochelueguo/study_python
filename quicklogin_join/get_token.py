# 通过注册快速登录帐号获取uid和对应token
import requests
import json
import random


def quick_login():

        # 创建快速登录帐号地址
        Quick_Create_Url = 'http://test.api.pokekara.com/api/user/login/?unique_device_id=test15755309420784'
        # 请求头
        header = {'Content-Type': 'application/json'}
        # name使用姓名+随机数，方便查看
        # ran = str(random.randint(0, 100))
        # name = 'sztest' + ran
        # 请求体
        body = {'platform': '7',
                'token': 'register',
                'id_token': '{"name":"sztest","gender":1}'}
        # 发送请求
        response = requests.post(Quick_Create_Url, data=body)
        # 使用uid_dict承接返回值，返回值为dict
        uid_dict = response.json()
        # 获取key值为data的字典值
        uid_data = uid_dict['data']
        # 从data中再摘取user值
        uid_user = uid_data['user']
        # print(uid_user)
        # 从data中再摘取uid
        uid = uid_user['uid']
        user_name = uid_user['screen_name']
        # 使用token承接返回token串
        token = response.cookies
        # 筛选出token值
        token2 = token['poke_session_id']
        # 输出uid
        # print(f'用户账户名为{user_name},uid为：{uid},token为：{token2}')
        return uid, user_name, token2




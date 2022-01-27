# 创建快速登陆用户，获取用户uid和token
import time

import requests
import jsonpath


def create_user(num):
    """
        批量正常快速登陆账号
    :param num: 需要生成的账号数量
    :return: 返回账号uid以及token,按照list返回
    """
    uid_list = []
    token_list = []
    for i in range(num):
        url = 'http://test.api.pokekara.com/api/user/login/?unique_device_id=test15755309420784'
        body = {'platform': '7',
                'token': 'register',
                'id_token': '{"name":"sztest","gender":1}'
                }
        response = (requests.post(url, data=body)).json()
        time.sleep(0.3)
        user_uid = jsonpath.jsonpath(response, '$..uid')[0]
        user_token = jsonpath.jsonpath(response, '$..poke_session_id')[0]
        uid_list.append(user_uid)
        token_list.append(user_token)
    return uid_list, token_list


if __name__ == '__main__':
    res = create_user(5)
    uid = res[0]
    token = res[1]
    print(uid)
    print(token)

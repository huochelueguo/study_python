# 创建快速登陆用户，获取用户uid和token
import time

import requests
import jsonpath


def create_user():
    url = 'http://test.api.pokekara.com/api/user/login/?unique_device_id=test15755309420784'
    body = {'platform': '7',
            'token': 'register',
            'id_token': '{"name":"sztest","gender":1}'
            }
    response = (requests.post(url, data=body)).json()
    user_uid = jsonpath.jsonpath(response, '$..uid')[0]
    user_token = jsonpath.jsonpath(response, '$..poke_session_id')[0]
    return user_uid, user_token


if __name__ == '__main__':
    uid_list = []
    token_list = []
    for i in range(60):
        ss = create_user()
        time.sleep(2)
        uid_list.append(ss[0])
        token_list.append(ss[1])
        print(i)
        i+=1
    print(uid_list)
    print(token_list)
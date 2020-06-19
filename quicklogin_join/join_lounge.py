# 使用get_uid文件中获取到的uid/token/client_id，走加入房间接口
import requests
import json


def JoinLonunge(client_id, room_id, dict_token_new):
    join_url = 'http://test.api.pokekara.com/x/lounge/join?'
    # 请求头
    header = {'Content-Type': 'application/json',
              'cookie': dict_token_new,
              }
    # 请求体
    body = {"client_id": client_id,
            "room_id": room_id,
            }
    # 参数要转为json
    json_body = json.dumps(body)
    respone = requests.post(url=join_url, headers=header, data=json_body)
    print(respone.text)




# 赠送礼物接口
import json
import random
import threading
import time
import uuid
import requests
from Get_Clientid import Get_Clientid
from Lounge.Join_Lounge import Join_Lounge, ROOM_ID, CLIENTID_PATH, ROOM_NID
from User_Add_Clientid import Add_Clientid


class SendCoinGift:

    def __init__(self):
        self.coin_url = 'http://test.api.pokekara.com/x/wallet/gift/send'

    def send_to_mv(self):
        pass

    def send_to_lounge_random(self, room_id, token, room_nid, to_uid, from_uid, client_id):
        """
            歌房内，随机赠送金币礼物
        :param room_id: 歌房ID
        :param token: 用户TOKEN
        :param room_nid: 歌房整形ID
        :param to_uid: 收礼用户ID
        :return: 返回response
        """
        #  接口部分
        cookie = 'poke_session_id=' + token
        header = {'Cookie': cookie, 'Content-Type': 'application/json'}
        gift_list = [5001, 5002, 5004]
        gift_id = random.choice(gift_list)
        payload = {
            "action_type": 0,
            "amount": 1,
            "group_id": "8c716348-028c-4e69-985f-eb071b71d43c",
            "lounge_type": 0,
            "mic_id": 1486316747673325569,
            "part_count": 0,
            "refer": "lounge",
            "t_uid": to_uid,
            "target_id": room_id,
            "target_nid": room_nid,
            "gift_id": gift_id
        }
        res = requests.post(self.coin_url, data=json.dumps(payload), headers=header)

        # ws部分
        data = {
            "extra_data": {
                "client_timestamp": int(round(time.time() * 1000))
            },
            "msg_id": str(uuid.uuid4()),
            "data": {
                "room_id": room_id,
                "from_uid": from_uid,
                "to_uid": to_uid,
                "gift_id": gift_id,
                "client_id": client_id,
                "count": 1,
                "group_id": "8c716348-028c-4e69-985f-eb071b71d43c",

            },
            "command": 4004
        }
        ws = Get_Clientid(token=token, uid=from_uid)
        ws.send_message(data=data)
        return res.json()

    def send_to_lounge_random_thred(self, thred_count, send_data):
        """
            多线程并发送礼
        :param thred_count: 线程数
        :param send_data:   送礼接口数据
        :return:
        """
        thred_list = []
        for i in range(thred_count):
            thred_list.append(threading.Thread(target=self.send_to_lounge_random, kwargs=send_data))
        for j in thred_list:
            time.sleep(1)
            j.start()


if __name__ == '__main__':
    user_path = 'user_10'
    clientid_path = CLIENTID_PATH
    room_id = ROOM_ID
    room_nid = ROOM_NID
    uid_token_clientid = ''
    a = 0
    while a < 200:
        a += 1
        if a == 1:
            Join_Lounge().join(data_file=user_path, room_id=room_id)
            uid_token_clientid = Add_Clientid(user_path=user_path, clientid_path=clientid_path).uid_token_clientid()
            print(uid_token_clientid)
        else:
            # 从下面列表随机选择收礼用户UID
            uid_list = ['u1631851507772944570', 'u1631851508262603387', 'u1631851508743789077', 'u1631851509220699117',
                        'u1631851510712099790', 'u1631851511202067772', 'u1631851511702191247', 'u1631851512183538782',
                        'u1631851512683747505', 'u1631851513172051612']
            for i in range(20):
                send_gift_user_info = random.choice(uid_token_clientid)
                token = send_gift_user_info[1]
                from_uid = send_gift_user_info[0]
                client_id = send_gift_user_info[2]
                to_uid = random.choice(uid_list)
                data = {'room_nid': room_nid, 'room_id': room_id, 'token': token, 'to_uid': to_uid,
                        "from_uid": from_uid,
                        "client_id": client_id}
                SendCoinGift().send_to_lounge_random_thred(thred_count=1, send_data=data)

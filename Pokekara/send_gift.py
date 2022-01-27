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
            "extra_data":{
              "client_timestamp": int(round(time.time() * 1000))
            },
            "msg_id": str(uuid.uuid4()),
            "data": {
                "room_id": room_id,
                "from_id": from_uid,
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
    user_path = 'user_1'
    clientid_path = CLIENTID_PATH
    room_id = ROOM_ID
    room_nid = ROOM_NID
    uid_token_clientid = ''
    a = 0
    while a < 2:
        a += 1
        if a == 1:
            Join_Lounge().join(data_file=user_path, room_id=room_id)
            uid_token_clientid = Add_Clientid(user_path=user_path, clientid_path=clientid_path).uid_token_clientid()
        else:
            # token_list = ['MTYzMTg1MTUwN3xtQ19YRE92eUVkMExnZldoT25uSXQ0aVZaYXB0bjNmc2d0UGdKLWh2RG9yTk1oZE9JcUtlT01yTlB2X1RVOXhpOV9yek9Gdi1Uc3BGYzlVMVQzS2dPdkFHRlBTSHVEeXF8rl6wiQ4pNO8cIjUDQBbBJBVYQgjqkR1TvM9sfKGwTTI=', 'MTYzMTg1MTUwOHwwNTZuVlU1cXo0RUxxV0FhT1Zpbk15VE5fejhVdTdLVDdUZnF2YzI3RjNhRDVBNUFhUnQ4Q2FULVZRdGpsTDRsWDJoLWFhSjdiY3VDdEw2WlF1SXp4SzB1aTczVmJudll8RCNyYYHsK9WMdmNHEG61IBZY0zn6841tS8RjDc4zdBM=', 'MTYzMTg1MTUwOHxXRjZwT2FQbDJfcE01VGlrR2VjVV9ROVZiWFNMWkxKMmdyVlNHaHJOZ3k3U0ZXa1llcnNzNnNUYkMzU2tGQkJ4U2MtS29rNG1OdS1vb2JqdGtTTnNrTUN4VTBlcUNNaU58enDqqfixK0XUqx1FPH1B_jGoH-AWm_mcgGNstXoHh2M=', 'MTYzMTg1MTUwOXxDQjlsNTRvbWtsNi1zSUF6TDFRcEl3cERzZHl5YWVDRGVObVFrZzdHU0RxN0djN1BlSTV3ZnlDMDJfMEoxVlMtMnpaNzhrZC01SG1IVDNWM3hEaGRTOU5OZ2tFZjNZdmZ8GESvOuQeQOZwXk5txjBv3ie865-R3wYv72IdH_BTTpU=', 'MTYzMTg1MTUxMHxhM0M1ZElKWWhhbXlyc1V4NmJZUmh4YkNBUHJ2NktCSGE0cllvQnFVN05vTnd2Z29LRXRoMGY4TXE5MkpfcEp1a2FSZ3k1em9KRTFJUlV0NF9pV0JTaEtRUWk0Zi1kR0t8nlmFQ8z3xTGhl0EBh6lLpRaxWCkltKTkMuDVYf9QVEU=', 'MTYzMTg1MTUxMXxaZ0ladG56bXMxb20zUGd3QUJfSEE4V3YwS2J4QU1pQnhlQjBFVWR3Y0VjZGIwRDBtVTVpUnBSd0NlWGVhQUdJVktkR25TN0RTdjJaNU0zcElSQ3RPR1ZZTXFBTmxVUnJ8bScVnl1ZoRAZ7VbrfihVX_V3-8xrTydvXP_WehkACEk=', 'MTYzMTg1MTUxMXxSbElFSjBOQVZWYlhpVDdlbTc3YU96VUFSUjRTWUlSalRuMzNtcFZNOEQyaHB0azdLemdKRlBQTFJyNl9sTUM1blNQbEhSbE9lT093V0VhWF9IYllrZGFsVUVIOUNWNGF8Iaaq3hCi5kUb0RcMtRGgTyoAAIwc1rSuVTmf8xd664Y=', 'MTYzMTg1MTUxMnxqQU41OExZQUhZUjFTRU91MkxGM216X1d5TFFQSmo4bjM5T3ZmdkZEMmpTNS1IRC00a3ctdDAwZEpYN0lGS05yQ2dTU1AwMTVPQjk5YnZZMEtNS0tLOW5fRXBpbmZRZWh8pN_C779rf5_HYgYldA2AZE8fFVZ1Ssqz-cwLV1pebNk=', 'MTYzMTg1MTUxMnxEWkoyMHJWT3EyZUtmSUNJVXNrT1pIRG8xd2hsRjdkYnFTemQxdGdCRnAtbGtFSkVoWklkTjNjVDVWY0E5c0ZWa1lwZHp6MGxJak1tUmE3dDg2bTUwTVA4c1p3NWVPVGN8Ty-Jb6cLsJY1YTMUFfx1udde2AhVmoMfV1VqeMo0b3w=', 'MTYzMTg1MTUxM3xLVEFkazJjWC01VkFMWGhONHViWTV1QVBzdE43XzhZMkZPbU9jZjd0dGRwYlJaTjJwVGNrMkptQzBRX1NoT09fSHFZODJlY3JwdkVTMkxsSUFqRTQ4U3J2a2V3LXJ6dWh8FQryn5j59QdCQG4ZGI2PLz308kZJk1O0ilSqS8bIZ1I=']
            uid_list = ['u1631851507772944570', 'u1631851508262603387', 'u1631851508743789077', 'u1631851509220699117', 'u1631851510712099790', 'u1631851511202067772', 'u1631851511702191247', 'u1631851512183538782', 'u1631851512683747505', 'u1631851513172051612']
            for i in range(20):
                send_gift_user_info = random.choice(uid_token_clientid)
                token = send_gift_user_info[1]
                from_uid = send_gift_user_info[0]
                clent_id = send_gift_user_info[2]
                to_uid = random.choice(uid_list)
                data = {'room_nid': room_nid, 'room_id': room_id, 'token': token, 'to_uid': to_uid, "from_uid": from_uid,
                    "client_id":clent_id}
                SendCoinGift().send_to_lounge_random_thred(thred_count=1, send_data=data)
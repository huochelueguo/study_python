import join_lounge
import get_client_id
from user_data import user_50
from user_data import user_20
from user_data import user_18

# uid列表，用来去获取client_id,通过导入DATA包读取
uid_list = user_50.uid_list
token_list = user_50.token_list

# 获取client_id，由于为实时获取，因此不需要传入列表中，获取到直接发送给join_lounge
clientid_list = []
a = 0
while a < len(uid_list):
    # 获取获取client_id
    list = get_client_id.get_clientid(uid_list[a])
    # 返回值为列表，取值
    clientid = list[0]
    clientid_list.insert(a, clientid)
    room_id = "cc8614a7-bc45-11ea-98fb-5254009bf4c3"
    token_list_new = 'poke_session_id=' + token_list[a]
    join_lounge.JoinLonunge(clientid, room_id, token_list_new)
    a += 1
print(clientid_list)









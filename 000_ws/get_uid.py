# 导入自己的包，可能报错，忽略即可
import get_client_id
import get_token
import join_lounge

# while循环判断需要循环次数，循环次数 = 加入房间人数
a = 0
while a < 2:
    # 使用快速登录创建用户
    get_token.quick_login()
    a += 1
    dict1 = get_token.quick_login()
    # print(dict1)
    # print(type(dict))
    # 使用切片获取返回结果中的uid
    dict_uid = dict1[0::4]
    # 使用切片获取返回结果中的token
    dict_token = dict1[2::4]
    dict_token_new = 'poke_session_id=' + dict_token[0]
    # print(f'创建的新用户信息为：{dict1}')
    print(f'用户对应的uid为：{dict_uid}')
    print(f'用户对应的token为：{dict_token_new}')

    # 获取各UID的client_id
    list2 = dict_uid
    # list2 = ['u1237326482846568448']
    # 其他文件中调用，需要文件名.方法
    client_id_list = get_client_id.get_clientid(list2)
    client_id = client_id_list[0]
    # print(type(client_id))
    print(f'用户对应的歌房client_id为：{client_id}')


    # 设置一个歌房room_id，根据token+client_id+room_id即可加入房间
    room_id = 'bc000870-b205-11ea-a0b3-5254009bf4c3'
    join_lounge.JoinLonunge(client_id, room_id, dict_token_new)

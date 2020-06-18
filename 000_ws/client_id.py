from websocket import create_connection
import json
# 获取client_id函数


def get_clientid(list_uid):
    # ws地址
    url1 = "ws://test.api.pokekara.com/ws?"
    # 列表循环，将ws地址和uid拼接，链接ws，获取返回值中的client_id
    for uid in list_uid:
        url2 = url1 + 'uid=' + uid
        # print(f'拼接后地址为{url2}')
        ws = create_connection(url2, timeout=5)
        if ws.connected:
            ws.send('')
            # 获取返回值
            dict1 = ws.recv()
            # 将返回值转换为json
            json_ws = json.loads(dict1)
            # print(type(json_ws))
            # 返回值中截取client_id的key和value
            client_id = json_ws['data']
            # 只输出返回值中的value
            id_str = client_id['client_id']
            # print(id_str)
        else:
            print('error,ws链接失败')
    # 将每次请求结果中的client_id整理到一个列表中
    client_id_list = []
    i = 0
    while i < len(list_uid):
        client_id_list.insert(i, id_str)
        i += 1
    return client_id_list




from websocket import create_connection
import json
# 获取client_id函数


url1 = "ws://test.api.pokekara.com/ws?"
# 列表循环，将ws地址和uid拼接，链接ws，获取返回值中的client_id

url2 = url1 + 'uid=' + 'u1592560688671743535'
# print(f'拼接后地址为{url2}')
ws = create_connection(url2, timeout=15)
if ws.connected:
    dict = {"command": 4001,
            "data": {"uid": "u1592560688671743535", "room_id": "12d8c8da-b23c-11ea-9bcc-5254009bf4c3",
            "client_id": "23af7c39-b23c-11ea-8adb-5254009bf4c3"}}
    json = json.dumps(dict)
    ws.send(dict)
    # 获取返回值
    dict1 = ws.recv()

else:
    print('error,ws链接失败')
    # 将每次请求结果中的client_id整理到一个列表中
    # client_id_list = []
    # client_id_list.insert(0, id_str)










from websocket import create_connection
import json
# 获取client_id函数

class WebSocket:
    def get_clientid(self, list_uid):
        # ws地址
        url1 = "ws://test.api.pokekara.com/ws?"
        # 列表循环，将ws地址和uid拼接，链接ws，获取返回值中的client_id

        url2 = url1 + 'uid=' + list_uid
        # print(f'拼接后地址为{url2}')
        ws = create_connection (url2, timeout=15)
        if ws.connected:
            ws.send ('')

            # 下面为输出聊天内容4003，问题是room_id和uid怎么传入
            # ws.send(
            #     '{"command": 4003, "data": '
            #     '{"room_id": "5748d744-b47e-11ea-9bcc-5254009bf4c3", "uid": "u1592560688671743535", '
            #     '"type": 1, "content": "234"},'
            #     '"msg_id": "059c44be-9d86-4bb7-8948-9fe13399bacb"}')
            # 获取返回值
            dict1 = ws.recv ()
            # 将返回值转换为json
            json_ws = json.loads (dict1)
            # print(type(json_ws))
            # 返回值中截取client_id的key和value
            client_id = json_ws[ 'data' ]
            # 只输出返回值中的value
            id_str = client_id[ 'client_id' ]
            # print(id_str)
        else:
            print ('error,ws链接失败')
        # 将每次请求结果中的client_id整理到一个列表中
        client_id_list = [ ]
        client_id_list.insert (0, id_str)
        return client_id_list

class Chat(WebSocket):
    pass



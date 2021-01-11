# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:User_Add_Clientid.py
@Time:NAME.py@Time:2021/1/9 18:45
@ 将用户的uid/token/clientid组合成一组数据，用户多线程发送消息
"""
from Lounge.Read_Usertoken import Read_Uid_Token


class Add_Clientid(object):

    def __init__(self, user_path, clientid_path):
        self.user_path = user_path
        self.user_clientid_path = clientid_path

    def get_clientid_list(self):
        """

        :return:将用户clientid返回，类型为list
        """
        with open(self.user_clientid_path, 'r', encoding='utf-8') as f:
            clientid_data = f.readlines()
            clientid = []
            for i in clientid_data:
                clientid.append(i[2:-1])
            # print(clientid)
            return clientid

    def get_uid_token_list(self):
        """

        :return: 分别将用户uid.token返回，类型为list
        """
        uid_token_data = Read_Uid_Token(path=self.user_path).read()
        uid_list = uid_token_data[0]
        token_list = uid_token_data[1]
        # print(uid_list, token_list)
        return uid_list, token_list

    def uid_token_clientid(self):
        """

        :return: 将uid token clientid组合成一条数据，整体作为列表返回
        """
        clientid_list = self.get_clientid_list()
        uid_list = self.get_uid_token_list()[0]
        token_list = self.get_uid_token_list()[1]
        uid_token_clientid_list = list(zip(uid_list, token_list, clientid_list))
        # print(uid_token_clientid_list[0])
        return uid_token_clientid_list





if __name__ == '__main__':
    user_path = 'user_18'
    # clientid_path = 'E:/python-workspace/Lounge/user_data/clientid'
    clientid_path = '/Users/sunwenxiao/PycharmProjects/study_python/Lounge/user_data/clientid'
    Add_Clientid(user_path, clientid_path).uid_token_clientid()


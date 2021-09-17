# 导入自己的包，可能报错，忽略即可

from joinlounge import get_token

a = 0
uid_list = []
token_list = []
while a < 10:
    get_token.quick_login()
    dict1 = get_token.quick_login()
    a += 1
    uid = dict1[0]
    uid_list.insert(a, uid)
    token = dict1[2]
    token_list.insert(a, token)

print(uid_list)
print(token_list)



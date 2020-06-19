# 导入自己的包，可能报错，忽略即可
import get_client_id
import get_token

a = 0
uid_list = []
token_list = []
while a < 2:
    get_token.quick_login()
    dict1 = get_token.quick_login()
    a += 1
    uid = dict1[0]
    uid_list.insert(a, uid)
    token = dict1[2]
    token_list.insert(a, token)

print(uid_list)
print(token_list)

b = 0
clientid_list = []
while b < len(uid_list):
    list = get_client_id.get_clientid(uid_list[b])
    # print(list)
    # clientid_list.insert(b, str(list))
    b += 1
print(list)

# list = get_client_id.get_clientid(uid_list)
# print(list)

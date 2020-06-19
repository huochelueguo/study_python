# 导入自己的包，可能报错，忽略即可
import get_client_id
import get_token
import json

uid_list = [ 'u1592560688671743535', 'u1592560689318259154', 'u1592560689997511820', 'u1592560690629720849'
             ]
a = 0
list2 = []
while a < len(uid_list):
    list = get_client_id.get_clientid(uid_list[a])
    clientid = list[0]
    list2.insert(a, clientid)
    # print(list2)
    a += 1
print(list2)


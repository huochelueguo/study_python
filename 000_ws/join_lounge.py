# 导入自己的包，可能报错，忽略即可
import client_id

# 获取各UID的client_id
list2 = ['u1237326482846568448', 'u1218064453223043072', 'u1585628598650592149', 'u1592478885382154380']
# 其他文件中调用，需要文件名.方法
print(client_id.get_clientid(list2))


# 获取各uid的token



# 设置一个歌房room_id，根据token+client_id+room_id即可加入房间
# 按行读取文件，使用readline(),每次仅读取一行
# readline()有一个参数，参数size表示从文件读取的字节数。
# 读取时，会将换行符'\n'也读取出来
# 需要遍历每一行文件时，使用该方法遍历
file = open('readme')
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
print('*' * 20)
txt = file.readline(2000)
print(txt)
file.close()


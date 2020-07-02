# 按行读取文件，使用readline(),每次仅读取一行
file = open('readme')
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
txt = file.readline()
print(txt)
file.close()


# 用with内置函数，它可以将文件自动关闭，格式如下：
# with open（“”，“”）as f:

with open('readme') as f:
    txt = f.readlines()
    print(txt)

with open('write', 'a') as f:
    f.write('使用with方法插入')


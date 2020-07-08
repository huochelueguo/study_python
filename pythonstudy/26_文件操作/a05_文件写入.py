# 写入方法：
# 1.打开文件时使用参数w：覆盖之前内容写入
# 2.打开文件时使用参数a:从文件末尾处写入：append

f = open('write', 'w')
f.write('123' + '\n'
        '234' + '\n')
f.close()

f = open('write', 'a')
f.write('345' + '\n'
        '456' + '\n')
f.close()

f = open('write')
txt = f.readlines()
print(txt)
f.close()

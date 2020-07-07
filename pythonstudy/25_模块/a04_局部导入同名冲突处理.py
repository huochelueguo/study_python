# 当局部导入的模块存在同名的情况时，可以对局部导入的内容起别名

from a_被导入模块01 import hanshu as hanshu01
from a_被导入模块02 import hanshu as hanshu02

# 使用导入内容时，使用别名即可避免同名问题
hs1 = hanshu01()
print(hs1)
hs2 = hanshu02()
print(hs2)

# from ..import 导入
# 如果希望从一个模块中，导入部分工具，就可以使用from ..import 导入
# 局部导入的好处；
# --使用不需要通过模块名.
# --可以直接使用模块提供的工具--全部变量、函数、类
# 局部导入注意问题：
# --如果两个模块，存在同名函数，那后导入的函数会覆盖先导入的函数


from a_被导入模块01 import hanshu
from a_被导入模块02 import lei02
# 导入同名的全局变量，输出的内容为后导入模块中的
from a_被导入模块01 import title
from a_被导入模块02 import title
print(hanshu())
lei = lei02()
print(lei)
print(title)
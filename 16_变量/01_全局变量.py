# 定义位置：函数体外部，定义在函数上方，确保函数能正常访问每一个全局变量
# 作用域：整个程序内
# 值的修改：函数中不能对全局变量进行修改，函数中修改实质是新建了一个名称一致的变量

a = 50
# a 为全局变量
# 函数体上下要有2个空行


def sum1():
    # 函数中可以直接使用全局变量a
    b = a * 10
    return b


print(sum1())

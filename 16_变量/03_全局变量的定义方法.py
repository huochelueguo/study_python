# 全局变量的标识：使用global关键字【建议全局变量使用gl_开头来定义】
# global关键字的作用：声明变量var是全局的，可以在函数内部对全局变量进行修改
gl_a = 50


def sum1(m, n):
    global gl_a
    gl_a = m
    return gl_a + n


print(f'使用global关键字后，可以在函数内部修改全局变量，将a的值修改为100，求和后={sum1(100,100)}')
print(f'修改后的全局变量a的值：{gl_a}')

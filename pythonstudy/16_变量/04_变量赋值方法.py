# 将a b 数字值对换
# 1.使用第三方字段，中介

print('1.使用三方字段承接法')
a = 10
b = 20
print(f'对换前a的值为{a},b的值为{b}')
c = a
a = b
b = c
print(f'对换后a的值为{a},b的值为{b}')


# 2.不使用第三方字段方法
print('2.不使用三方字段方法')
a = 10
b = 20
print(f'对换前a的值为{a},b的值为{b}')
a = a + b
b = a - b
a = a - b
print(f'对换后a的值为{a},b的值为{b}')

# 3.python特有方法
print('python特有方法')
a = 10
b = 20
a, b = b, a
print(f'对换后a的值为{a},b的值为{b}')

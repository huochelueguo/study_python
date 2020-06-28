# 捕获位置错误
# --在开发中，要预判到有可能出现的所有错误，还是有一定得难度的
# --如果希望程勋无论出现何种错误，都不会因为抛出异常而被终止，可以再增加一个except
# --语法如下：
#   except Exception as result:
#     print(f'未知错误{result}')

# 例子：提示用户输入一个整数，使用8除用户输入的整数并且输出值
try:
    num = int(input('请输入一个整数：'))
    num2 = 8 / num
    print(num2)
except ValueError:
    print('请输入整数，目前输入错误')
# except ZeroDivisionError:
#     print('除数不能为0')
# 捕获位置错误，一般情况下习惯使用result作为结论输出
except Exception as result:
    print(f'出现未知错误:{result}')

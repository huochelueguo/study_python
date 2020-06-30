# 当 函数/方法 执行中出现异常，会将异常 传递给函数/方法的调用一方
# 如果传递到主程序，仍然没有处理异常，程序才会被终止
# 提示：
# --在开发中，可以再主函数中增加异常捕获
# --而在主函数中调用其他函数，主要出现异常，都会传递到主函数中捕获异常
# --好处：就不用再代码中，增加大量的异常捕获，保证代码的整洁


def inputnum():
        num = int(input(f'请输入一个整数： '))
        num2 = 8 / num
        print(f'输入的数字被8除后，结果为：{num2}')
        return


try:
    inputnum()
except ValueError:
    print('输入错误，请检查')
    # inputnum()
except ZeroDivisionError:
    print('除数不能为0，请检查输入内容')
except Exception as result:
    print(f'遇到未知错误:{result}')


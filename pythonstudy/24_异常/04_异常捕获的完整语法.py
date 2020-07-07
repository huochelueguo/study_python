# 完整的异常语法如下：
# try:
#     # 可能出现异常的语法
#     pass
# except 异常1：
#     处理异常的语句
# except 异常2：
#     处理异常的语句
# except Exception as result:
#     处理未知异常的语句
# else:
#     没有异常时才会执行的代码
# finally：
#     无论是否有异常，都会执行的代码
# 注意：
# --else: 只有在没有异常时才会执行的代码
# --finally: 无论是否有异常都会去执行的代码
# --except Exception as result： 承接未知错误使用


def inputnum():
    try:
        num = int(input(f'请输入一个整数： '))
        num2 = 8 / num

    except ValueError:
        print('请输入整数，目前输入错误, 请重新输入：')
        inputnum()
    except ZeroDivisionError:
        print('除数不能为0，请重新输入')
        inputnum()
    except Exception as result:
        print(f'遇到未知错误:{result}')
    # 只有没报异常，才会执行的内容
    else:
        print(f'输入的整数被8除后值为：{num2}')
    # 不论是否有异常都会执行的内容
    finally:
        print(f'不论是否有异常都会输出这句话')


inputnum()

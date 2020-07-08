# 概念：
# 概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能,其实装饰器就是一个闭包，装饰器是闭包的一种应用
# 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
#
# 使用方法：再需要的函数前加上@demo即可
# 模版：
#     def    装饰器名(func):                    #def 与 @之后的函数名称一致   调用函数func与ret=func(*args,**kwargs)内部函数一致
#         def wrapper(*args,**kwargs):         #def 与 return 之后的函数名称一致
#             ret = func(*args,**kwargs)
#             return ret                       #return ret 与 ret=func(*args,**kwargs)一致
#         return wrapper
#
#     @装饰器名
#     def foo():
#         pass
#
# https://zhuanlan.zhihu.com/p/87353829
# https://www.cnblogs.com/yuzhanhong/p/9180212.html

# 参数和返回值都是一个函数
# 需要将函数本身传入装饰器中，一般使用func代替函数本体名


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        func()
        # return func()
    # 返回内容和函数名一致
    return wrapper


@debug
def hello():
    print('hello')


if __name__ == '__main__':
    hello()


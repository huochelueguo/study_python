# 模块使用__name__方法，将不需要被其他模块导入得内容，放置在main方法中
# 在函数本身文件中，__name__恒等于__main__
# 在被导入其他文件中时，__name__等于被导入文件名
# 因此可以使用__name__，将不希望被其他模块使用得内容，放在main函数中


class Dog(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'狗狗的名字是：{self.name}'


# 将不需要外部模块使用的代码，写到main函数中
def main():
    wangcai = Dog('旺财')
    print(wangcai)
    # 因为在文件本体汇总，因此下句输出内容为__main__
    print(__name__)


# 在文件中，使用如下判断,如果在本体中，则会执行main()，如果不是，则不执行
if __name__ == '__main__':
    main()






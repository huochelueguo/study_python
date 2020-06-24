#     摆放家具
# 1.房子有户型、总面积、家具名称列表
# 2.家具有名字、占地面积，其中
#     席梦思 占地4平米
#     衣柜 占地2平米
#     餐桌 占地1.5平米
# 3.将以上家具添加到房子里面
# 4.打印房子时，传输户型、总面积、剩余面积、家具名称列表


class JiaJu(object):
    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):
        return f'家具的名字是:{self.name}，面积是{self.area}'


class House(object):
    def __init__(self, huxing, area):
        self.huxing =huxing
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表,初始化家具列表为空
        self.item_list = []

    def __str__(self):

        return f'房子户型为{self.huxing},房子面积为{self.area}平米,剩余面积为{self.free_area},' \
               f'家具列表为{self.item_list}'

    def add_jiaju(self, jiaju):

        print(f'要添加{jiaju.name}')
        # 判断家具面积和房子面积大小
        if jiaju.area > self.free_area:
            print('家具面积过大，放不下啦')
            return
        # 将符合大小的家具插入到家具列表中
        self.item_list.append(jiaju.name)
        # 房屋面积减去家具面积
        self.free_area -= jiaju.area


bed = JiaJu('席梦思', 4)
guizi = JiaJu('衣柜', 2)
canzhuo = JiaJu('餐桌', 1.5)
# print(bed)
# print(guizi)
# print(canzhuo)

house = House('三室一厅', 112)
# 使用房子的添加家具方法，传参使用家具类的对象
house.add_jiaju(bed)
house.add_jiaju(guizi)
house.add_jiaju(canzhuo)
print(house)

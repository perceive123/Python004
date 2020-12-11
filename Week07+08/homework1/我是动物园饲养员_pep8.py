# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。
# 这个类可以使用如下形式为动物园增加一只猫：

# if __name__ == '__main__':
#     # 实例化动物园
#     z = Zoo('时间动物园')
#     # 实例化一只猫，属性包括名字、类型、体型、性格
#     cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
#     # 增加一只猫到动物园
#     z.add_animal(cat1)
#     # 动物园是否有猫这种动物
#     have_cat = hasattr(z, 'Cat')

# 具体要求：
# 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

from abc import ABCMeta, abstractmethod


# 动物
class Animal(metaclass=ABCMeta):  # 该类不允许被实例化
    @abstractmethod
    def __init__(self, form, shape, character):
        self.form = form  # 食草/食肉
        self.shape = shape  # 小型/中等/大型
        self.character = character  # 凶猛或温顺
        if self.form == '食肉' and self.shape in ['中', '大'] and self.character == '凶猛':
            self.is_fierce = True  # 是（体型>=中等 食肉类型 性格凶猛）或否
        else:
            self.is_fierce = False


# 猫
class Cat(Animal):
    cry = 'miao'  # 叫声

    def __init__(self, name, form, shape, character):  # 名字，类型，体型，性格
        self.name = name
        super().__init__(form, shape, character)
        if self.is_fierce:
            self.is_pet = False  # 可作宠物（不是凶猛动物）或否
        else:
            self.is_fierce = True


# 狗
class Dog(Animal):
    cry = 'wang'  # 叫声

    def __init__(self, name, form, shape, character):  # 名字，类型，体型，性格
        super().__init__(form, shape, character)
        if self.is_fierce == False:
            self.is_pet = True  # 可作宠物（不是凶猛动物）或否
        else:
            self.is_fierce = False


# 动物园
class Zoo:
    def __init__(self, name):
        self.name = name  # 名字
        self.zoo = {}

    def add_animal(self, isinstance):  # 实现同一只动物（同一个动物实例）不能被重复添加
        params = isinstance.__class__.__name__
        id_instance = id(isinstance)
        # print(id_instance)
        if id_instance not in self.zoo:
            self.zoo[id_instance] = isinstance
            self.__dict__[params] = isinstance
        else:
            print(f'id{id_instance}重复，同一个动物实例不能被重复添加')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字，类型，体型，性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

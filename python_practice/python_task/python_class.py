# 1、定义一个人类的类
class Student:
    # 静态属性
    weight = 50
    height = 158
    gender = "女"

    # g构造方法，类实例化的时候会直接执行,实例化的时候要传入性别参数
    def __init__(self, name, classe):
        # 定义学生的姓名，班级
        self.name = name
        self.classe = classe

    # 动态方法
    def sleep(self):
        print(f"{self.name}在睡觉")

    def learn(self):
        print(f"{self.name}在学习")

    def have_lesson(self):
        print(f"{self.classe}的同学在上体育课")

zhangsan = Student("张三", "五年级三班")
zhangsan.sleep()

# 2、定义一个动物的类
class Animal:
    # 构造方法，传入参数：动物种类
    def __init__(self, name):
        self.name = name

    # 动态方法
    def eat(self):
        print(f"{self.name}在吃")

    def play(self):
        print("它在玩")

pig = Animal("小猪")
pig.eat()

# 3、定义一个电脑的类
class Computer:
    # 静态变量
    type = "笔记本"
    size = "24寸"

    # 动态方法
    def install_software(self):
        print("电脑上可以安装不同的软件")

    def play_computer(self):
        print("可以用电脑玩游戏")

computer = Computer()
computer.install_software()

# 4、定义一个水果的类
class Fruit:
    # 构造方法，实例化类的时候直接执行
    def __init__(self, species, color, weight):
        self.species = species
        self.color = color
        self.weight = weight

    def buy(self):
        print(f"有人买{self.species}了")

    def paint(self):
        print(f"谁种{self.species}树了")

fruit = Fruit("苹果", "红色", 0.2)
fruit.buy()

# 5、定义一个车的类
class Car:
    # 静态变量
    color = "red"
    type = "小轿车"
    # 构造函数，实例化类的时候会直接执行
    def __init__(self, brand):
        self.brand = brand

    def run(self):
        print(f"{self.brand}牌子的车正在路上跑着")

mycar = Car("丰田")
# 直接调用类变量
print(mycar.color)
print(mycar.type)
# 调用类方法
mycar.run()
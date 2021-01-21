class Game():

    def __init__(self, my_hp, enemy_hp):
        # 定义4个实例变量存放数据
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    def fight(self):
        # 加入循环，让游戏可以进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)

            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件就跳出循环
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break

    def rest(self, time_num):
        print(f"太累了，休息{time_num}分钟")


class HouYi(Game):
    """
    后裔，后裔类继承了Game的hp 和 power. 并多了护甲属性 defense
    final_hp = hp + defense - enemy_power
    enemy_final_hp = enemy_hp - power
    两个hp 进行对比，血量先为零的人输掉比赛
    """

    # 定义护甲属性
    def __init__(self, my_hp, enemy_hp):
        self.defense = 100
        # 通过继承调用父类的构造函数，拿到父类的属性
        super().__init__(my_hp, enemy_hp)

    # 改造fight()方法
    def fight(self):
        while True:
            # 修改了 my_hp 的计算方式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)

            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件就跳出循环
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


houyi = HouYi(1000, 1200)
houyi.fight()
houyi.rest(3)
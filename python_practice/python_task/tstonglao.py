class TongLao:

    # 构造方法
    def __init__(self, power):
        self.hp = 1000
        self.power = power


    # see_people方法
    def see_people(self, name):
        if name == "WYZ" or name == "无崖子":
            print("师弟！！")
        elif name == "李秋水":
            print("师弟是我的！！")
        elif name == "丁春秋":
            print("叛徒，我杀了你！！")
        else:
            print("传入的参数不正确！")

    # fight_zms方法
    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp / 2
        self.power = self.power * 10

        # 计算一回合后双方血量
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power

        # 比较双方血量大小。 血多的一方获胜
        if self.hp > enemy_hp:
            print("我赢了")
        elif self.hp < enemy_hp:
            print("我输了")
        else:
            print("平局")



if __name__ =="__main__":
    tonglao = TongLao(120)
    tonglao.see_people("丁春秋")
    tonglao.fight_zms(1200, 250)

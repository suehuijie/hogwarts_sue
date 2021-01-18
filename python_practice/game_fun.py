"""
一个回合制游戏(多轮)
敌人的血量随机
"""

# 复制一行代码： ctrl + d
# 注释： ctrl + /
# 导入包： alt + 回车


# 定义fight函数实现游戏逻辑
import random


def fight(enemy_hp, enemy_power):
    # 定义4个变亮存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print(f"敌人的血量为 {enemy_hp}， 攻击力为 {enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # print(my_hp)

         # 判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为 {my_hp}")
            print(f"敌人的剩余血量为 {enemy_hp}")
            print("我输了")
            # 满足条件就跳出循环
            break
        elif  enemy_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为 {my_hp}")
            print(f"敌人的剩余血量为 {enemy_hp}")
            print("我赢了")
            break


if __name__=="__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # 打印hp
    # print(hp)
    # print(type(hp))
    # 让敌人的hp从hp列表中随机挑选一个值
    # 自动导包： alt+回车
    enemy_hp = random.choice(hp)
    # print(enemy_hp)

    # 敌人的攻击力用 randint方法生成随机整数
    enemy_power = random.randint(190, 210)
    # print(enemy_power)

    # 调用fight()函数，传入敌人的hp 和power
    fight(enemy_hp, enemy_power)
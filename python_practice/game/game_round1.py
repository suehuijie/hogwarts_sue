"""
一个回合制游戏
"""

# 定义fight函数实现游戏逻辑

def fight():
    # 定义4个变亮存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 计算1回合后双方的血量
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断谁的血量剩余多，谁获胜
    if my_final_hp > enemy_final_hp:
        print("我赢了")
    elif  my_final_hp < enemy_final_hp:
        print("我输了")
    else:
        print("平局")

fight()
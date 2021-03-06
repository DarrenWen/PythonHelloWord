'''
    作者:付文军
    功能:模拟掷骰子
    版本:v3.0
    日期:2018年12月10日
    v2.0新增功能: 模拟投掷两个骰子
    v3.0新增功能: 数据可视化
'''
import random
import matplotlib.pyplot as pl

def roll_dice():
    '''
        模拟掷骰子
    '''
    roll = random.randint(1, 6)
    return  roll

def main():
    '''
        主函数
    '''
    total_times = 10000
    # 初始化列表
    result_list = [0]*11
    # 初始化点数列表
    roll_list = list(range(2, 13))

    roll_dict = dict(zip(roll_list, result_list))

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        for j in range(2, 13):
            if roll1+roll2 == j:
                roll_dict[j] += 1

    for i, result in roll_dict.items():
        print('点数{}的次数{},频率{} \n'.format(i, result, result/total_times))
    # 数据可视化
if __name__ == '__main__':
    main()

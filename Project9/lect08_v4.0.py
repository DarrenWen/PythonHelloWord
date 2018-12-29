'''
    作者:付文军
    功能:模拟掷骰子
    版本:v3.0
    日期:2018年12月10日
    v2.0新增功能: 模拟投掷两个骰子
    v3.0新增功能: 数据可视化
    v4.0新增功能: 数据可视化 直方图
'''
import random
import matplotlib.pyplot as plt

# 统计图中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
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
    total_times = 1000
    # 初始化列表
    result_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        result_list.append(roll1+roll2)
    # 数据可视化
    plt.hist(result_list, bins=range(2, 14),density=1, edgecolor='white', linewidth=1)
    plt.title("骰子点数统计")
    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.show()

if __name__ == '__main__':
    main()

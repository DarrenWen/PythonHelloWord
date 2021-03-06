'''
    作者:付文军
    功能:模拟掷骰子
    版本:v1.0
    日期:2018年12月10日
'''
import  random

def roll_dice():
    '''
        模拟掷骰子
    '''
    roll = random.randint(1,6)
    return  roll

def main():
    '''
        主函数
    '''
    total_times = 500
    # 初始化列表
    result_list = [0]*6
    for i in range(total_times):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                result_list[j-1] += 1
    for i,resuult in enumerate(result_list):
        print('点数{}的次数{},频率{} \n'.format(i+1, resuult, resuult/total_times))

if __name__ == '__main__':
    main()
"""
    作者：付文军
    功能：52周存钱挑战
    版本：V2.0
    日期：2018年11月21日
    2.0     记录每周存款数
    3.0     使用for循环直接计数
"""
import  math

def main():
    """
        主函数
    """
    money_perweek = 10  # 每周存入金额
    i = 1               # 记录周数
    incress_mondy = 10  # 递增资金
    total_week = 52     # 总共周数
    saving = 0          # 账户累计
    money_list = []     # 用来记录每周存款数的列表
    for i in range(total_week):
        # 存钱操作
        money_list.append(money_perweek)
        saving = math.fsum(money_list)
        # 输出信息
        print('第{}周，存入{}元，账户累计:{}元'.format(i+1, money_perweek, saving))
        # 更新下一周存钱金额
        money_perweek += incress_mondy

if __name__ == "__main__":
    main()
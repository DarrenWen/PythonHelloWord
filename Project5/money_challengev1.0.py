"""
    作者：付文军
    功能：52周存钱挑战
    版本：V1.0
    日期：2018年11月21日
"""
def main():
    """
        主函数
    """
    a = 'Hi'
    print(a*2)
    money_perweek = 10  # 每周存入金额
    i = 1               # 记录周数
    incress_mondy = 10  # 递增资金
    total_week = 52     # 总共周数
    saving = 0          # 账户累计
    while i <= total_week :
        # 存钱操作
        saving += money_perweek
        # 输出信息
        print('第{}周，存入{}元，账户累计:{}元'.format(i, money_perweek, saving))
        # 更新下一周存钱金额
        money_perweek += incress_mondy
        i += 1
if __name__ == "__main__":
    main()
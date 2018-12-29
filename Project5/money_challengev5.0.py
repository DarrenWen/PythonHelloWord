"""
    作者：付文军
    功能：52周存钱挑战
    版本：V2.0
    日期：2018年11月21日
    2.0     记录每周存款数
    3.0     使用for循环直接计数
    4.0     动态输入计数参数
    5.0     根据用户输入日期，计算是第几周
"""
import  math
import datetime

saving = 0  # 账户累计

def main():
    """
        主函数
    """
    money_perweek = float(input('请输入每周存入的金额：'))  # 每周存入金额

    incress_money = float(input("请输入每周的递增金额："))  # 递增资金
    total_week = int(input('请输入总工周数：'))     # 总共周数
    saved_money_list = Save_MoneyInWeek(money_perweek, incress_money, total_week)

    input_date_str = input('请输入日期(yyyy/mm/dd)：')

    input_date = datetime.datetime.strptime(input_date_str, format("%Y/%m/%d"))
    week_num = input_date.isocalendar()[1]
    print('第{}周，存款{}元'.format(week_num, saved_money_list[week_num-1]))
def Save_MoneyInWeek(money_perweek, incress_money, total_week):
    global  saving
    money_list = []  # 用来记录每周存款数的列表
    saved_money_list = []  # 记录每周账户累计
    for i in range(total_week):
        # 存钱操作
        money_list.append(money_perweek)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        # 输出信息
        # print('第{}周，存入{}元，账户累计:{}元'.format(i + 1, money_perweek, saving))
        # 更新下一周存钱金额
        money_perweek += incress_money
    return saved_money_list
if __name__ == "__main__":
    main()

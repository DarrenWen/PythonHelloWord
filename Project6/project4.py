'''
    作者:付文军
    版本:v4.0
    日期:2018年11月30日
    功能:输入某年某月某日，判断这一天是一年的第几天
    2.0     增加功能:用列表替换元组
    3.0     增加功能:使用集合替换列表
    4.0     增加功能:使用字典替换集合
'''

from datetime import datetime

def is_leap_year(year):
    '''
        判断year是否为闰年
        是:返回True
        否:返回False
    '''
    is_leap = False
    if (year % 400 == 00) or ((year % 4 == 0) and (year % 100 == 0)):
        is_leap = True
    return  is_leap
def main():
    '''
     主函数 
    '''
    input_date_str = input('请输入日期(yyyy/mmm/dd):')
    input_date = datetime.strptime(input_date_str, format('%Y/%m/%d'))
    print(input_date)
    year = input_date.year
    month = input_date.month
    day = input_date.day
    # 初始化值
    days = 0
    month_day_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    # days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1, month):
        days += month_day_dict[i]

    if is_leap_year(year):
        days += 1
    days += day
    print("这是{}年第{}天。".format(year, days))


if __name__ == '__main__':
   main()
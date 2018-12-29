# coding=utf-8
'''
    作者:Wiggins
    日期:2018年11月6日
    版本:v3
'''


# def convert_currency(im, er):
#     out = im*er
#     return out

def main():
    usd_vs_rmb = 6.97
    currency_strValue = input("请输入带单位的货币金额(退出程序请输入Q)：")
    str_value = currency_strValue[:-3]
    unit = currency_strValue[-3:].upper()
    # print(unit)
    if unit == "USD":
        exchange_rate = usd_vs_rmb
    elif unit == "CNY":
        exchange_rate = 1/usd_vs_rmb
    else:
       exchange_rate = -1

    if exchange_rate != -1:
        inMoney = eval(str_value)
        # out1 = convert_currency(inMoney, exchange_rate)
        # 使用Lambda定义函数
        conver_curruncy2 = lambda x, y: x*y
        out1 = conver_curruncy2(inMoney, exchange_rate)
        print(out1)
    else:
        print("无效的汇率")

if __name__ == '__main__':
    main()

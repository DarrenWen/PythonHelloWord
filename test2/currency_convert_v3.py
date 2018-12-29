'''
    作者:Wiggins
    日期:2018年11月6日
    版本:v3
'''

# 汇率
usd_vs_rmb = 6.97

# 带单位的货币输入
currence_str_value = input("请输入带单位的货币金额(退出程序请输入Q)：")
while(currence_str_value != "Q"):
    str_value=currence_str_value[:-3];
    unit = currence_str_value[-3:].upper()
    # print(unit)
    if unit=="USD":
        rmb_value=eval(str_value)
        print("美元转人民币金额:",rmb_value*usd_vs_rmb)
    elif unit=="RMB":
        usd_value = eval(str_value)
        print("人民币转美元金额:", usd_value / usd_vs_rmb)
    else:
        print("不支持该汇率转换")
    print("********************************************************************")
    currence_str_value = input("请输入带单位的货币金额(退出程序请输入Q)：")
print("程序已退出")

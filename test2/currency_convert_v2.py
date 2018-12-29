# 汇率
usd_vs_rmb = 6.97

# 带单位的货币输入
currence_str_value = input("请输入带单位的货币金额：")
str_value=currence_str_value[:-3];
unit = currence_str_value[-3:].upper()
print(unit)
if unit=="USD":
    rmb_value=eval(str_value)
    print("美元转人民币金额:",rmb_value*usd_vs_rmb)
elif unit=="RMB":
    usd_value = eval(str_value)
    print("人民币转美元金额:", usd_value / usd_vs_rmb)
else:
    print("不支持该汇率转换")

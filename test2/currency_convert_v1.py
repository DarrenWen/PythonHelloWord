# 人民币的输入
rmb_value = input("请输入人民币金额：")
# 将字符串转换为数字
rmb_value = eval(rmb_value)
print(rmb_value)
# 美元兑人民币汇率
usd_vs_rmb = 6.97
usb_value = rmb_value/usd_vs_rmb
print("美元(USD)金额是:", usb_value)

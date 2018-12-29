"""
 作者：付文军
 功能:BMR 计算器
 版本:v2.0
 日期:2018年11月19日

"""

def main():
    """
    主函数
    :return:
    """
    a=5
    a *= 20+15*2+34
    print(a)
    print(float(1))
    y_or_n = input("是否退出程序(y/n)?")
    while y_or_n == "n":
        gender = input("性别：")
        # print(type(gender))
        height = float(input("体重(kg)："))
        # print(type(height))
        weight = int(input("身高(cm)："))
        # print(type(weight))
        age = int(input("年龄："))
        if gender == "男":
            bmr = (13.7*weight)+(5.0*height)-(6.8*age)+66
        elif gender == "女":
            bmr = (9.6*weight)+(1.8*height)-(4.7*age)+655
        else:
            bmr = -1
        if bmr != -1:
            print('基础代谢率(打卡)：', bmr)
        else:
            print('暂不支持该性别的BMR值计算')
        y_or_n = input("是否退出程序(y/n)?")

if __name__ == '__main__':
    main()

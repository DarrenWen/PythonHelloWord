"""
 作者：付文军
 功能:BMR 计算器
 版本:v1.0
 日期:2018年11月19日
"""

def main():
    """
    主函数
    :return:
    """
    # 性别
    gender = '男'
    # 身高
    height = 178
    # 体重
    weight = 80
    # 年龄
    age = 28
    if gender == "男":
        bmr = (13.7*weight)+(5.0*height)-(6.8*age)+66
    elif gender == "女":
        bmr = (9.6*weight)+(1.8*height)-(4.7*age)+655
    else:
        bmr = -1

    if bmr != -1:
        print('当前BMR值:', bmr)
    else:
        print('暂不支持该性别的BMR值计算')

if __name__ == '__main__':
    main()

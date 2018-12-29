"""
 作者：付文军
 功能:BMR 计算器
 版本:v3.0
 日期:2018年11月20日

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
        print('请输入以下信息:')
        input_str = input("性别 体重(kg) 身高(cm) 年龄：")
        str_array = input_str.split(' ')
        gender = str_array[0]
        # print(type(gender))
        height = float(str_array[1])
        # print(type(height))
        weight = int(str_array[2])
        # print(type(weight))
        age = int(str_array[3])
        if gender == "男":
            bmr = (13.7*weight)+(5.0*height)-(6.8*age)+66
        elif gender == "女":
            bmr = (9.6*weight)+(1.8*height)-(4.7*age)+655
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别:{},体重:{}kg,身高:{}cm,年龄:{}岁'.format(gender, weight, height, age))
            print('基础代谢率:{}大卡：'.format(bmr))
        else:
            print('暂不支持该性别的BMR值计算')
        y_or_n = input("是否退出程序(y/n)?")

if __name__ == '__main__':
    main()

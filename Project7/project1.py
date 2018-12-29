'''
    作者:付文军
    功能:判断密码强度
    版本:v1.0
    日期:2018年12月4日
'''
def main():
    '''
        主函数
    '''
    Password = input("请输入密码：")
    # 密码强度
    strength_level = 0

    # 规则1：密码长度大于8
    if len(Password)>=8:
        strength_level+=1
    else:
        print('密码长度不小于8位')
    if check_number_isexist(Password):
        strength_level+=1
    else:
        print('密码要包含数字')
    if check_letter_isexist(Password):
        strength_level+=1
    else:
        print('密码要包含字母')
    print('密码验证通过')

def check_number_isexist(password):
    for c in password:
        if c.isnumeric():
            return True
    return  False
def check_letter_isexist(password):
    # c = ""
    # c.isalpha()
    for c in password:
        if c.isalpha():
            return True
    return  False

if __name__ == '__main__':
    main()
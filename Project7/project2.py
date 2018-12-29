'''
    作者:付文军
    功能:判断密码强度
    版本:v2.0
    日期:2018年12月4日
    2.0 新增输入密码次数验证
'''
def main():
    '''
        主函数
    '''
    try_times = 5
    while try_times>0:
        Password = input("请输入密码：")
        # 密码强度
        strength_level = 0
        print()
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
            strength_level += 1
        else:
            print('密码要包含字母')
        if strength_level >= 3:
            print('密码验证通过')
            break
        else:
            try_times -= 1
            print('密码验证不通过')
    if try_times<=0:
        print('输入次数太多，请稍后再试!')

def check_number_isexist(password):
    has_number = False
    for c in password:
        if c.isnumeric():
            has_number = True
            break
    return  has_number
def check_letter_isexist(password):
    has_letter = False
    for c in password:
        if c.isalpha():
            has_letter=True
            break
    return  has_letter

if __name__ == '__main__':
    main()
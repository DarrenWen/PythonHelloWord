'''
    作者:付文军
    功能:判断密码强度
    版本: v5.0
    日期:2018年12月4日
    2.0 新增输入密码次数验证
    3.0 保存密码以及强度到文件中
    4.0 读取文件
    5.0 面向对象编程
'''


class PasswordTool:
    '''
        密码工具类
    '''
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0
        # 类的方法
    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
           self.strength_level += 1
        else:
            print('密码长度不小于8位')
        if self.check_number_isexist():
            self.strength_level+=1
        else:
            print('密码要包含数字')
        if self.check_letter_isexist():
            self.strength_level += 1
        else:
            print('密码要包含字母')

    def check_number_isexist(self):
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_isexist(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

def main():
    '''
        主函数
    '''


    try_times = 5
    while try_times>0:
        Password = input("请输入密码：")
        # 密码强度
        tool =  PasswordTool(Password)
        tool.process_password()
        write_file(tool.password, tool.strength_level)
        if tool.strength_level >= 3:
            print('密码验证通过')
            break
        else:
            try_times -= 1
            print('密码验证不通过')
    if try_times<=0:
        print('输入次数太多，请稍后再试!')
    # read_file()

def read_file():
    f = open('password_3.0.txt','r')
    # 1.0
    # content = f.read()
    # print(content)
    # 2.0
    # line = f.readline()
    # print(line)
    # 3.0
    # lines = f.readlines()
    # print(lines)
    for line in f:
        print(line)
    f.close()

def write_file(password,level):
   f = open('password_3.0.txt', 'a')
   f.write('密码：{},强度：{} \n'.format(password,level))
   f.close()

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
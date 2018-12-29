"""
    作者:付文军
    版本:v1.0
    日期:2018年12月12日
    功能:AQI计算
"""

def cal_liner(iaqi_lo,iaqi_hi,bp_lo,bp_hi,cp):
    """
        范围缩放
    """
    iaqi = (iaqi_hi-iaqi_lo)*(cp-bp_lo)/(bp_hi-bp_lo)+iaqi_lo
    return  iaqi

def cal_pm_aqi(pm_val):
    """
        计算PM2.5AQI
        :return:
    """
    if 0<= pm_val<36:
        iaqi = cal_liner(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_liner(50, 100, 35, 75, pm_val)
    else:
        pass

def cal_co_aqi(co_val):
    """
        计算CO AQI
    """
    if 0<= co_val<36:
        iaqi = cal_liner(0,50,0,3,co_val)
    elif 36 <= co_val < 76:
        iaqi = cal_liner(50,100,2,4,co_val)
    elif 76 <= co_val < 116:
        iaqi = cal_liner(100,150,75,115,co_val)
    else:
        pass



def cal_aql(parm_list):
    """
        AQI计算
    """
    pm_val = parm_list[0]
    co_val = parm_list[1]
    co_iaqi = cal_co_aqi(co_val)
    pm_iaqi = cal_pm_aqi(pm_val)


def main():
    """
        主函数
    """
    print('请输入以下信息，使用空格分割')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)


if __name__ == '__main__':
    main()

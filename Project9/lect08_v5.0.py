'''
    作者:付文军
    功能:模拟掷骰子
    版本:v5.0
    日期:2018年12月10日
    v2.0新增功能: 模拟投掷两个骰子
    v3.0新增功能: 数据可视化
    v4.0新增功能: 数据可视化 直方图
    v5.0 新增功能: 科学计算 使用numpy简化操作
'''
import numpy as np
import matplotlib.pyplot as plt

# 统计图中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def main():
    '''
        主函数
    '''
    total_times = 1000
    # 初始化列表
    roll1_array = np.random.randint(1, 7, size=total_times)
    roll2_array = np.random.randint(1, 7, size=total_times)
    result_array = roll1_array+roll2_array
    hist,bins = np.histogram(result_array,bins=range(2,14))
    print(hist)
    print(bins)
    # 数据可视化
    plt.hist(result_array, bins=range(2, 14),density=1, edgecolor='black', linewidth=1,rwidth=0.8)
    plt.title("骰子点数统计")

    plt.xlabel("点数")
    plt.ylabel("频率")
    plt.show()

if __name__ == '__main__':
    main()

"""
    作者:Wiggins
    功能:五角星绘制
    版本:v1.0
    日期:2018年11月8日
"""
import turtle
def main():
    """
    主函数
    :return:
    """
    #计数器
    count=0

    while count < 5:
        turtle.forward(300)
        turtle.right(144)
        count += 1


    turtle.exitonclick()


if __name__=="__main__":
    main()

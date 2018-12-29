"""
    作者:Wiggins
    功能:五角星绘制 加入
    版本:v2.0
    日期:2018年11月8日
    新增功能：加入循环输出五角星操作
"""
import turtle

def printStar(length):
    #计数器
    count=0
    while count < 5:
        turtle.forward(length)
        turtle.right(144)
        count += 1


def main():
    """
    主函数
    :return:
    """
    size = 30
    turtle.penup()
    turtle.backward(200)
    turtle.pencolor("red")
    turtle.pendown()
    while size<=300:
        size+=20
        printStar(size)
    turtle.exitonclick()


if __name__=="__main__":
    main()

"""
    作者:Wiggins
    功能:分形树
    版本:v1.0
    日期:2018年11月19日
    新增功能：利用递归绘制分型树
"""
import turtle

def draw_Branch(length):
    """
    :param 绘制分型树函数:
    :return:
    """
    if(length>5):
        """
        绘制右侧树枝
        """
        turtle.forward(length)
        turtle.right(20)
        draw_Branch(length-15)
        # 绘制左侧树枝
        turtle.left(40)
        draw_Branch(length-15)
        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(length)
def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color("brown")
    draw_Branch(100)
    turtle.exitonclick()

if __name__=="__main__":
    main()

import turtle as t #引入turtle库
'''定义函数'''
def drawlinex(selet='3'):   #横向划线
    t.forward(50)
    t.penup()
    t.forward(10)
    if selet==1:    #判断左右和pass
        t.right(90)
        t.forward(10)
        t.pendown()
    elif selet==0:
        t.left(90)
        t.forward(10)
        t.pendown()
    else:
        t.forward(10)
        t.pendown()
        pass
def drawliney(selet='3'):   #纵向换线
    t.forward(50)
    t.penup()
    t.forward(10)
    if selet==1:    #判断左右和pass
        t.right(90)
        t.forward(10)
        t.pendown()
    elif selet==0:
        t.left(90)
        t.forward(10)
        t.pendown()
    else:
        t.forward(10)
        t.pendown()
        pass
'''主程序'''
t.pensize(10)
t.speed(1000)
drawlinex(0)
drawliney(0)
drawlinex(0)
drawliney()
drawliney(0)
drawlinex(0)
drawliney(0)
input()
exit()

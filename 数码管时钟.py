import turtle as t #引入turtle库
import time  as m
'''定义函数'''
def drawlinex( selet='3',mode='0'):   #横向划线
    if mode==0:		#判断是否写出
        t.fd(50)
        t.up()
        t.fd(10)
    elif mode==1:
        t.up() 
        t.fd(60)
    else:
        print('ERROR！\n请输入‘mode值为1或零’')
        input()
        exit()
    if selet==1:  #判断左右和pass
        t.rt(90)
        t.fd(10)
        t.pendown()
    elif selet==0:
        t.left(90)
        t.forward(10)
        t.down()
    else:
        t.fd(10)
        t.down()
        pass

def drawliney(selet='3',mode='0'):   #纵向换线
    if mode==0:		#判断是否写出
        t.fd(50)
        t.up()
        t.fd(10)
    elif mode==1:
        t.up()
        t.fd(60)
    else:
        print('ERROR！\n请输入‘mode值为1或零’')
        input()
        exit()
    if selet==1:    #判断左右和pass
        t.rt(90)
        t.fd(10)
        t.down()
    elif selet==0:
        t.lt(90)
        t.fd(10)
        t.down()
    else:
        t.fd(10)
        t.down()
        pass
'''数字函数'''
def drawmath(math='0'):
    if math ==1:
        drawlinex(0,1)
        drawliney(0,0)           
        drawlinex(0,1)
        drawliney(0,1)
        drawlinex(1,1)
        drawliney(3,0) #1的显示以下递增
    elif math == 2:
        drawlinex(0,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawliney(3,1)
        drawlinex(0,0)
        drawliney(3,0) 
    elif math == 3:
        drawlinex(0,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawliney(3,1)
        drawliney(0,1)
        drawlinex(0,0)
        drawliney(3,0)
    elif math ==4:
        drawlinex(0,0)
        drawliney(0,0)
        drawlinex(0,1)
        drawliney(3,0)
        drawliney(0,1)
        drawlinex(0,1)
        drawliney(3,0)
    elif math ==5:
        drawlinex(0,0)
        drawliney(0,1)
        drawlinex(0,0)
        drawliney(3,0)
        drawliney(0,1)
        drawlinex(0,0)
        drawliney(3,0)
    elif math ==6:
        drawlinex(0,0)
        drawliney(0,1)
        drawlinex(0,0)
        drawliney(3,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawlinex(3,0)
    elif math ==7:
        drawlinex(0,1)
        drawliney(0,0)
        drawlinex(0,0)
        drawliney(3,1)
        drawliney(0,1)
        drawlinex(0,1)
        drawlinex(3,0)
    elif math ==8:
        drawlinex(0,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawliney(3,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawlinex(3,0)
    elif math ==9:
        drawlinex(0,0)
        drawliney(0,0)
        drawlinex(0,0)
        drawliney(3,0)
        drawliney(0,1)
        drawlinex(0,0)
        drawliney(3,0)
    else:
        print("ERROR!\nDon't input outside from 1 to 9 !")
        input()
        exit()

'''主程序'''                                                                             
t.pensize(10)
t.speed(1000)
t.ht() #隐藏海龟
Nt = m.localtime()
Hour1 = int(int(m.strftime('%I',Nt)) / 10)                                                        
Hour2 = int(m.strftime('%I',Nt)) % 10
Min1 = int(int(m.strftime('%M',Nt))  / 10)
Min2 = int(m.strftime('%M',Nt))  % 10
if Hour1==0 and Min1==0:
    drawmath(Hour2)
    t.up()
    t.home()
    t.goto(100,50)
    t.down() 
    t.dot(10)
    t.up() 
    t.home()
    t.goto(100,-50)
    t.down()
    t.dot(10)
    t.up()
    t.home()
    t.goto(150,0)
    t.down()
    drawmath(Min2)
elif Hour1==0 and Min1>=1:
    drawmath(Hour2)
    t.up()
    t.home()
    t.goto(100,50)
    t.down() 
    t.dot(10)
    t.up() 
    t.home()
    t.goto(100,-50)
    t.down()
    t.dot(10)
    t.up()
    t.home()
    t.goto(150,0)
    t.down()
    drawmath(Min1)
    t.up()
    t.home()
    t.goto(250,0)
    t.down()
    drawmath(Min2)
elif Hour1== 1 and Min1>=1:
    drawmath(Hour1)
    t.up
    t.home()
    t.goto(100,0)
    t.down()
    drawmath(Hour2)
    t.up()
    t.home()
    t.goto(150,50)
    t.down()
    t.dot(10)
    t.up()
    t.home()
    t.goto(150,-50)
    t.down()
    t.dot(10)
    t.up()
    t.home()
    t.goto(200,0)
    t.down()
    drawmath(Min1)
    t.up()
    t.home()
    t.goto(300,0)
    t.down()
    drawmath(Min2)
input()
exit()

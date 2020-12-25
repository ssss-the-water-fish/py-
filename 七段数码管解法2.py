import turtle as t
import time as m
def drawline(selet):
    t.down() if selet == 'true' elif selet =='false'  t.up()
    t.fd(50) 
    t.up()
    t.fd(5)
    t.down()
    t.left(90)
    t.up()
    t.fd(5)
    t.down()
def drawmath(math):
    drawline(true) if math in [0,2,3,4,5,6,8,9] else drawline(false)

localTime=m.gmtime()
localTime_Hour= m.strftime('%H',localTime)
drawline(localTime)


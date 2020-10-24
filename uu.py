
a = eval(input("请输入时间！(请以分钟为基本单位)"))

if a == 30 or a == 0:
    print("免费！")
elif a < 30 or a == 0:
    print("免费！")

if a < 0 and a != 0 :
    a *= (-1)
elif a > 30 and a != 0:
    a -= 30
    b = a / 60 * 3
    print("请付费", b ,"元")

input("请按任意健退出\n")
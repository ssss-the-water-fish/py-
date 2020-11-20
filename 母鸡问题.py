for a in range(0,20):
    for b in range(0,33):
        for c in range(0,300):
            if a+b+c==100 and a*5+b*3+c*(1/3)==100:
                print('%s\000%s\000%s\000%s\000%s\000%s'%('公鸡:',a,'母鸡:',b,'小鸡:',c))
input('按任意键结束!')
exit()

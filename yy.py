def adds(n1,n2):
    s = n1*n2
    return s

for n1 in range(1,10):
    for n2 in range(1,n1+1):
        print('%sx%s=%s'%(n1,n2,adds(n1,n2)),'\000',end='')
    print('\n')
    print('%s'%('----------------------------------------------------------------'))
    print()
input('按任意健退出！')
exit()

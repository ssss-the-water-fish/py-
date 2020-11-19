#5*a+3*b+3*c=100
#a+b+c=100
for a in range(0,20):
    for b in range(0,33):
        for c in range(0,300):
            if a+b+c==100 and 5*a+3*b+(1/3)*c==100:
                print(a,b,c)
input()
exit()
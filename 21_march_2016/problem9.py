from math import *
for a in range(1,1000):
    if not a%2==0:
        temp=(a/2)**2
        b=temp-1
        c=temp+1
    else:
        temp=(a**2)//2
        b=temp
        c=temp+1
    if a+b+c==1000:
        print(a,b,c)
        print(a*b*c)
        break
        

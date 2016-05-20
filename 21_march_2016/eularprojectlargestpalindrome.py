max=1
for i in range(100,1000):
    for j in range (100,i):
        t=i*j
        if int(str(t)[::-1])==t:
            if t>max:
                max=t
print(max)

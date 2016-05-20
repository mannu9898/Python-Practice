n=1
while n>0:
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
        else:
            n = 3 * n + 1
        print(n)
    n+=1

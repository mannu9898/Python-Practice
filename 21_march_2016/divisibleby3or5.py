x=int(input())
sum=0
for i in range(1,x):
    if i%3==0 or i%5==0:
        sum=sum+i
    elif i%3==0 and i%5==0:
        sum=sum-i
print(sum)

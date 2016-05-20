def lcm(x, y):
    global t
    """Returns the least common multiple of x and y."""
    #multiples = []
    high = x*y
    for i in range(1,high+1):
        if i % x == 0 and i % y == 0:
            t=i
            break
            #multiples.append(i)
   # multiples.sort()
   # t=multiples[0]
    return z

z=1
t=1
for i in range(1,21):
   lcm(i,t)


print(t)

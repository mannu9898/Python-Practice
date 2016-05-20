a = int(input())
for i in range(0,a):
	
    final = []
    z = []
    n = int(input())

    for l in range(0,n):
        t = int(input())
        z.append(t)
	
    for j in range(0,n):
        final.append(0)
        for k in range(j+1,n):
            if z[k]<z[j]:
                final[j] = (k-j)
                break
                        
	
	
	#for i in range(0,len(final)):
		#print(final[i])
        print(z,final)

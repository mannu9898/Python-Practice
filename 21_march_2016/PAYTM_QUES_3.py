
arr = [[37,36,35,34,33,32,31] , [38,17,16,15,14,13,30] , [39,18,5,4,3,12,29] , [40,19,6,1,2,11,28] , [41,20,7,8,9,10,27] , [42,21,22,23,24,25,26] , [43,44,45,46,47,48,49]]




def isPrime(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return False

    return True




prime = 2;
total_daigonal_elems = 0;
t = int(input())
for i in range(0,t):
	max_row_value = int(input())
	for j in range(0 ,max_row_value):
		for k in range(0,max_row_value):
			if((j==k) or i+j==max_row_value-1):
				if(isPrime(arr[j][k])==True):
					prime = prime + 1;
					#total_diagoanl_elems = total_daigonal_elems + 1;
				#else:
					#total_daigonal_elems = total_daigonal_elems + 1;
					
d =(prime*100)/13

print(format(d, '.2f'))

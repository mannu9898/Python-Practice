Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> n=1000
>>> for a in range(1,n/2):
	for b in range(1,a):
		if (a**2+b**2-(n-a-b)**2) == 0:
			print(a,b,n-a-b,a*b*(n-a-b))

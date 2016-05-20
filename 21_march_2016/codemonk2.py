a = int(input())
for i in range(0,a):
	n = int(input())
	raw_ip = input()
	splitted = raw_ip.split()
	z = map(int,splitted)
	sort = z.sorted()


print(z)

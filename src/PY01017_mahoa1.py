t = int(input())

while t>0:
	str = input()
	l = len(str)
	dem = 1
	for i in range(1,l):
		if str[i] != str[i-1]:
			print(dem,end='')
			print(str[i-1],end='')
			dem = 1
		else:
			dem += 1
	print(dem,end='')
	print(str[l-1],end='\n')
	t -= 1 
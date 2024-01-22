# PY01038_kiemtrachiahetcho7.py

t = int(input())
while t>0:
	n = input()
	i = 1
	d = 0
	while i<=1000:
		if int(n)%7==0:
			print(n)
			d = 1
			break
		else:
			a = n[::-1]
			b = int(a) + int(n)
			n = str(b)
		i += 1
	if d==0: print(-1)
	t-=1
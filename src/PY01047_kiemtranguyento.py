# PY01047_kiemtranguyento.py
import math
t = int(input())

def check(n):
	if n<2: return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0: return False
	return True

while t>0:
	s = input()
	l = len(s)
	n = s[l-4] + s[l-3] + s[l-2] + s[l-1]
	n = int(n)
	if check(n)==True: print("YES")
	else: print("NO")
	t-=1
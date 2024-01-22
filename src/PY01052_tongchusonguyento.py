# PY01052_tongchusonguyento.py
import math
t = int(input())
def checknt(n):
	if n<2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True

def solve(s):
	sum = 0
	for i in s:
		sum+=int(i)
	if checknt(sum)==True: print("YES")
	else: print("NO")

while t>0:
	s = input()
	solve(s)
	t-=1
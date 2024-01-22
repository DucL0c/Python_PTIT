# PY01053_sochiahetcho3.py
t = int(input())

def solve(s):
	sum = 0
	for i in s:
		sum+=int(i)
	if sum%3==0: print("YES")
	else: print("NO")

while t>0:
	s = input()
	solve(s)
	t-=1
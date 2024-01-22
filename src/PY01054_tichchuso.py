# PY01054_tichchuso.py
t = int(input())

def solve(s):
	ans = 1
	for i in s:
		if i!='0':
			ans *= int(i)
	print(ans)

while t>0:
	s = input()
	solve(s)
	t-=1
# PY01055_soxenke.py
t = int(input())

def solve(s):
	if len(s)%2==0: return False
	if s[0]==s[1]: return False
	for i in range(2,len(s),2):
		if s[i] != s[0]:
			return False
	return True

while t>0:
	s = input()
	if solve(s)==True: print("YES")
	else: print("NO")
	t-=1
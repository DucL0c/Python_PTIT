# PY01042_hecoso3.py
t = int(input())

def check(s):
	for i in s:
		if i=='0' or i=='1' or i=='2':
			continue
		else:
			return False
	return True

while t>0:
	s = input()
	if check(s) == True: print("YES")
	else: print("NO")	
	t-=1
# PY01043_sothuannghichchan.py
t = int(input())

def check(s):
	if len(s)%2!=0 or s != s[::-1]:
		return False
	for i in s:
		if int(i)%2!=0:
			return False
	return True

while t>0:
	n = int(input())
	for i in range(22,n,2):
		if check(str(i))==True:
			print(i,end = " ")
	print()
	t-=1
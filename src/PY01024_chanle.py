t = int(input())

def check1(s):
	l = len(s)
	sum = 0
	for i in range(0,l):
		sum += int(s[i])
	if sum%10==0: return True
	else: return False

def check2(s):
	l = len(n)
	d = 1
	for i in range(1,l):
		if (int(s[i]) + 2 == int(s[i-1])) or (int(s[i]) - 2 == int(s[i-1])):
			continue
		else: d = 0
	if d==0: return False
	else: return True 

while t>0:
	n = input()
	check1(n)
	if(check1(n)==True and check2(n)==True): print("YES")
	else: print("NO")
	t-=1
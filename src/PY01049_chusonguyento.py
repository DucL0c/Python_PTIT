# PY01049_chusonguyento.py
import math
t = int(input())

def checknt(n):
	if n<2: return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n%i==0: return False
	return True

def check(s):
	if checknt(len(s))==False: return False
	demnt = 0
	for i in range(0,len(s)):
		if checknt(int(s[i]))==True:
			demnt +=1
	demkont = len(s) - demnt
	if demnt<=demkont: return False
	return True


while t>0:
	s = input()

	if check(s)==True: print("YES")
	else: print("NO")
	t-=1
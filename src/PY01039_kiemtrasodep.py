# PY01039_kiemtrasodep.py
t = int(input())

def check1(s):
	st = {1,2,3}
	st.clear()
	for i in s:
		st.add(i)
	if len(st)==2:
		return True
	else:
		return False

def check2(s):
	for i in range(1,len(s)):
		if s[i] == s[i-1]: return False
	
	return True


while t>0:
	s = input()
	if  check1(s)==True and check2(s)==True: print("YES")
	else: print("NO")
	t-=1
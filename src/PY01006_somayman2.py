t = int(input())
while t>0:
	s = input()
	check = 0
	for i in s:
		if(i!='4' and i!='7'):
			check = 1
			break
	if(check==0): print("YES")
	else: print("NO")
	t-=1
t = int(input())
while t>0:
	s = input()
	tmp = s[::-1]
	d = 1
	for i in range(1,len(s)):
		if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(tmp[i])-ord(tmp[i-1])):
			d = 0
	if d==0: print("NO")
	else: print("YES")

	t-=1
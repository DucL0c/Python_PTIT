t = int(input())
while t>0:
	str = input()
	n = len(str)
	if (str[0]==str[n-2] and str[1]==str[n-1]): print("YES")
	else: print("NO")
	t -= 1

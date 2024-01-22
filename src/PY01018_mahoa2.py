p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
	tmp = input()
	if(tmp[0]=='0'): 
		break
	k,s = tmp.split()
	k = int(k)
	res = ""
	for i in s:
		res += p[(p.find(i)+k)%28]
	print(res[::-1])
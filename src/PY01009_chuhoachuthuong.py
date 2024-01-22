str = input()
demhoa = 0
demthuong = 0
for i in str:
	if ord(i) >= 65 and ord(i)<=90:
		demhoa += 1
	else:
		demthuong += 1
if(demhoa>demthuong): 
	print(str.upper())
else: 
	print(str.lower())
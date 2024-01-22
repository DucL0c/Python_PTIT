t = int(input())

def tongchan(n):
	sum = 0
	for i in range(2,n+2,2):
		sum += float(1/i)
	print('{0:.{1}f}'.format(sum, 6))

def tongle(n):
	sum = 0
	for i in range(1,n+2,2):
		sum += float(1/i)
	print('{0:.{1}f}'.format(sum, 6))

while t>0:
	n = int(input())
	if n%2==0:
		tongchan(n)
	else: 
		tongle(n)
	t-=1
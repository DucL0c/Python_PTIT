# PY01046_thaphanoi.py
def chuyen(n,a,b):
	print(a + ' -> ' + b)

def thn(n,a,b,c):
	if n==1: chuyen(n,a,c)
	else:
		thn(n-1,a,c,b)
		chuyen(n,a,c)
		thn(n-1,b,a,c)

n = int(input())
a,b,c = 'A','B','C'
thn(n,a,b,c)

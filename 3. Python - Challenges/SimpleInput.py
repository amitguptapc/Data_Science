sum=0
while sum>=0:
	try:
		a = int(input())
	except :
		break
	sum+=a
	if sum>=0:
		print(a)

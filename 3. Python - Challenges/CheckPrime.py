def isPrime(n):
	if n<=1:
		return 'Not Prime'
	if n<=3:
		return 'Prime'
	if n%2==0 or n%3==0:
		return 'Not Prime'
	i=5
	while i*i<=n:
		if n%i==0 or n%(i+2)==0:
			return "Not Prime"
		i+=6
	return 'Prime'

n= int(input())
print(isPrime(n))

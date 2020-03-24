def parentheses(n,o,c,s):
	if c==n:
		print(s)
		return
	else:
		if o>c:
			parentheses(n,o,c+1,s+')')
		if o<n:
			parentheses(n,o+1,c,s+'(')
	return	

n=int(input())
parentheses(n,0,0,'')


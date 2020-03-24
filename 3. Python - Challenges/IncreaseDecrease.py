n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
inc = False
dec = True
flag = 0
repeat = 0
m=min(a)
c=a.count(m)
for i in range(n-1):
    if a[i]>a[i+1] and inc == True:
        flag=1
        break
    elif a[i]<a[i+1]:
        inc = True
    if a[i]==a[i+1]and a[i]!=m:
        repeat=1
if flag == 0 and repeat == 0 and (c==1 or c==2):
    print("true")
else:
    print("false")

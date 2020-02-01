from math import sqrt
def sieve(n):
    a = [0]*(n+1)
    a[2]=1
    for i in range(3,n+1,2):
        a[i]=1
    for i in range(3,int(sqrt(n))+1,2):
        if a[i]==1:
            for j in range(i*i,n+1,2*i):
                a[j]=0
    return a

def segment(a,b):
    val=sieve(int(sqrt(b)))
    res = [1]*(b-a+1)
    for i in range(2,int(sqrt(b))+1):
        if val[i]==1:
            for j in range(a,b+1):
                if i==j:
                    continue
                if j%i==0:
                    res[j-a]=0
    return res

t = int(input())
while t>0:
    m =[int(x) for x in input().split()]
    a=m[0]
    b=m[1]
    r = segment(a,b)
    for i in range(len(r)):
        if r[i]==1 and a+i !=1:
            print(a+i,end=" ")
    print()
    t-=1

from math import sqrt
t = int(input())
while t>0:
    n=int(input())
    a,b=0,int(sqrt(n))
    while a<=b:
        if (a**2)+(b**2)==n:
            print("({},{})".format(a,b),end=" ")
            a+=1
            b-=1
        elif (a**2)+(b**2)>n:
            b-=1
        else:
            a+=1
    print()
    t-=1

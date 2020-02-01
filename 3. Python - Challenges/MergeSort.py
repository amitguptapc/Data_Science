def merge(a,l,m,r):
    n1 = m-l+1
    n2 = r-m
    L = [0]*n1
    R = [0]*n2
    for i in range(0,n1):
        L[i] = a[l+i]
    for j in range(0,n2):
        R[j] = a[m+j+1]
    i,j,k = 0,0,l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            a[k]=L[i]
            k+=1
            i+=1
        else:
            a[k]=R[j]
            k+=1
            j+=1
    while i<n1:
        a[k]=L[i]
        k+=1
        i+=1
    while j<n2:
        a[k]=R[j]
        k+=1
        j+=1

def mergeSort(a,l,r):
    if l<r:
        m = (l+r)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)

n = int(input())
a = [int(x) for x in input().split()]
mergeSort(a,0,n-1)
for i in a:
    print(i,end=" ")

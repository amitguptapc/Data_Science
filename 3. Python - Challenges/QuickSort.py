def partition(arr,lo,hi):
    i=lo-1
    pivot=arr[hi]
    for j in range(lo,hi):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[hi]=arr[hi],arr[i+1]
    return i+1

def quick_sort(arr,lo,hi):
    if lo<hi:
        mid=partition(arr,lo,hi)
        quick_sort(arr,lo,mid-1)
        quick_sort(arr,mid+1,hi)

n =int(input())
arr=[int(x) for x in input().split()]
quick_sort(arr,0,n-1)
for i in arr:
    print(i,end=" ")

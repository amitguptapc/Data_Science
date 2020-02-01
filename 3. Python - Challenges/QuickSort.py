def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

n =int(input())
arr=[int(x) for x in input().split()]
arr=quicksort(arr)
for i in arr:
    print(i,end=" ")

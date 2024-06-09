def binarysearch(arr,n,elem):
    lb = 0
    ub = n-1
    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == elem:
            return mid + 1
        elif arr[mid] < elem:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1

arr = [2,4,5,9,12,15,17,22]
n = len(arr)
elem = 17
result = binarysearch(arr,n,elem)
print(result)
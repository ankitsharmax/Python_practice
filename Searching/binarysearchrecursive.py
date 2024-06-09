def binarysearchrecursive(arr,lb,ub,elem):
    if lb <= ub:
        mid = (lb + ub)//2
        if arr[mid] == elem:
            return mid + 1
        elif arr[mid] < elem:
            return binarysearchrecursive(arr,mid+1,ub,elem)
        else:
            return binarysearchrecursive(arr,lb, mid-1, elem)
    return -1

arr = [2,3,4,6,8,9,12,15,17,22]
n = len(arr)
elem = 22
lb = 0
ub = n-1
result = binarysearchrecursive(arr,lb,ub,elem)
print(result)
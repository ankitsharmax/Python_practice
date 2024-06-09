def linearsearch(arr,n,elem):
    for i in range(n):
        if arr[i] == elem:
            return i+1
    return -1


arr = [12,11,2,5,16,22,13,17]
n = len(arr)
elem = 13
result = linearsearch(arr,n,elem)
print(result)
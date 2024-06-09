class QuickSort:
    def partition(self,arr,lb,ub):
        pivot = arr[lb]
        start = lb
        end = ub
        while (start<end):
            while(arr[start]<=pivot and start<ub):
                start += 1
            while(arr[end]>pivot):
                end -= 1
            if start < end:
                arr[start],arr[end] = arr[end],arr[start]
        arr[lb],arr[end] = arr[end], arr[lb]

        return end

    def quickSort(self,arr,lb,ub):
        if lb < ub:
            loc = self.partition(arr,lb,ub)
            self.quickSort(arr,lb,loc-1)
            self.quickSort(arr,loc+1,ub)

if __name__ == '__main__':
    n = int(input("Enter Size of Array: "))
    arr = list(map(int, input("Enter arr: \n").split()))
    print("Array Before: {}".format(arr))
    lb = 0
    ub = n-1
    qs = QuickSort()
    qs.quickSort(arr, lb, ub)
    print("Array After: {}".format(arr))
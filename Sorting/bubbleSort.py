class BubbleSort:
    def bubbleSort(self,arr,n):
        for i in range(n-1):
            flag = False
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = True
            if flag == False:
                return

if __name__ == '__main__':
    n = int(input("Enter Size of array: "))
    arr = list(map(int,input("Enter array:\n").split()))
    print("Array Before: {}".format(arr))
    bs = BubbleSort()
    bs.bubbleSort(arr,n)
    print("Array After: {}".format(arr))
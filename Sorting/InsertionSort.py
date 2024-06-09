class InsertionSort:
    def insertionSort(self, arr, n):
        '''sorted | unsorted ------ '''
        # start from index 1
        for i in range(1,n):
            temp = arr[i]
            j = i-1
            while(j>=0 and arr[j]>temp):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = temp


if __name__ == '__main__':
    n = int(input("Enter Size of Array: "))
    arr = list(map(int, input("Enter arr: \n").split()))
    print("Array Before: {}".format(arr))
    ins = InsertionSort()
    ins.insertionSort(arr, n)
    print("Array After: {}".format(arr))

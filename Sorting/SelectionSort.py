class SelectionSort:
    def selectionSort(self,arr,n):
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min = j
            if min != i:
                arr[min], arr[i] = arr[i], arr[min]


if __name__ == '__main__':
    n = int(input("Enter Size of Array: "))
    arr = list(map(int, input("Enter arr: \n").split()))
    print("Array Before: {}".format(arr))
    sel = SelectionSort()
    sel.selectionSort(arr, n)
    print("Array After: {}".format(arr))
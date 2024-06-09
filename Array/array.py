class Array:
    def __init__(self,arr,n):
        self.arr = arr
        self.n = n

    def addEnd(self,value):
        self.arr.append(value)

    def addFirst(self,value):
        self.arr[:] = [value] + self.arr[:]

    def addPos(self,key,value):
        self.arr.insert(key,value)

    def sortArray(self,reverse=False):
        self.arr.sort(reverse=reverse)

    def delEnd(self):
        self.arr.pop()

    def delFirst(self):
        self.arr = self.arr[1:]

    def delPos(self,key):
        self.arr.remove(self.arr[key-1])

    def delValue(self,value):
        self.arr.remove(value)

    def length(self):
        print("Array Length: ",len(self.arr))

    def reverseArr(self):
        self.arr.reverse()

    def swap(self,key1,key2):
        self.arr[key1], self.arr[key2] = self.arr[key2], self.arr[key1]

    def deleteArr(self):
        self.arr.clear()

    def display(self):
        print("Array is: ",self.arr)

if __name__ == '__main__':
    arr = [1,2,0,5,4,2]
    n = len(arr)
    array = Array(arr,n)
    array.addEnd(12)
    array.display()
    array.addFirst(-3)
    array.display()
    array.addPos(4,999)
    array.display()
    array.sortArray()
    array.display()
    array.delEnd()
    array.display()
    array.delFirst()
    array.display()
    array.delPos(3)
    array.display()
    array.delValue(5)
    array.display()
    array.length()
    array.reverseArr()
    array.display()
    array.sortArray(reverse=False)
    array.display()
    array.swap(4,0)
    array.display()
    array.deleteArr()
    array.display()
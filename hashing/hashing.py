# Creating a hash function
'''
There are various ways of creating a hash function.
Here I am using ASCII method which is available in python via ord() function.
'''

class HashTable:
    def __init__(self):
        self.MAX = 10 # supposing the max size of the hash table
        self.arr = [None for i in range(self.MAX)] # creating a array to hold the values

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

ht = HashTable()
ht.add('march 6',103)
ht.add('march 12',12)
ht.add('march 2',22)
ht.add('march 8',353)
print(ht.arr)
print(ht.get('march 6'))

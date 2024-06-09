class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,N):
        self.head = None
        self.tail = None
        self.N = N
        self.count = -1

    def isEmpty(self):
        if self.head == None and self.tail == None:
            return True
        else:
            return False

    def isFull(self):
        if self.count == N-1:
            return True
        else:
            return False

    def enqueue(self):
        val = int(input("Enter value to enqueue: "))
        newnode = Node(data=val)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
            self.count += 1
        elif self.isFull():
            print("Queue is Full: Overflow")
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            print("Empty Queue: Underflow")
        else:
            item = self.head.data
            self.head = self.head.next
            print("Dequeued: ",item)

    def peek(self):
        if self.isEmpty():
            print("Empty Queue: Underflow")
        else:
            print("Head: ",self.head.data)
            print("Tail: ",self.tail.data)

    def display(self):
        temp = self.head
        res = ''
        while temp:
            res += str(temp.data) + '->'
            temp = temp.next
        print(res)

if __name__ == '__main__':
    N = int(input("Enter the size of Queue: "))
    ll = LinkedList(N)
    ll.enqueue()
    ll.enqueue()
    ll.enqueue()
    ll.display()
    ll.peek()
    ll.dequeue()
    ll.display()
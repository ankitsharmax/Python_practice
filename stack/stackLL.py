class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,N,top):
        self.head = None
        self.N = N
        self.top = top

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.N:
            return True
        else:
            return False

    def push(self):
        if self.isFull():
            return "Overflow"
        value = int(input("Enter data to push: "))
        if self.isEmpty():
            self.head = Node(data=value)
            return
        else:
            newnode = Node(data=value)
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            self.top += 1

    def pop(self):
        if self.isEmpty():
            return "Underflow"
        temp = self.head
        prev = self.head
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        self.top -= 1
        print("Popped: ",temp.data)

    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        temp = self.head
        while temp.next != None:
            temp = temp.next
        print(temp.data)

    def display(self):
        if self.isEmpty():
            return "Empty Stack"
        temp = self.head
        res = ''
        while temp != None:
            res += str(temp.data) + '-->'
            temp = temp.next
        print(res)

if __name__ == '__main__':
    N = int(input("Enter size of Stack: "))
    ll = LinkedList(N,top=-1)
    ll.push()
    ll.push()
    ll.display()
    ll.peek()
    ll.pop()
    ll.display()
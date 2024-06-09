class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,next = self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data)

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        temp = self.head
        while temp and count<index-1:
            count += 1
            temp = temp.next
        node = Node(data,next=temp.next)
        temp.next = node

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def display(self):
        temp = self.head
        listStr = ''
        while temp:
            listStr += str(temp.data) + '-->'
            temp = temp.next
        return listStr[:-3]


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(5)
    ll.insert_at_end(24)
    print(ll.display())
    print(ll.get_length())
    ll.insert_at_index(2,11)
    print(ll.display())
    ll.insert_values(['alpha','beta','gamma'])
    print(ll.display())
    

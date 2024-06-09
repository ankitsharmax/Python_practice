class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        else:
            node = Node(data,next=None)

            temp = self.head
            while temp.next is not None:
                temp = temp.next
            else:
                temp.next = node
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            temp = temp.next
        return count
    def insert_at_pos(self,pos,data):
        if pos<0 or pos>=self.get_length():
            raise Exception("Invalid Index")
        if pos ==0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            temp = self.head
            while temp:
                if count == pos-1:
                    node = Node(data,next = temp.next)
                    temp.next = node
                    break
                temp = temp.next
                count += 1
 
    def delete_at_pos(self,pos):
        if pos<0 or pos>= self.get_length():
            raise Exception("Invalid Index")
        if pos == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            temp = self.head
            while temp:
                if count == pos-1:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                count += 1
        

    def print(self):
        if self.head is None:
            print("Undeflow")
            return

        temp = self.head
        listStr = ''
        while temp:
            listStr += str(temp.data) + '-->'
            temp = temp.next
        print(listStr)

if __name__ == '__main__':
    ll = LinkedList()
    choices = '''
0: Demo Linked List
1. Display Linked List
2. Insert at beginning
3. Insert at end
4. Insert in between
5. Delete at beginning
6. Delete at end
7. Delete in between
8. Update at beginning
9. Update at end
10. Update in between
11. Insert multiple values in list
12. Length of the linked list
13. Delete at position
14. Insert at position

'''
    print(choices)
    while True:
        choice = int(input("Choose an option: "))
        if choice == 0:
            ll.insert_values(['alpha','beta','gamma','omega'])
        if choice == 1:
            ll.print()
        if choice == 2:
            data = int(input("Enter the data value: "))
            ll.insert_at_beginning(data)
        if choice == 3:
            data = int(input("Enter the data value: "))
            ll.insert_at_end(data)
        if choice == 11:
            data = list(input("Enter muliple values in line: ").split())
            ll.insert_values(data)
        if choice == 12:
            print(ll.get_length())
        if choice == 13:
            pos = int(input("Enter the data index to be delete: "))
            ll.delete_at_pos(pos)
        if choice == 14:
            pos,data = input("Enter index and data value to insert: ").split()
            ll.insert_at_pos(int(pos),data)

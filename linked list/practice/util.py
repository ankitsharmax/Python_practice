class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Demo:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data)

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def display(self):
        temp = self.head
        listStr = ''
        while temp:
            listStr += str(temp.data) + '-->'
            temp = temp.next
        return listStr[:-3]

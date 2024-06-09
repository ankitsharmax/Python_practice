import util 

class LinkedList(util.Demo):
    def __init__(self):
        self.head = None

    def delete_at_beginning(self):
        self.head = self.head.next

    def delete_at_end(self):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete_at_index(self,index):
        if index<0 or index>self.get_length()-1:
            raise Exception("Invalid Index")
        if index == 0:
            self.delete_at_beginning()
            return
        count = 0
        temp = self.head
        while temp and count<index-1:
            count += 1
            temp = temp.next
        temp.next = temp.next.next

if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_values([5,11,12,24,44,50])
    print(ll.display())
    ll.delete_at_beginning()
    print(ll.display())
    ll.delete_at_end()
    print(ll.display())
    print(ll.get_length())
    ll.delete_at_index(1)
    print(ll.display())



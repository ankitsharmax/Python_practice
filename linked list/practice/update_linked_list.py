import util

class LinkedList(util.Demo):
    def update_at_beginning(self,data):
        self.head.data = data

    def update_at_end(self,data):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next.data = data

    def update_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.update_at_beginning(data)
            return
        count = 0
        temp = self.head
        while temp and count<index:
            count += 1
            temp = temp.next
        temp.data = data

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([2,5,12,24,44,50])
    print(ll.display())
    print(ll.get_length())
    ll.update_at_beginning(1)
    print(ll.display())
    ll.update_at_end(55)
    print(ll.display())
    ll.update_at_index(3,22)
    print(ll.display())

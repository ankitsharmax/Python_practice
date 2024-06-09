queue = []
head = -1
tail = -1
N = int(input("Enter size of the queue: "))

def enqueue():
    global tail,head
    val = int(input("Enter value to enqueue: "))
    if tail == N-1:
        print("Overflow")
    elif tail == -1 and head == -1:
        queue.append(val)
        tail += 1
        head += 1
    else:
        tail += 1
        queue.append(val)

def dequeue():
    global tail, head
    if tail == -1 and head == -1:
        print("Underflow")
    elif tail == head:
        item = queue[head]
        tail = -1
        head = -1
        # print("Element dequeue: ",item)
    else:
        item = queue[head]
        head += 1
    print("Element dequeue: ",item)

def peek():
    global tail, head
    if head == -1 and tail == -1:
        print("Underflow")
    else:
        print("First Element: ",queue[head])

def display():
    global tail, head
    if head == -1 and tail == -1:
        print("Underflow")
    else:
        i = head
        res = '|'
        while i <= tail:
            res += str(queue[i]) + '|'
            i += 1
        print(res)

if __name__ == "__main__":
    enqueue()
    enqueue()
    display()
    peek()
    dequeue()
    display()
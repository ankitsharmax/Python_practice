top = -1
N = int(input("Enter length of stack: "))
arr = [0]*N
# arr = []

def push():
    global top
    x = int(input("Enter value to push: "))
    if top == N:
        return "Overflow"
    top += 1
    arr[top] = x
    # arr += x
    print(f"Pushed {x} in stack")

def pop():
    global top
    if top == -1:
        return "Underflow"
    item = arr[top]
    del(arr[top])
    top -= 1
    print(f"Pop {item} from stack")
    del(item)

def peek():
    global top
    if top == -1:
        return "Empty stack"
    print("Top of stack: ",arr[top])

def display():
    global top
    if top == -1:
        return "Empty stack"

    print("Stack: ",end="")
    for i in range(len(arr)):
        if arr[i] != 0:
            print(arr[i],end=" ")
    print()

if __name__ == '__main__':
    push()
    push()
    display()
    peek()
    pop()
    display()

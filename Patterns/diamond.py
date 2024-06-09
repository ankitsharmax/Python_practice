rows = 10
spaces = rows-1
for i in range(rows):
    for j in range(spaces):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    spaces -= 1
    print()

spaces = 0
for i in range(rows-1,0,-1):
    for j in range(spaces+1):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    spaces += 1
    print()

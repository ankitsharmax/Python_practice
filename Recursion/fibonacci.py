count = 0
def fibo(n):
    global count
    count += 1
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    # for i in range(5):
    #     print(fibo(i), end=' ')
    # print()
    print(fibo(5))
    print("Number of recusive calls: ", count)
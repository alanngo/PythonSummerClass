def collatz(n):
    cycleLen = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        cycleLen += 1
    return cycleLen


def main():
    for i in range(0, 101):
        print(str(i)+"::"+str(collatz(i)))


main()

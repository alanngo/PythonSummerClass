def collatz(n):
    cycleLen = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        cycleLen += 1
    return cycleLen


def generate_dictionary(n):
    ret = {}
    for x in range(0, n):
        ret[x] = x ** 2
    return ret


def main():
    # dependent: key
    # independent: value
    dictionary = generate_dictionary(100)
    print(dictionary)


main()

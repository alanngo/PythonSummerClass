def collatz(n):
    cycleLen = 1
    while n > 1:
        if n % 2 == 0:
            n = n >> 1
        else:
            n = n + (n << 1) + 1
        cycleLen += 1
    return cycleLen


def sum_numbers(array_list):
    sum = 0
    # for i in range(0, len(array_list)): naive
    #     sum += array_list[i]
    for i in array_list:
        sum += i
    return sum


def check_set(set, elem):
    return elem in set


cache = {}  # key n, value fib(n)


def fib(n):
    cache[0] = 0
    cache[1] = 1
    cache[2] = 1

    keys = cache.keys()

    if n in keys:
        return cache[n]
    else:
        cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

def t9(original):
    map = {
    'abc': '2',
    'def': '3',
    'ghi' : '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9',
    " ": '0'
    }
    string = ""
    for char in original:
        for str in map.keys():
            if char in str:
                char_num = map[str]
                string += char_num
                break
    return string

print(t9('alan'))
print(t9('alan loves neha'))


def main():
    # list []
    # tuple ()
    # set {}
    # dictionary {} key -> value relationship
    for i in range(0, 100):
        print(fib(i))


main()

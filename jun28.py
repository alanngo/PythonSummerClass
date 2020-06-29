# read from file and store in list
def read_file(file_name):
    ret = []

    # open file
    file = open(file_name, "r")

    # iterate thru file
    for line in file:
        ret.append(line.rstrip("\n"))

    # return a list representation
    file.close()
    return ret


# writes a list to a file
def write_file(file_name, lst):
    file = open(file_name, "w")
    for elem in lst:
        file.write(elem + "\n")
    file.close()


def file_io():
    print(read_file("food.txt"))
    write_file("names.txt", ["Angela", "Kevin", "Lyndon", "Smruti", "Josh", "Vince"])


cache = {}


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


def recursion():
    for i in range(0, 100):
        print(str(i) + " " + str(fib(i)))


def main():
    file_io()
    recursion()


main()

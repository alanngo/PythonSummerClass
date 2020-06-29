def list_food(file_name):
    ret = []
    file = open(file_name)
    for line in file:
        ret.append(line.rstrip("\n"))
    return ret


# basic syntax
file = open("food.txt")
for line in file:
    print(line.rstrip("\n"))
file.close()

print(list_food("food.txt"))
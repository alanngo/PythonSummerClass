def factorial(n):
    # n is our number
    if n == 0:
        return 1
    # compute factorial
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
    return fact


# addition and subtraction
# write a function that
# multiply 2 numbers WITHOUT using multiplication
# exponentiate without using exponentiateion

def abs_value(n):
    if n < 0:
        return -n
    if n > 0:
        return n
    return 0


def multiply(x, y):
    # edge case
    if x == 0 or y == 0:
        return 0
    product = 0
    # make sure you work w/ positive numbers
    posX = abs_value(x)
    posY = abs_value(y)
    for i in range(0, posY):
        product = product + posX

    # check negative cases
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return product
    if (x < 0 and y > 0) or (x > 0 and y < 0):
        return -product

    return product


def exp(x, n):
    # initial edge cases
    if n == 0:
        return 1
    if x == 0:
        return 0

    # make sure you work w/ positive numbers
    posX = abs_value(x)
    posN = abs_value(n)
    result = 1
    for i in range(0, posN):
        result = multiply(result, posX)
    ret = result

    # check negative  cases
    if x > 0 and n < 0:
        ret = 1 / result

    if x < 0 and n > 0:
        if n % 2 == 0:
            ret = result
        else:
            ret = -result

    if x < 0 and n < 0:
        if n % 2 == 0:
            ret = 1 / result
        else:
            ret = -1 / result
    return ret

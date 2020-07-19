def find_factors(x):  # find all the factors of x and return it in a list
    if x == 0:
        raise ValueError("indeterminite amounts ")
    if x < 0:
        x = -x
    ret = []
    if x == 1:
        ret.append(x)
        return ret
    for i in range(1, x+1):
        if x % i == 0:
            ret.append(i)
    return ret

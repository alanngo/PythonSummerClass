from assignment2.sandbox import *


def test_eq(actual, expected):
    if actual == expected:
        print("test passed")
    else:
        raise RuntimeError('TEST FAILED expected ' + str(expected) + ' got ' + str(actual))


def test_true(condition):
    if condition:
        print("test passed")
    else:
        raise RuntimeError('TEST FAILED')


def test_false(condition):
    if not condition:
        print("test passed")
    else:
        raise RuntimeError('TEST FAILED')


def main():
    test_eq(part0(1, 100), 5050)
    test_eq(part0(100, 1), 5050)
    test_eq(part0(1, 191), 18336)
    test_eq(part0(832, 928), 85360)
    test_eq(part0(398, 717), 178400)
    test_eq(part0(613, 963), 276588)
    test_eq(part0(23, 399), 79547)
    test_eq(part0(99, 734), 264894)
    test_eq(part0(3, 1), 6)

    test_true(part1(1024))
    test_true(part1(8))
    test_true(part1(2))
    test_true(part1(32))
    test_false(part1(0))
    test_false(part1(1))
    test_false(part1(355))
    test_false(part1(50))

    test_eq(part2(4), "IV")
    test_eq(part2(1), "I")
    test_eq(part2(150), "CL")
    test_eq(part2(999), "CMXCIX")
    test_eq(part2(70), "LXX")
    test_eq(part2(800), "DCCC")
    test_eq(part2(1000), "M")
    test_eq(part2(0), "")

    test_eq(part3("Alan"), 2526)
    test_eq(part3("cab"), 222)
    test_eq(part3("windows xp"), 9463697097)
    test_eq(part3("Phil sWift"), 7445079438)
    test_eq(part3("StrIx"), 78749)

    test_true(part4("paper", "title"))
    test_true(part4("mom", "dad"))
    test_false(part4("asus", "alan"))
    test_false(part4("ramen", "lobster"))

    test_true(part5("racecar"))
    test_true(part5("NOON"))
    test_false(part5("HanNAH"))
    test_false(part5("Devangi"))
    test_false(part5("Sodium"))

    test_eq(part6(5, 2), 10)
    test_eq(part6(32, 4), 35960)
    test_eq(part6(10, 0), 1)
    test_eq(part6(10, 250), -1)

    test_eq(part7(5, 2), 20)
    test_eq(part7(32, 4), 863040)
    test_eq(part7(10, 0), 1)
    test_eq(part7(10, 250), -1)

    print("ALL TESTS PASSED")


main()

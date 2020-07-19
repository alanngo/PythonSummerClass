from testing.Factors import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_factors0(self):  # testing 1
        expected = 1  # len of list
        actual = len(find_factors(1))
        self.assertEqual(expected, actual)

    def test_factors1(self):
        try:
            find_factors(0)
        except ValueError:
            self.assertTrue(True)

    def test_factors2(self):
        expected = 2  # len of list
        actual = len(find_factors(-2))
        self.assertEqual(expected, actual)

    def test_factors3(self):
        expected = 3  # len of list
        actual = len(find_factors(4))  # should give 1, 2, 4
        self.assertEqual(expected, actual)

    def test_factors4(self):
        expected = [1, 2, 3, 4, 6, 12]  # len of list
        actual = find_factors(12)  # should give 1, 2, 3 4, 6 12
        print(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

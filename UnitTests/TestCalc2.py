from unittest import *
from .Calculator import *


class PerfectEven(TestCase):
    # perfect even test cases
    def test_pe0(self):
        self.assertTrue(perfect_even(0))

    def test_pe1(self):
        self.assertTrue(perfect_even(2))

    def test_pe2(self):
        with self.assertRaises(ValueError):
            perfect_even(-1)

    def test_pe3(self):
        with self.assertRaises(ValueError):
            perfect_even(-128)

    def test_pe4(self):
        self.assertFalse(perfect_even(5))

    def test_pe5(self):
        self.assertFalse(perfect_even(42))


if __name__ == '__main__':
    main()

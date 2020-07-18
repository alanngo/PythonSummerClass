from unittest import *
from UnitTests.Calculator import *


# assertEquals(expected, actual): 2 variables are equal in content
# assertNotEquals(expected, actual): 2 variables are NOT equal in content
# assertTrue(condition): condition is true
# assertFalse(condition): condition is false
# assertRaises(SomeError): SomeError is expected
class Fib(TestCase):
    # fibonacci test cases
    def test_fib0(self):
        self.assertEqual(8, fib(6))

    def test_fib1(self):
        self.assertEqual(-1, fib(-1))

    def test_fib2(self):
        self.assertEqual(0, fib(0))

    def test_fib3(self):
        self.assertEqual(55, fib(10))


if __name__ == '__main__':
    main()

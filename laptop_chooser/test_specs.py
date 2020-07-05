import unittest
from laptop_chooser.specs import *


class MyTestCase(unittest.TestCase):
    def test_cpu(self):
        self.assertEqual(get_cpu("i7 9750h"), PERFORMANCE)

    def test_ram(self):
        self.assertEqual(get_ram(8), MAINSTREAM)

    def test_storage(self):
        self.assertEqual(get_storage(256), ENTRY_LEVEL)

    def test_gpu(self):
        self.assertEqual(get_gpu("1060"), MAINSTREAM)


if __name__ == '__main__':
    unittest.main()

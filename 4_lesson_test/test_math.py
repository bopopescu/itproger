import unittest
import math_file


class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(math_file.addition(5, 7), 12)
        self.assertEqual(math_file.addition(5, ), 9)
        self.assertEqual(math_file.addition(5, 7), 12)
        self.assertEqual(math_file.addition(), 5)


if __name__ == "__main__":
    unittest.main()

# test.py

import unittest
from main import get_remainder

class TestGetRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        """Тест для положительных чисел"""
        self.assertEqual(get_remainder(10, 3), 1)  # 10 % 3 = 1
        self.assertEqual(get_remainder(20, 5), 0)  # 20 % 5 = 0

    def test_negative_divisor(self):
        """Тест для отрицательного делителя"""
        self.assertEqual(get_remainder(10, -3), -2)  # 10 % -3 = -2
        self.assertEqual(get_remainder(20, -4), 0)   # 20 % -4 = 0

    def test_negative_dividend(self):
        """Тест для отрицательного числителя"""
        self.assertEqual(get_remainder(-10, 3), 2)   # -10 % 3 = 2
        self.assertEqual(get_remainder(-20, 7), 1)   # -20 % 7 = 1

    def test_division_by_one(self):
        """Тест для деления на 1 и -1"""
        self.assertEqual(get_remainder(10, 1), 0)   # 10 % 1 = 0
        self.assertEqual(get_remainder(10, -1), 0)  # 10 % -1 = 0

    def test_division_by_zero(self):
        """Тест для обработки деления на ноль"""
        with self.assertRaises(ValueError):
            get_remainder(10, 0)
        with self.assertRaises(ValueError):
            get_remainder(0, 0)

if __name__ == "__main__":
    unittest.main()
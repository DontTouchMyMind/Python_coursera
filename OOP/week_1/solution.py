import unittest


def factorize(x):
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(i=1):
            self.assertRaises(TypeError, factorize, 'string')
        with self.subTest(i=2):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        with self.subTest(i=1):
            self.assertRaises(ValueError, factorize, -1)
        with self.subTest(i=2):
            self.assertRaises(ValueError, factorize, -10)
        with self.subTest(i=3):
            self.assertRaises(ValueError, factorize, -100)

    def test_zero_and_one_cases(self):
        with self.subTest(i=1):
            self.assertEqual(factorize(0), (0, ))
        with self.subTest(i=2):
            self.assertEqual(factorize(1), (1, ))

    def test_simple_numbers(self):
        with self.subTest(i=1):
            self.assertEqual(factorize(3), (3, ))
        with self.subTest(i=2):
            self.assertEqual(factorize(13), (13, ))
        with self.subTest(i=3):
            self.assertEqual(factorize(29), (29, ))

    def test_two_simple_multipliers(self):
        with self.subTest(i=1):
            self.assertEqual(factorize(6), (2, 3))
        with self.subTest(i=2):
            self.assertEqual(factorize(26), (2, 13))
        with self.subTest(i=3):
            self.assertEqual(factorize(121), (11, 11))

    def test_many_multipliers(self):
        with self.subTest(i=1):
            self.assertEqual(factorize(1001), (7, 11, 13))
        with self.subTest(i=1):
            self.assertEqual(factorize(9699690), (2, 3, 5, 7, 11, 13, 17, 19))


# SOLUTION FROM TEACHER
# class TestFactorize(unittest.TestCase):
#     def test_wrong_types_raise_exception(self):
#         """ аргументы типа float или str вызывают исключение TypeError """
#         for x in 1.5, 'string':
#             with self.subTest(x=x):
#                 with self.assertRaises(TypeError):
#                     factorize(x)
#
#     def test_negative(self):
#         """ отрицательные числа вызывают исключение ValueError """
#         for x in -1, -10, -100:
#             with self.subTest(x=x):
#                 with self.assertRaises(ValueError):
#                     factorize(x)
#
#     def test_zero_and_one_cases(self):
#         """ целые чисела 0 и 1, возвращают кортежи (0,) и (1,) соответственно. """
#         for x in 0, 1:
#             with self.subTest(x=x):
#                 self.assertEqual(factorize(x), (x,))
#
#     def test_simple_numbers(self):
#         """ для простых чисел возвращается кортеж, содержащий одно данное число """
#         for x in 3, 13, 29:
#             with self.subTest(x=x):
#                 self.assertEqual(factorize(x), (x,))
#
#     def test_two_simple_multipliers(self):
#         """ числа для которых функция factorize возвращает кортеж размером 2 """
#         test_cases = (
#             (6, (2, 3)),
#             (26, (2, 13)),
#             (121, (11, 11)),
#         )
#         for x, expected in test_cases:
#             with self.subTest(x=x):
#                 self.assertEqual(factorize(x), expected)
#
#     def test_many_multipliers(self):
#         """ числа для которых функция factorize возвращает кортеж размером >2 """
#         test_cases = (
#             (1001, (7, 11, 13)),
#             (9699690, (2, 3, 5, 7, 11, 13, 17, 19)),
#         )
#         for x, expected in test_cases:
#             with self.subTest(x=x):
#                 self.assertEqual(factorize(x), expected)





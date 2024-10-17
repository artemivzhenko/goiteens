import unittest


def add_two_numbers(number_1, number_2):
    summary = number_1 * number_2
    return summary


class MyTestClass(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(2, 3), 5)


if __name__ == '__main__':
    unittest.main()

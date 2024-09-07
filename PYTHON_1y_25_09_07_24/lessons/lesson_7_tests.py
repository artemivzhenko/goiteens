import unittest


def add_two_numbers(number_1, number_2):
    summary = number_1 + number_2
    return summary


my_summary = add_two_numbers(90, 70)
print(my_summary)

my_summary_2 = add_two_numbers(340, 570)
print(my_summary_2)






# class MyTestClass(unittest.TestCase):
#
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(2, 3), 5)
#
#
# if __name__ == '__main__':
#     unittest.main()

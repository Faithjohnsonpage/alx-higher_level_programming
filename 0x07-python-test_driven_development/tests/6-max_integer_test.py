import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        list_1 = [1, 2, 3, 4, 5]
        max_no = max_integer(list_1)
        self.assertEqual(max_no, 5)

        list_2 = []
        max_no = max_integer(list_2)
        self.assertEqual(max_no, None)

        list_3 = [-1, 3, 5, 2]
        max_no = max_integer(list_3)
        self.assertEqual(max_no, 5)

        list_4 = [-2, -3, -6, -9, -1]
        max_no = max_integer(list_4)
        self.assertEqual(max_no, -1)

        list_5 = [1]
        max_no = max_integer(list_5)
        self.assertEqual(max_no, 1)

        list_6 = [1, 4, 5, 3, 2]
        max_no = max_integer(list_6)
        self.assertEqual(max_no, 5)

        list_7 = [7, 2, 3, 5, 6]
        max_no = max_integer(list_7)
        self.assertEqual(max_no, 7)

        list_8 = [-2, -2, -2, -2]
        max_no = max_integer(list_8)
        self.assertEqual(max_no, -2)

        list_9 = [0, 0, 0, 0]
        max_no = max_integer(list_9)
        self.assertEqual(max_no, 0)

        list_t = [100, 1000, 92, 550]
        max_no = max_integer(list_t)
        self.assertEqual(max_no, 1000)

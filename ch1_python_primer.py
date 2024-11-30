import re
import unittest
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint
Num = TypeVar('Num', int, float)


# R-1.1 is_multiple
def is_multiple(int1, int2):
    if int1 % int2 == 0:
        return True
    return False

# R-1.2 is_even
def is_even(k):
    if str(k)[-1] in {"0", "2", "4", "6", "8"}:
        return True
    return False

# R-1.3 minmax
def min_max(data: List[Num]) -> Tuple[Num, Num]:
    min_num = max_num = data[0] # initialize with the first element
    for num in data:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def sum_of_squares(n):
    total = 0
    for num in range(0, n):  # Starts at 0
        total += num ** 2
    return total

def sum_of_squares_better(n):
    return sum([i ** 2 for i in range(1, n)])

def sum_of_squares_worse(n):
    total = 0
    for num in range(1, n):
        if num % 2 == 1 and num > 0:
            total += num ** 2
    return total



class TestAdd(unittest.TestCase):
    def test_is_multiple(self):
        self.assertEqual(is_multiple(2, 3), False)
        self.assertEqual(is_multiple(4, 2), True)
        print(self)
    def test_is_even(self):
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(5), False)
        self.assertEqual(is_even(100), True)
        self.assertEqual(is_even(7), False)

    def test_min_max(self):
        self.assertEqual(min_max([2, 4, 6, 8, 10]), (2, 10))
        self.assertEqual(min_max([0, 4, 26, 8, -1]), (-1, 26))
        self.assertEqual(min_max([-1]), (-1, -1))

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(5), 30)
        self.assertEqual(sum_of_squares(20), 2470)
        print(self)

    def test_sum_of_squares_better(self):
        self.assertEqual(sum_of_squares_better(5), 30)
        self.assertEqual(sum_of_squares_better(20), 2470)

    def test_sum_of_squares_worse(self):
        self.assertEqual(sum_of_squares_worse(10), 165)




if __name__ == '__main__':
    unittest.main()

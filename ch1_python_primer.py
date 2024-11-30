import re
import unittest
from typing import List, TypeVar, Tuple, Any, Generator
from random import randrange, randint


# R-1.1 is_multiple
def is_multiple(int1, int2):
    if int1 % int2 == 0:
        return True
    return False


class TestAdd(unittest.TestCase):
    def test_is_multiple(self):
        self.assertEqual(is_multiple(2, 3), False)
        self.assertEqual(is_multiple(4, 2), True)
        print(self)


if __name__ == '__main__':
    unittest.main()

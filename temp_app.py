import unittest
from app import add,sub

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(3, 2), 1)
        self.assertEqual(sub(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
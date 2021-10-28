import unittest
from lab4.dijkstra import dijkstra


class MyTestCase(unittest.TestCase):
    def test_empty_dictionary(self):
        self.assertEqual(dijkstra({}, 0), {})

    def test_raise(self):
        self.assertRaises(ValueError, dijkstra, {1: [(2, 3)], 2: [(1, 3)]}, 4)


if __name__ == '__main__':
    unittest.main()

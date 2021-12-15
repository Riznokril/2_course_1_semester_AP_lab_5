import unittest
from tarjan import Graph

class TestHamster(unittest.TestCase):

    def test_case(self):
        g = Graph()
        g.read_data("tarjan_in_test.txt")
        self.assertEqual(g.tarjan(), [[3, 4, 5], [0, 2, 1]])

if __name__ == '__main__':
    unittest.main()

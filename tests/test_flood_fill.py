import unittest
from flood_fill import Solution

class TestFloodFill(unittest.TestCase):
    def test_example_1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        result = Solution().floodFill(image, 1, 1, 2)
        self.assertEqual(result, [[2,2,2],[2,2,0],[2,0,1]])

    def test_example_2(self):
        image = [[0,0,0],[0,0,0]]
        result = Solution().floodFill(image, 0, 0, 0)
        self.assertEqual(result, [[0,0,0],[0,0,0]])

if __name__ == "__main__":
    unittest.main()

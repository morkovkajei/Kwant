import unittest
from boxes import define
 
class TestDefineBoxes(unittest.TestCase):
 
    def test_upper(self):
        b1 = (2, 5, 9)
        b2 = (9, 2, 5)
        result = define(b1, b2)
        self.assertEqual(result, "equal")
 
 
    def test_b1(self):
        pairs = [((3, 5, 9), (9, 2, 5)),
                 ((2, 15, 10), (9, 2, 5)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "box1 bigger")
 
    def test_b2(self):
        pairs = [((9, 2, 5), (3, 5, 9)),
                 ((9, 2, 5), (2, 15, 10)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "box2 bigger")
 
 
    def test_incomparable(self):
        pairs = [((9, 3, 5), (2, 5, 10)),
                 ((9, 2, 5), (1, 15, 10)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "incomparable")
 
 
if __name__ == '__main__':
    unittest.main()

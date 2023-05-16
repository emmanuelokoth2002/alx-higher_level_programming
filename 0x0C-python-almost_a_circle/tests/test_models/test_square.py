import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_attributes(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')

    def test_update(self):
        s = Square(1, 2, 3, 4)
        s.update(5, 6, 7, 8)
        self.assertEqual(str(s), '[Square] (5) 7/8 - 6')

    def test_to_dict(self):
        s = Square(1, 2, 3, 4)
        d = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), d)

if __name__ == '__main__':
    unittest.main()


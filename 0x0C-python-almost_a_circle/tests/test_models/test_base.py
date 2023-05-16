import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 20, 5, 5)
        r1_dict = r1.to_dictionary()

        self.assertEqual(Base.to_json_string([r1_dict]), '[{"x": 5, "y": 5, "id": 1, "width": 10, "height": 20}]')

    def test_from_json_string(self):
        json_str = '[{"x": 5, "y": 5, "id": 1, "width": 10, "height": 20}]'
        json_list = Base.from_json_string(json_str)

        self.assertEqual(json_list, [{"x": 5, "y": 5, "id": 1, "width": 10, "height": 20}])

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 20, 5, 5)
        r2 = Rectangle(15, 25, 10, 10)
        s1 = Square(30, 15, 5)
        s2 = Square(40, 20, 10)

        Rectangle.save_to_file_csv([r1, r2])
        Square.save_to_file_csv([s1, s2])

        with open('Rectangle.csv', 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0], '1,10,20,5,5\n')
            self.assertEqual(lines[1], '2,15,25,10,10\n')

        with open('Square.csv', 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0], '1,30,15,5\n')
            self.assertEqual(lines[1], '2,40,20,10\n')

    def test_load_from_file_csv(self):
        r1 = Rectangle(10, 20, 5, 5)
        r2 = Rectangle(15, 25, 10, 10)
        s1 = Square(30, 15, 5)
        s2 = Square(40, 20, 10)

        Rectangle.save_to_file_csv([r1, r2])
        Square.save_to_file_csv([s1, s2])

        rectangles = Rectangle.load_from_file_csv()
        squares = Square.load_from_file_csv()

        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 20)
        self.assertEqual(rectangles[0].x, 5)
        self.assertEqual(rectangles[0].y, 5)

        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[1].size, 10)
        self.assertEqual(squares[1].x, 20)
        self.assertEqual(squares[1].y, 40)

if __name__ == '__main__':
    unittest.main()


import unittest
from models.base import Base
from models.rectangle import Rectangle

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.r1 = Rectangle(10, 7, 2, 8)

    def tearDown(self):
        pass

    def test_init_valid_values(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_to_json_string(self):
        dict_result = self.r1.to_dictionary()
        json_string = Base.to_json_string([dict_result])
        expected_result = '[{{"id": {}, "width": 10, "height": 7, "x": 2, "y": 8}}]'.format(self.r1.id)
        self.assertEqual(json_string, expected_result)
        

if __name__ == "__main__":
    unittest.main()

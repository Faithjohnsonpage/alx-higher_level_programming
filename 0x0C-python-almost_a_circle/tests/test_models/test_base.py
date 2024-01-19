import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()

    def tearDown(self):
        pass

    def test_init_valid_values(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

if __name__ == "__main__":
    unittest.main()

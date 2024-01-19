import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

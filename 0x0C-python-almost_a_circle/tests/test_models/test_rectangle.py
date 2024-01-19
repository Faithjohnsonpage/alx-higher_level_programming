import unittest
from models.rectangle import Rectangle
from unittest.mock import patch, Mock
import io


class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        # Create instances for testing
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(10, 2, 2, 1, 12)
        self.r3 = Rectangle(5, 5)
        self.r4 = Rectangle(1000, 2000, 500, 300, 999)
        self.r5 = Rectangle(1, 2, 4)
        self.r6 = Rectangle(1, 2, 3, 4)

    def tearDown(self):
        # Clean up resources if needed
        pass

    def test_init_valid_values(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertIsInstance(self.r1, Rectangle)

    def test_init_all_values_assigned(self):
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 12)
        self.assertIsInstance(self.r2, Rectangle)

    def test_init_equal_params(self):
        self.assertEqual(self.r3.width, self.r3.height)

    def test_init_large_values(self):
        self.assertEqual(self.r4.width, 1000)
        self.assertEqual(self.r4.height, 2000)
        self.assertEqual(self.r4.x, 500)
        self.assertEqual(self.r4.y, 300)
        self.assertEqual(self.r4.id, 999)

    def test_init_x_specified(self):
        self.assertEqual(self.r5.width, 1)
        self.assertEqual(self.r5.height, 2)
        self.assertEqual(self.r5.x, 4)
        self.assertEqual(self.r5.y, 0)

    def test_init_y_specified(self):
        self.assertEqual(self.r6.width, 1)
        self.assertEqual(self.r6.height, 2)
        self.assertEqual(self.r6.x, 3)
        self.assertEqual(self.r6.y, 4)

    def test_init_invalid_values(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, 'a')

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 6, '1')

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "string")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 4.4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 4)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -3)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 4, 1, -3)

    def test_width(self):
        self.r2.width = 1
        
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 12)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r2.width = -1

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r2.width = 0

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r2.width = '1'

    def test_x(self):
        self.r2.x = 1

        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 12)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r2.x = -1

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r2.x = '1'

    def test_y(self):
        self.r2.y = 5
        
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r2.id, 12)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r2.y = -1

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r2.y = '1'

    def test_height(self):
        self.r2.height = 1

        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 1)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 12)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r2.height = -1

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r2.height = 0

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r2.height = '1'


    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 25)
        self.assertEqual(self.r4.area(), 2000000)
        self.assertEqual(self.r5.area(), 2)

        self.r4.height = 3
        self.r4.width = 2
        self.assertEqual(self.r4.area(), 6)

    def test_str(self):
        self.assertEqual(str(self.r1), f"[Rectangle] ({self.r1.id}) 0/0 - 10/2")
        self.assertEqual(str(self.r2), f"[Rectangle] ({self.r2.id}) 2/1 - 10/2")
        self.assertEqual(str(self.r3), f"[Rectangle] ({self.r3.id}) 0/0 - 5/5")

    def test_display(self):
        # Case 1
        self.r7 = Rectangle(2, 1)
        expected_output1 = "##"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r7.display()

        actual_output1 = mock_stdout.getvalue().strip()
        self.assertEqual(actual_output1, expected_output1)

        # Case 2
        self.r8 = Rectangle(2, 1, 1)
        expected_output2 = " ##"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r8.display()

        actual_output2 = mock_stdout.getvalue().strip()
        self.assertIn(actual_output2, expected_output2)

        # Case 3
        self.r9 = Rectangle(2, 1, 1, 1)
        expected_output3 = "\n ##"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r9.display()

        actual_output3 = mock_stdout.getvalue().strip()
        self.assertIn(actual_output3, expected_output3)

    def test_update(self, *args, **kwargs):
        # Case 1
        self.r2.update(89)

        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 89)

        # Case 2
        self.r2.update(89, 2)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 89)

        # Case 3
        self.r2.update(89, 2, 3)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 89)

        # Case 4
        self.r2.update(89, 2, 3, 4)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 89)

        # Case 5
        self.r2.update(89, 2, 3, 4, 5)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r2.id, 89)


if __name__ == "__main__":
    unittest.main()

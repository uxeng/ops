# """Unit tests for the app module."""

# import unittest

# from sample.app import add_one


# class TestSimple(unittest.TestCase):
#     """Test cases for simple mathematical operations."""

#     def test_add_one(self) -> None:
#         """Test that add_one correctly increments a number by one."""
#         self.assertEqual(add_one(5), 6)


# if __name__ == "__main__":
#     unittest.main()



"""Unit tests for the app module."""

import unittest

from sample.app import add_one
from sample.app import hello_worlds


class TestSimple(unittest.TestCase):
    """Test cases for simple mathematical operations."""

    def test_generate_one(self) -> None:
        """Test that add_one correctly increments a number by one."""
        self.assertEqual(add_one(5), 6)

    def test_hello_worlds(self) -> None:
        """Test that add_one correctly increments a number by one."""
        hello_worlds_result: str = hello_worlds()
        self.assertEqual(type(hello_worlds_result), str)
        self.assertTrue(hello_worlds_result.startswith("<p>"))

if __name__ == "__main__":
    unittest.main()

"""Unit tests for the simple module."""

import unittest

from sample.app import add_one
from sample.app import get_tcp_port
from sample.app import hello_worlds


class TestSimpleApp(unittest.TestCase):
    """Test cases for the methods in simple.app module."""

    def test_get_tcp_port(self) -> None:
        """Test that the get_tcp_port method returns an int."""
        self.assertEqual(type(get_tcp_port(5)), int)

    def test_generate_one(self) -> None:
        """Test that the add_one method correctly increments a number by one."""
        self.assertEqual(add_one(5), 6)

    def test_hello_worlds(self) -> None:
        """Test that hello_worlds returns a string and that the string is formated as an html paragraph."""
        hello_worlds_result: str = hello_worlds()
        self.assertEqual(type(hello_worlds_result), str)
        self.assertTrue(hello_worlds_result.startswith("<p>") and hello_worlds_result.endswith("</p>"))

if __name__ == "__main__":
    unittest.main()

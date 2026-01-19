"""Unit tests for the sample.app module."""

import unittest

from sample.app import add_one
from sample.app import get_tcp_port
from sample.app import hello_worlds


class TestSampleApp(unittest.TestCase):
    """Test cases for the methods in sample.app module."""

    def test_add_one(self) -> None:
        """Test that the add_one method correctly increments a number by one."""
        self.assertEqual(add_one(5), 6)

    def test_get_tcp_port(self) -> None:
        """Test that the get_tcp_port method returns an int."""
        self.assertEqual(type(get_tcp_port()), int)

    def test_hello_worlds(self) -> None:
        """Test that hello_worlds returns a string formatted as an html paragraph."""
        hello_worlds_result: str = hello_worlds()
        self.assertEqual(type(hello_worlds_result), str)
        self.assertTrue(
            hello_worlds_result.startswith("<p>")
            and hello_worlds_result.endswith("</p>")
        )


if __name__ == "__main__":
    unittest.main()

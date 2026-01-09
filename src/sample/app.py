# """Application module providing basic mathematical operations."""


# def add_one(number: int) -> int:
#     """Add one to the given number.

#     Args:
#         number: The integer to increment.

#     Returns:
#         The input number incremented by one.

#     Example:
#         >>> add_one(5)
#         6
#     """
#     return number + 1


"""Application module providing basic mathematical operations."""

from flask import Flask
from random import random

def add_one(number: int) -> int:
    """Add one to the given number.

    Args:
        number: The integer to increment.

    Returns:
        The input number incremented by one.

    Example:
        >>> add_one(5)
        6
    """
    return number + 1


app = Flask(__name__)

@app.route("/")
def hello_worlds():
    """Constructs an html compatible string based on a friendly message and a random number
    
    Returns:
        the constructed string"""
    return "<p>Hello " + str(add_one(int(1000*random()))) +  " Worlds!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)



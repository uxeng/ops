"""Application module providing basic mathematical operations."""

import os
import logging
from random import random

import structlog

from flask import Flask


def set_some_info(_, __, event_dict):
    """Process structlog event dictionary to add some info.

    Args:
        _: First argument (unused, required by structlog processor signature)
        __: Second argument (unused, required by structlog processor signature)
        event_dict: Dictionary containing log event data

    Returns:
        Modified event dictionary with 'set_some_info' key added
    """
    event_dict["set_some_info"] = "some-info"
    return event_dict


log_level = os.environ.get("LOG_LEVEL", logging.INFO)


structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        set_some_info,
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(log_level),
)


logger = structlog.get_logger()


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

    # Log format reference:
    # %date{YYYY-MM-dd HH:mm:ss.SSS} %X{application} %X{url} %X{uuid}
    # %X{utility} thread="%thread" level="%-5level" className="%logger{36}.%M:%line"
    # %X{userId} %X{logChannel} %msg%n

    message: str = "abcdefg"
    logger.info(
        message,
        application="sample.app",
        utility="utility-12345",
        className=__name__,
        url="/",
        userid="user-123445",
        channel="http",
    )

    return "<p>Hello " + str(add_one(int(1000 * random()))) + " Worlds!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

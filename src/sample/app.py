"""Sample web application"""

import logging
import os
from random import random

from flask import Flask
from pythonjsonlogger import jsonlogger

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)

log_level = os.environ.get("LOG_LEVEL", logging.INFO)
logger.setLevel(log_level)


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


def get_tcp_port() -> int:
    """Gets the tcp port configuration from the environment.
    If the env var PYTHON_APP_TCP_PORT is not present the tcp port is set
    to the default value of 8080.

    Returns:
        The TCP port number as an integer.
    """
    tcp_port: int = 8080
    logger.info(
        "Checking the following environment variable: %s", "PYTHON_APP_TCP_PORT"
    )
    try:
        tcp_port: int = int(os.environ.get("PYTHON_APP_TCP_PORT", tcp_port))
    except ValueError:
        logger.error(
            "Could not parse PYTHON_APP_TCP_PORT env variable %s", exc_info=True
        )
    logger.info("Using the following TCP_PORT: %s", tcp_port)
    return tcp_port


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
        extra={
            "application": "sample.app",
            "utility": "utility-12345",
            "className": __name__,
            "url": "/",
            "userid": "user-123445",
            "channel": "http",
        },
    )

    return "<p>Hello " + str(add_one(int(1000 * random()))) + " Worlds!</p>"


if __name__ == "__main__":
    logger.info("Application starting")
    app.run(host="0.0.0.0", port=get_tcp_port())

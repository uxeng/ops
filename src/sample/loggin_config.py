import logging
import threading
import uuid
from datetime import datetime

# Thread-local storage for request context
_request_context = threading.local()


def set_request_context(
    request_id=None,
    user_id=None,
    url=None,
    channel=None
):
    _request_context.request_id = request_id or str(uuid.uuid4())
    _request_context.user_id = user_id or "-"
    _request_context.url = url or "-"
    _request_context.channel = channel or "-"


def get_request_context():
    return {
        "request_id": getattr(_request_context, "request_id", "-"),
        "user_id": getattr(_request_context, "user_id", "-"),
        "url": getattr(_request_context, "url", "-"),
        "channel": getattr(_request_context, "channel", "-"),
    }


class ContextFilter(logging.Filter):
    def __init__(self, app_name, utility):
        super().__init__()
        self.app_name = app_name
        self.utility = utility

    def filter(self, record):
        ctx = get_request_context()

        record.app_name = self.app_name
        record.utility = self.utility
        record.request_id = ctx["request_id"]
        record.user_id = ctx["user_id"]
        record.url = ctx["url"]
        record.channel = ctx["channel"]
        return True


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created)
        return dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def setup_logging(
    app_name="MyApp",
    utility="UtilityA",
    level=logging.INFO
):
    logger = logging.getLogger()
    logger.setLevel(level)

    handler = logging.StreamHandler()

    log_format = (
        "%(asctime)s | "
        "%(app_name)s | "
        "%(utility)s | "
        "%(levelname)s | "
        "%(threadName)s | "
        "%(request_id)s | "
        "%(user_id)s | "
        "%(url)s | "
        "%(channel)s | "
        "%(name)s.%(funcName)s:%(lineno)d | "
        "%(message)s"
    )

    formatter = CustomFormatter(log_format)
    handler.setFormatter(formatter)

    handler.addFilter(ContextFilter(app_name, utility))

    logger.addHandler(handler)

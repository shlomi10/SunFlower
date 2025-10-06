import logging
import os
import allure

LOG_DIR = "../logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "test_execution.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)


class AllureLoggerAdapter(logging.LoggerAdapter):
    """Logger adapter that sends messages to both log file and Allure report."""

    def process(self, msg, kwargs):
        # Attach to Allure as text step
        try:
            allure.attach(
                str(msg),
                name="log",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass
        return msg, kwargs


def get_logger(name: str) -> logging.Logger:
    """Return a logger instance that logs to file and Allure."""
    base_logger = logging.getLogger(name)
    return AllureLoggerAdapter(base_logger, {})

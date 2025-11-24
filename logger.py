import logging
import os
import colorlog


os.makedirs("logs", exist_ok=True)


logger = logging.getLogger("selenium_logger")
logger.setLevel(logging.DEBUG)

# -------- (Without colors) --------
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

# -------- (With colors)    --------
console_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s | " "%(message_log_color)s%(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    secondary_log_colors={
        "message": {
            "ERROR": "red",
            "CRITICAL": "bold_red",
            "WARNING": "yellow",
        }
    },
)

console_handler = colorlog.StreamHandler()
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.INFO)

# Añadir handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

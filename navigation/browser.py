from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from logger import logger

import os
from dotenv import load_dotenv

load_dotenv()

HEADLESS = os.getenv("HEADLESS", "True") == "True"
USER_AGENT = os.getenv("USER_AGENT")
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920,1080")


def create_driver(headless=HEADLESS):
    logger.info("Initializing Chrome WebDriver...")

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument(f"--window-size={WINDOW_SIZE}")
        options.add_argument(f"user-agent={USER_AGENT}")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    logger.info(f"Chrome WebDriver started (headless={headless}).")
    return driver

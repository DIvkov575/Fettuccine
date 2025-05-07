"""
Incomplete ...
requires user to submit login + enter 2fa code
"""
from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os

def login_and_save_state():
    load_dotenv()
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://distrokid.com/login")
        time.sleep(0.5)
        page.click(".signinWrapper")
        time.sleep(0.5)

        page.locator('input[placeholder="Email"][id *= Signin]').fill(email)
        page.locator('input[placeholder="Password"][id *= Signin]').fill(password)

        time.sleep(60)

        context.storage_state(path="auth.json")

        browser.close()

if __name__ == "__main__":
    login_and_save_state()

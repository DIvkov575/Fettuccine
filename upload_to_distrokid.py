from pathlib import Path
from playwright.sync_api import sync_playwright
import time
import os
import datetime

def upload_file(filename):
    # using pre authenticated session
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto("https://distrokid.com/new")

        page.locator("#chkapplemusic").uncheck()
        page.locator("#chkitunes").uncheck()
        page.locator("#chkfacebook").uncheck()
        page.locator("#chktiktok").uncheck()
        page.locator("#chkgoogle").uncheck()
        page.locator("#chkamazon").uncheck()
        page.locator("#chkrdio").uncheck()
        page.locator("#chkdeezer").uncheck()
        page.locator("#chktidal").uncheck()
        page.locator("#chkiheart").uncheck()
        page.locator("#chkimusica").uncheck()
        page.locator("#chksaavn").uncheck()
        page.locator("#chkboomplay").uncheck()
        page.locator("#chkanghami").uncheck()
        page.locator("#chknetease").uncheck()
        page.locator("#chktencent").uncheck()
        page.locator("#chkqobuz").uncheck()
        page.locator("#chkjoox").uncheck()
        page.locator("#chkkuackmedia").uncheck()
        page.locator("#chkfeedfm").uncheck()
        page.locator("#chkflo").uncheck()
        page.locator("#chkbeats").uncheck()
        page.locator("#chksnap").uncheck()
        page.locator("#chkroblox").uncheck()

        page.locator("#release-date-dp").fill(str(datetime.date.today())) # release date
        page.select_option("select#genrePrimary", value="24") # genre
        page.set_input_files("input#artwork", "art/cvart.jpg") # cover art
        page.fill('input[type="text"][placeholder="Track 1 title"]', str(Path(filename).name)) # title
        page.set_input_files("input#js-track-upload-1", filename) # track
        page.fill('input[type="text"][placeholder="First name"]', "Bartholomew")
        page.fill('input[type="text"][placeholder="Last name"]', "Phd")

        checkboxes = page.locator("div.upload-mobile-important-checkboxes input[type='checkbox']") # agreements
        count = checkboxes.count()
        for i in range(count):
            if checkboxes.nth(i).is_visible():
                checkboxes.nth(i).check(force=True)


        page.click('input[type="button"][id="doneButton"]')
        time.sleep(5)

        page.check('input[name="variant"][value="0"]')
        page.click('button.submit-button')
        time.sleep(4)

        browser.close()

if __name__ == "__main__":
    source_files = [file for file in Path("source").iterdir() if file.is_file() and file.suffix == '.mp3']
    for file in source_files:
        source_fname = Path("source") / (file.name)
        sink_fname = Path("sink") / (file.name)
        os.rename(source_fname, sink_fname)
        print(file.name)
        upload_file(sink_fname)






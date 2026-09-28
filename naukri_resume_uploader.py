import os
import time
from datetime import datetime

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

#============================================================
# CONFIGURATION
#============================================================

load_dotenv()

NAUKRI_URL = os.getenv(
"NAUKRI_URL",
"https://www.naukri.com/mnjuser/profile?id=&altresid"
)

RESUME_PATH = os.getenv("RESUME_PATH")

INTERVAL_MINUTES = int(
os.getenv("INTERVAL_MINUTES", "60")
)

TIMEOUT_MS = int(
os.getenv("TIMEOUT_MS", "30000")
)

BROWSER_PROFILE = os.getenv(
    "BROWSER_PROFILE",
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "naukri_browser_profile"
    )
)


#============================================================
# LOGGING
#============================================================

def log(message):
    """Print a timestamped log message."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")

#============================================================
# RESUME UPLOAD
#============================================================

def upload_resume(page):
    """Upload the configured resume to the Naukri profile."""

    log("Opening Naukri profile...")

    page.goto(
        NAUKRI_URL,
        wait_until="domcontentloaded",
        timeout=TIMEOUT_MS
    )

    # Allow dynamic page content to load.
    page.wait_for_timeout(3000)

    log("Looking for resume upload element...")

    file_input = page.locator("#attachCV")

    file_input.wait_for(
        state="attached",
        timeout=TIMEOUT_MS
    )

    log("Found resume upload element.")

    file_input.set_input_files(RESUME_PATH)

    log("Resume file selected.")

    update_button = page.locator(
        'input[type="button"][value="Update resume"]'
    )

    update_button.wait_for(
        state="visible",
        timeout=TIMEOUT_MS
    )

    log("Clicking 'Update resume'...")

    update_button.click()

    # Allow the website to process the upload.
    page.wait_for_timeout(5000)

    log("Upload/update request completed.")

    # Save a screenshot for verification.
    screenshot_name = os.path.join(
        "screenshots",
        f"upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    os.makedirs("screenshots", exist_ok=True)

    page.screenshot(
        path=screenshot_name,
        full_page=True
    )

    log(f"Screenshot saved: {screenshot_name}")

    return True

#============================================================
# MAIN
#============================================================

def main():

    if not RESUME_PATH:
        log("ERROR: RESUME_PATH is not configured.")
        log("Set RESUME_PATH in your .env file.")
        return

    if not os.path.isfile(RESUME_PATH):
        log("ERROR: Resume file was not found.")
        log(f"File path: {RESUME_PATH}")
        return

    if INTERVAL_MINUTES <= 0:
        log("ERROR: INTERVAL_MINUTES must be greater than zero.")
        return

    log("Naukri Resume Auto-Uploader started.")
    log(f"Resume: {RESUME_PATH}")
    log(f"Interval: {INTERVAL_MINUTES} minutes")

    with sync_playwright() as playwright:

        context = playwright.chromium.launch_persistent_context(
            user_data_dir=BROWSER_PROFILE,
            headless=False
        )

        page = (
            context.pages[0]
            if context.pages
            else context.new_page()
        )

        first_run = True

        try:

            while True:

                if not first_run:
                    log(
                        f"Waiting {INTERVAL_MINUTES} minutes "
                        "until the next upload..."
                    )

                    time.sleep(INTERVAL_MINUTES * 60)

                first_run = False

                try:

                    log("=" * 60)
                    log("Starting resume upload...")

                    upload_resume(page)

                    log("Upload cycle finished.")
                    log("=" * 60)

                except PlaywrightTimeoutError as error:

                    log(
                        "ERROR: Timed out while interacting "
                        "with Naukri."
                    )

                    log(str(error))

                    try:

                        os.makedirs("screenshots", exist_ok=True)

                        error_screenshot = os.path.join(
                            "screenshots",
                            (
                                f"error_"
                                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                                f".png"
                            )
                        )

                        page.screenshot(
                            path=error_screenshot,
                            full_page=True
                        )

                        log(
                            f"Error screenshot saved: "
                            f"{error_screenshot}"
                        )

                    except Exception:
                        pass

                except Exception as error:

                    log("ERROR during upload:")
                    log(str(error))

        except KeyboardInterrupt:

            log("Stopping automation...")

        finally:

            context.close()

            log("Browser closed.")
            log("Program stopped.")


if __name__ == "__main__":
    main()
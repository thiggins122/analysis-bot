from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# === LOGIN CREDENTIALS ===
EMAIL = "thiggins@manta.com"
PASSWORD = "iiYFWsWBFDh9X!j"
TARGET_URL = "https://app.insites.com/en_US/keyword-planner/d51365a4c7d7bdcf0e7ccfc3ae93a99b1c01b1eb"

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print("🔐 Logging in...")
    driver.get("https://app.insites.com/")
    time.sleep(3)

    login_link = driver.find_element(By.LINK_TEXT, "Log in")
    login_link.click()
    time.sleep(2)

    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(EMAIL)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    print("📄 Navigating to planner...")
    driver.get(TARGET_URL)
    time.sleep(5)

    print("⚙️ Clicking generate...")
    generate_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate keyword suggestions')]")
    generate_btn.click()

    print("✅ Done!")

    time.sleep(3)
finally:
    driver.quit()

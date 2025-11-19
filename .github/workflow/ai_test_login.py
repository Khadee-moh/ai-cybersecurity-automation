import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def run_ai_login_test():
    print("=== AI Login Test Started ===")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://example.com/login")
        time.sleep(3)

        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("admin")
        password.send_keys("password123")
        login_btn.click()

        time.sleep(3)
        print("Login test completed successfully!")

    except NoSuchElementException as e:
        print("❌ Element not found:", e)

    except Exception as e:
        print("❌ Login test failed:", e)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_ai_login_test()

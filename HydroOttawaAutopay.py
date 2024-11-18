from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HydroOttawaLoginPayBot:
    def __init__(self, email, password, account_number):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        self.account_number = account_number

    def wait_for_element(self, xpath):
        try:
            # Wait for up to 10 seconds for the element to be present in the DOM
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            print("Element found!")
            print("ID:", element.get_attribute("id"))
            print("Name:", element.get_attribute("name"))
            print("Value:", element.get_attribute("value"))
        except Exception as e:
            print("Element not found:", e)

    def wait_for_element_with_ID(self, id):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
            print("ID:", element.get_attribute("id"))
            print("Name:", element.get_attribute("name"))
            print("Value:", element.get_attribute("value"))
        except Exception as e:
            print("Element not found:", e)

    def open_login_page(self):
        self.driver.get("https://account.hydroottawa.com/login")
        self.driver.implicitly_wait(5)

    def enter_credentials(self):
        self.driver.find_element(By.ID, "EmailAddress").send_keys(self.email)
        self.driver.find_element(By.ID, "LoginPassword").send_keys(self.password)

    def submit_login(self):
        self.driver.find_element(By.ID, "LoginSubmitButton").click()

    def pay_now(self):
        self.driver.find_element(By.ID, "PaynowButton").click()

        self.wait_for_element_with_ID("header.accountNumber")

    def close_browser(self):
        time.sleep(5)
        self.driver.quit()

    def run(self):
        self.open_login_page()
        self.enter_credentials()
        self.submit_login()
        self.pay_now()
        time.sleep(5)
        self.close_browser()


if __name__ == "__main__":
    email = ""
    password = ""
    account_number = ""
    login_bot = HydroOttawaLoginPayBot(email, password, account_number)
    login_bot.run()

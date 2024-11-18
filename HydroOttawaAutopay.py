from selenium import webdriver
import os
import tools
import time
from dotenv import load_dotenv


class HydroOttawaLoginPayBot:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("HYDRO_OTTAWA_PASSWORD")
        self.driver = webdriver.Chrome()
        self.account_number = os.getenv("HYDRO_OTTAWA_ACCOUNT_NUMBER")

    def open_login_page(self):
        self.driver.get("https://account.hydroottawa.com/login")
        self.driver.implicitly_wait(5)

    def enter_credentials(self):
        tools.wait_for_element_with_ID(self.driver, "EmailAddress")
        tools.wait_for_element_with_ID(self.driver, "LoginPassword")
        self.driver.find_element(By.ID, "EmailAddress").send_keys(self.email)
        self.driver.find_element(By.ID, "LoginPassword").send_keys(self.password)

    def submit_login(self):
        self.driver.find_element(By.ID, "LoginSubmitButton").click()

    def pay_now(self):
        tools.wait_for_element_with_ID(self.driver, "PaynowButton")
        self.driver.find_element(By.ID, "PaynowButton").click()

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
    load_dotenv()
    login_bot = HydroOttawaLoginPayBot()
    login_bot.run()

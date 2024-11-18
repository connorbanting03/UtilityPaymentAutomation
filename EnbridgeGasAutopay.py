from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EnbridgeGasPayBot:
    def __init__(self, account_number, postal_code):
        self.driver = webdriver.Chrome()
        self.account_number = account_number
        self.postal_code = postal_code

    def open_login_page(self):
        self.driver.get("https://ez-pay.ca/Validate.aspx?billerid=p8kpaTvbk1")
        self.driver.implicitly_wait(5)

    def populate_login(self):
        self.driver.find_element(By.ID, "ctl00_BodyPlaceholder_CUSTNO").send_keys(
            self.account_number
        )
        self.driver.find_element(By.ID, "ctl00_BodyPlaceholder_SOLDTO6").send_keys(
            self.postal_code
        )
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(
            EC.element_to_be_clickable((By.ID, "ctl00_BodyPlaceholder_btnLookUp"))
        )
        button.click()


if __name__ == "__main__":
    account_number = ""
    postal_code = ""
    login_bot = EnbridgeGasPayBot(account_number, postal_code)
    login_bot.open_login_page()
    login_bot.populate_login()
    time.sleep(10)


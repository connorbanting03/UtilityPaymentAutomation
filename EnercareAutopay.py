from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class EnercarePayBot:
    def __init__(self, email, password, card_number, card_name):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        self.card_number = card_number
        self.card_name = card_name

    def open_login_page(self):
        self.driver.get(
            "https://cxselfserveprd.b2clogin.com/cxselfserveprd.onmicrosoft.com/b2c_1a_my_account_signin_relying_party_policy/oauth2/v2.0/authorize?client_id=cb335abb-0001-4742-a0e3-bbfb9d3a606c&scope=openid%20email%20profile%20offline_access&response_type=code&redirect_uri=https%3A%2F%2Fmyaccount.enercare.ca%2Fapi%2Fauth%2Fcallback%2Fsignin&response_mode=form_post&code_challenge_method=S256&state=3YVVn55KoNTkuOvCpXGQlZRbbAwqagXuVICdaR7zEZc&code_challenge=j9qCqvgFOHDdHmGrgRHKdO6pOqM3IUcfUTmwTLacM54&nonce=pNuZ_jasmPaH_V5l2r25I1BpsbbRfbg-EW5PNT_Rj2I"
        )
        self.driver.implicitly_wait(5)

    def sign_in(self):
        self.driver.find_element(By.ID, "signInName").send_keys(self.email)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        self.driver.find_element(By.ID, "next").click()

    def pay_bill(self):
        time.sleep(10)
        self.driver.get("https://mybilling.enercare.ca/s/make-a-payment?idx=0")
       

       

    def run(self):
        self.open_login_page()
        self.sign_in()
        self.pay_bill()
        time.sleep(1000)


if __name__ == "__main__":
    email = ""
    password = ""
    card_name = ""
    card_number = ""

    login_bot = EnercarePayBot(email, password, card_number, card_name)
    login_bot.run()


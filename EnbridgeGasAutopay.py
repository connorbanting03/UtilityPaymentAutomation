from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tools
import os
from dotenv import load_dotenv


class EnbridgeGasPayBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.account_number = os.getenv("ENBRIDGEGAS_ACCOUNTNUMBER")
        self.postal_code = os.getenv("POSTAL_CODE")

    def open_login_page(self):
        self.driver.get("https://ez-pay.ca/Validate.aspx?billerid=p8kpaTvbk1")
        self.driver.implicitly_wait(5)

    def populate_login(self):
        tools.wait_for_element_with_ID(self.driver, "ctl00_BodyPlaceholder_CUSTNO")
        self.driver.find_element(By.ID, "ctl00_BodyPlaceholder_CUSTNO").send_keys(
            self.account_number
        )
        tools.wait_for_element_with_ID(self.driver, "ctl00_BodyPlaceholder_CUSTNO")
        self.driver.find_element(By.ID, "ctl00_BodyPlaceholder_SOLDTO6").send_keys(
            self.postal_code
        )
        time.sleep(5)

       
                

    def run(self):
        self.open_login_page()
        self.populate_login()


if __name__ == "__main__":
    load_dotenv()
    login_bot = EnbridgeGasPayBot()
    login_bot.run()
    time.sleep(10)


#<input type="submit" name="ctl00$BodyPlaceholder$btnLookUp" value="Look Up" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$BodyPlaceholder$btnLookUp&quot;, &quot;&quot;, true, &quot;OTPValidationGrp&quot;, &quot;&quot;, false, false))" id="ctl00_BodyPlaceholder_btnLookUp" class="button next w-inline-block" style="border-style:None;">
#<a id="ctl00_BodyPlaceholder_btnBack" href="#" class="button back w-inline-block" onclick="javascript:window.history.back(); return false;" onkeypress="javascript:window.history.back(); return false;" style="visibility: hidden">Back</a>
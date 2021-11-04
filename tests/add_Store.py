import pytest
import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from pages.store_Page import LoginShopify
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker



class addStore(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://www.shopify.com/partners"

        # image
        file_csv = "C:\\Users\\PC\\Pictures\\products_export.csv"
        # Name
        fake = Faker()
        name = fake.name()
        content = fake.paragraphs()
        email = 'hoangvidct2@gmail.com'
        password = 'vole132465798'
        # for x in range(0,200):
        #     # name_store = "test-store-dev-" + rnd_value +"-"+ time_str
        #     name_store = "store-dev-ar"+ str(x)
        
        store_Page = LoginShopify(driver)
        
        driver.get(url)
        driver.maximize_window()
            
        store_Page.login_page()

        store_Page.set_fill_email(email)

        sleep(3)

        store_Page.click_btn_next()

        sleep(2)

        store_Page.set_fill_password(password)

        sleep(2)

        store_Page.click_btn_log_in()

        sleep(2)

        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(1, 200):
            for n in range(500, 600):
                # name_store = "test-store-dev-" + rnd_value +"-"+ time_str
                city = fake.city()
                zipcode = fake.zipcode()
                # time_str = str(round(time.time() * 1000))
                today = datetime.now()
                name_store = "vileh store "+ str(n)

                pass_store = 1

                time_str = today.strftime("%d%m%Y%H%M%S")

                rnd_value = str(random.randint(1, 10000))


                rnd_add = str(random.randint(1,300))
                address = fake.street_address()

                store_Page.go_to_store()

                sleep(2)

                store_Page.add_new_store()

                # shopify_page.add_new_store()

                sleep(2)

                store_Page.select_mode()
                
                sleep(2)

                store_Page.set_store_name(name_store)

                sleep(5)

                store_Page.set_passwpord(password)

                sleep(2)

                store_Page.set_confirm_password(password)

                sleep(2)
                
                store_Page.set_address(address)

                store_Page.set_city(city)

                store_Page.set_zip_code(zipcode)

                sleep(2)

                store_Page.select_save_btn()

                sleep(15)

                # # store_Page.select_product_btn()

                # # sleep(3)

                # # store_Page.select_import_btn()

                # # store_Page.click_import_btn(file_csv)

                # # sleep(10)

                # store_Page.select_store_online_btn()

                # sleep(10)

                # store_Page.select_change_pass_btn()

                # sleep(7)

                # store_Page.set_pass_store(pass_store)

                # sleep(5)

                # store_Page.select_save_pass()

                # sleep(5)

                driver.get(url)
                sleep(3)
                store_Page.login_page()

     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



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
from pages.order_Page import createOrder
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker



class addOrder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://store-vile-11.myshopify.com/collections/all"
        # url = "https://store-vile-11.myshopify.com/46107132053/checkouts/16dc72b2fdeb10ef698b27c140d3fa4e?previous_step=shipping_method&step=payment_method"
        # Name
        fake = Faker()
        name = fake.name()
        email = fake.ascii_free_email()
        content = fake.paragraphs()
        firstname = fake.first_name()
        lastname = fake.last_name()
        address = fake.street_address()
        city = fake.city()
        postalcode = "550000"

        # Phone
        rnd_value = str(random.randint(1000, 9000)) 
        phone = "+1201555"+ rnd_value
        # mail = fake.email()
        name_phone = [email, phone]

        # Card 
        number = 1
        namecard = "card test"
        month = 11
        year = 22
        code = 112

        order_Page = createOrder(driver)

        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(0, 50):
            driver.get(url)
            driver.maximize_window()
            order_Page.click_select_product_3_btn()
            order_Page.click_buy_now()
            order_Page.set_fill_name_phone(random.choice(name_phone))
            order_Page.set_fill_first_name(firstname)
            order_Page.set_fill_last_name(lastname)
            order_Page.set_fill_adress(address)
            order_Page.set_fill_city(city)
            order_Page.set_fill_postal_code(postalcode)
            order_Page.click_next_btn()
            order_Page.click_next_btn()
            # driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@title="Field container for: Card number"]'))
            order_Page.set_fill_number_card(number)
            order_Page.set_fill_name_card(namecard)
            order_Page.set_fill_expiry_card(month, year)
            order_Page.set_fill_security_card(code)
            order_Page.click_next_btn()
            sleep(5)
     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



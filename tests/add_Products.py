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
from pages.products_Page import addProducts
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker



class createProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://store-billing-01.myshopify.com/admin"
        # url = "https://store-vile-11.myshopify.com/46107132053/checkouts/16dc72b2fdeb10ef698b27c140d3fa4e?previous_step=shipping_method&step=payment_method"
        # Name
        fake = Faker()
        name = fake.name()
        email_fake = fake.ascii_free_email()
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
        name_phone = [email_fake, phone]
        
        # image
        image_1 = "C:\\Users\\PC\\Pictures\\image\\1.jpg"
        image_2 = "C:\\Users\\PC\\Pictures\\image\\2.jpg"
        image_3 = "C:\\Users\\PC\\Pictures\\image\\3.jpg"
        image_4 = "C:\\Users\\PC\\Pictures\\image\\4.jpg"
        image_5 = "C:\\Users\\PC\\Pictures\\image\\5.jpg"
        image_6 = "C:\\Users\\PC\\Pictures\\image\\6.jpg"
        image_7 = "C:\\Users\\PC\\Pictures\\image\\7.jpg"
        image_8 = "C:\\Users\\PC\\Pictures\\image\\8.jpg"
        image_9 = "C:\\Users\\PC\\Pictures\\image\\9.jpg"
        image_10 = "C:\\Users\\PC\\Pictures\\image\\10.jpg"
        image_11 = "C:\\Users\\PC\\Pictures\\image\\11.jpg"
        image_12 = "C:\\Users\\PC\\Pictures\\image\\12.jpg"
        image_13 = "C:\\Users\\PC\\Pictures\\image\\13.jpg"
        image_14 = "C:\\Users\\PC\\Pictures\\image\\14.jpg"
        image_15 = "C:\\Users\\PC\\Pictures\\image\\15.jpg"

        choice_image = [image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, image_10, image_11, image_12, image_13, image_14, image_15, ]

        # Account
        email = "alireview.extension@fireapps.vn"
        password = "123321"
        today = datetime.now()
        # time_str = today.strftime("%d%m%H%M%S")
        # product_name = "Product" + "-" + time_str
        # product_price = str(random.randint(1000000,99999999))
        # product_quantity = str(random.randint(1000,9000))
        product_type = ['Sport', 'Normal', 'Man', 'Women']

        products_Page = addProducts(driver)
        driver.get(url)
        driver.maximize_window()
        products_Page.set_fill_email_shopify(email)
        products_Page.click_next_btn_shopify()
        products_Page.set_fill_pass_shopify(password)
        products_Page.click_login_btn_shopify()
        sleep(2)
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(0, 500):

            today = datetime.now()
            time_str = today.strftime("%d%m%H%M%S")
            product_name = "Product" + "-" + time_str
            product_price = str(random.randint(1000000,7000000))
            product_quantity = str(random.randint(1000,9000))
            products_Page.click_product_btn_shopify()
            sleep(2)
            products_Page.click_add_product_btn_shopify()
            products_Page.set_fill_product_name_shopify(product_name)
            sleep(2)
            products_Page.set_add_photo_product(random.choice(choice_image))
            sleep(2)
            products_Page.set_fill_product_price_shopify(product_price)
            sleep(2)
            products_Page.set_fill_product_quantity_shopify(product_quantity)
            sleep(2)
            products_Page.set_fill_product_type_shopify(random.choice(product_type))
            products_Page.click_save_product_btn_shopify()
            sleep(3)
            driver.get(url)
     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



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
from pages.judge_Page import addReviewJudge
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker



class importReviewsJudge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://vileh-store.myshopify.com/admin"



        # Account
        email = "hoangvidct1@gmail.com"
        password = "vole132465798"
        url_1 = "https://www.aliexpress.com/item/33026237232.html"
        url_2 = "https://www.aliexpress.com/item/32848249257.html"
        url_3 = "https://www.aliexpress.com/item/4000470566385.html"
        url_4 = "https://www.aliexpress.com/item/4000183536923.html"
        url_5 = "https://www.aliexpress.com/item/32924395212.html"
        url_6 = "https://www.aliexpress.com/item/32975685695.html"

        product_url = [url_1, url_2, url_3, url_4, url_5, url_6]

        product_1 = "Product-0109182922"
        product_2 = "Product-0109183027"
        product_3 = "Product-0109183005"
        product_4 = "Product-0109183109"
        product_5 = "Product-0109183047"
        product_6 = "Product-0109183237"
        product_7 = "Product-0109183258"
        product_8 = "Product-0109183321"

        product_name = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8]

        number = 500
        # time_str = today.strftime("%d%m%H%M%S")
        # product_name = "Product" + "-" + time_str
        # product_price = str(random.randint(1000000,99999999))
        # product_quantity = str(random.randint(1000,9000))

        judge_Page = addReviewJudge(driver)
        driver.get(url)
        driver.maximize_window()
        judge_Page.set_fill_email_shopify(email)
        judge_Page.click_next_btn_shopify()
        judge_Page.set_fill_pass_shopify(password)
        judge_Page.click_login_btn_shopify()
        sleep(2)
        judge_Page.click_apps_btn_shopify()
        judge_Page.click_judge_import()
        sleep(10)
        judge_Page.click_import_button()
        sleep(5)
        # judge_Page.set_fill_product_url(random.choice(product_url))
        judge_Page.set_fill_product_url(random.choice(product_name), number)

        judge_Page.uncheck_checkbox_mail()
        judge_Page.click_import_review_judge()

        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(0, 10):
            url_1 = "https://www.aliexpress.com/item/33026237232.html"
            url_2 = "https://www.aliexpress.com/item/32848249257.html"
            url_3 = "https://www.aliexpress.com/item/4000470566385.html"
            url_4 = "https://www.aliexpress.com/item/4000183536923.html"
            url_5 = "https://www.aliexpress.com/item/32924395212.html"
            url_6 = "https://www.aliexpress.com/item/32975685695.html"

            product_url = [url_1, url_2, url_3, url_4, url_5, url_6]

            product_1 = "Product-0109182922"
            product_2 = "Product-0109183027"
            product_3 = "Product-0109183005"
            product_4 = "Product-0109183109"
            product_5 = "Product-0109183047"
            product_6 = "Product-0109183237"
            product_7 = "Product-0109183258"
            product_8 = "Product-0109183321"

            product_name = [product_1, product_2, product_3, product_4, product_5, product_6, product_7, product_8]

            # Code

            judge_Page.click_continue_import()
            judge_Page.set_fill_product_url(random.choice(product_url))
            judge_Page.set_fill_product_name(random.choice(product_name))
            judge_Page.click_import_review_judge()


     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



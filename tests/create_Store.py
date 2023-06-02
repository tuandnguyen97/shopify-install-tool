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
from pages.createStoreMCMA import CreateTrialstore
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker
import pandas as pd
import openpyxl
import xlwt
from xlsxwriter import Workbook
import xlsxwriter 


class CreateStoretrial(unittest.TestCase):

 
    def setUp(self):
        print("==============[Start Test]============")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self) -> None:
        return super().tearDown()
        time.sleep(2)


    def testcase_1(self):


        #URL
        driver = self.driver
        url = "https://shopify.com/"
        # url = "https://apps.shopify.com/"

        # CREATE STORE
        createStoreMCMA = CreateTrialstore(driver)

        for i in range(0, 19):
            
            # Fake data
            fake = Faker()

            # Name store
            name = fake.name()
            firstname = fake.first_name()
            lastname = fake.last_name()        
            time_str = str(round(time.time() * 1000))
            rnd_value = str(random.randint(1, 10000))
            st1 = name + " " + time_str
            st2 = firstname + lastname
            st3 = firstname + " " + rnd_value
            st4 = firstname + " " + time_str
            st5 = lastname + " " + time_str
            st6 = lastname + " " + rnd_value
            store_name = [st1, st2, st3, st4, st5]

            # Password
            password = 'password@12345'
            keyword_1 = 'flash sale'
            keyword_2 = 'FLASH SALE'
            keyword_3 = 'Flash Sale'
            key_word = [keyword_1, keyword_2, keyword_3]

            # Email
            email = fake.ascii_free_email()

            #Steps
            driver.get(url)
            driver.maximize_window()
            createStoreMCMA.create_trial_btn()
            createStoreMCMA.click_skip_btn()
            # createStoreMCMA.click_next_btn_1()
            # createStoreMCMA.click_next_btn_1()
            # createStoreMCMA.fill_store_name(random.choices(store_name))
            # createStoreMCMA.click_next_btn_2()
            createStoreMCMA.click_next_btn_3()
            createStoreMCMA.click_email_continue_btn()
            createStoreMCMA.fill_email(email)
            createStoreMCMA.fill_pass(password)
            createStoreMCMA.click_create_shopify_id_btn()
            createStoreMCMA.click_add_apps_btn()
            createStoreMCMA.click_shopify_apps_store_btn()
            driver.switch_to.window(driver.window_handles[1])
            createStoreMCMA.fill_keyword(random.choices(key_word))
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
            sleep(5)
            # createStoreMCMA.click_page_btn()
            createStoreMCMA.click_select_app_install()
            createStoreMCMA.click_app_shopify()
            createStoreMCMA.click_install_app_shopify()
            sleep(5)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])



        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
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
from pages.createStoreMCMA import CreateTrialstore as CT
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker

class CreateStoretrial(unittest.TestCase):

 
    def setUp(self):
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

        # Fake data
        fake = Faker()
        name = fake.name()
        time_str = str(round(time.time() * 1000))
        storename = name + time_str
        content = fake.paragraphs()
        email = fake.ascii_free_email()
        password = '123321'
        keyword = 'flash'


        #URL
        driver = self.driver
        url = "https://shopify.com/"

        # CREATE STORE
        steps = CT(driver)
        driver.get(url)
        driver.maximize_window()
        steps.create_trial_btn()
        steps.click_next_btn_1()
        steps.click_next_btn_1()
        steps.click_next_btn_1()
        steps.fill_store_name(storename)
        steps.click_next_btn_2()
        steps.click_next_btn_3()
        steps.click_email_continue_btn()
        steps.fill_email(email)
        steps.fill_pass(password)
        steps.click_create_shopify_id_btn()
        steps.click_add_apps_btn()
        steps.click_shopify_apps_store_btn()
        driver.switch_to.window(driver.window_handles[1])
        steps.fill_keyword(keyword)



       



           
        # Fake data
        # fake = Faker()
        # name = fake.name()
        # content = fake.paragraphs()
        # email = fake.ascii_free_email()
        # password = '123321'


        # def tearDown(self):
        #     self.driver.quit()
        #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
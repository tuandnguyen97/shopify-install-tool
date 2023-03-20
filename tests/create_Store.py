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
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):

        # Fake data
        fake = Faker()
        name = fake.name()
        time_str = str(round(time.time() * 1000))
        storename = name + time_str
        content = fake.paragraphs()
        email = fake.ascii_free_email()
        password = '123321'


        #URL
        driver = self.driver
        url = "https://shopify.com/"

        # CREATE STORE
        steps = CT(driver)
        driver.get(url)
        driver.maximize_window()
        sleep(5) 
        steps.create_trial_btn()
        sleep(5)
        steps.click_next_btn()
        sleep(5)
        steps.click_next_btn()
        sleep(5)
        steps.click_next_btn()
        sleep(5)
        steps.fill_store_name(storename)
        sleep(15)
       



           
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
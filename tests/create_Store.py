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

        # Email
        email = fake.ascii_free_email()

        # Password
        password = '123321'
        keyword_1 = 'flash'
        keyword_2 = 'FLASH'
        keyword_3 = 'Flash'
        key_word = [keyword_1, keyword_2, keyword_3]

        #URL
        driver = self.driver
        # url = "https://shopify.com/"
        url = "https://apps.shopify.com/"

        # CREATE STORE
        for i in range(0, 10):
            steps = CT(driver)
            driver.get(url)
            driver.maximize_window()
            # steps.create_trial_btn()
            # steps.click_next_btn_1()
            # steps.click_next_btn_1()
            # steps.click_next_btn_1()
            # steps.fill_store_name(random.choices(store_name))
            # steps.click_next_btn_2()
            # steps.click_next_btn_3()
            # steps.click_email_continue_btn()
            # steps.fill_email(email)
            # steps.fill_pass(password)
            # steps.click_create_shopify_id_btn()
            # steps.click_add_apps_btn()
            # steps.click_shopify_apps_store_btn()
            # driver.switch_to.window(driver.window_handles[1])
            steps.fill_keyword(random.choices(key_word))
            # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            # driver.execute_script("window.scrollTo(0, window.scrollY + 1440)")
            # sleep(5)
            # steps.click_page_btn()
            # steps.click_select_app_install()
            # steps.click_app_shopify()
            # steps.click_install_app_shopify()




        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
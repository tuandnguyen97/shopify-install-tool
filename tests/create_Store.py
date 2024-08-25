import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
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
from datetime import datetime

# import pandas as pd
# import openpyxl
# import xlwt
# from xlsxwriter import Workbook
# import xlsxwriter 


class CreateStoretrial(unittest.TestCase):
    # def setUp(self):
        # print("==============[Start Test]============")
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('excludeSwitches', ['enable-logging'])  
        # option.add_argument("start-maximized")
        # option.add_argument("--incognito")
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
        # # self.geckodriver_autoinstaller.install()
        # # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        # self.driver.implicitly_wait(30)
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def tearDown(self) -> None:
        return super().tearDown()
        time.sleep(2)

    def testcase_1(self):
        #URL
        # driver = self.driver
        # url = "https://shopify.com/"
        # # url = "https://apps.shopify.com/"

        # # CREATE STORE
        # createStoreMCMA = CreateTrialstore(driver)
        # driver.get(url)
        # driver.delete_all_cookies()

        for i in range(0, 19):
            print("==============[Start Test]============")
            option = webdriver.ChromeOptions()
            option.add_experimental_option('excludeSwitches', ['enable-logging'])  
            option.add_argument("start-maximized")
            option.add_argument("--incognito")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
            # self.geckodriver_autoinstaller.install()
            # self.driver = webdriver.Firefox(GeckoDriverManager().install())
            self.driver.implicitly_wait(30)
            self.verificationErrors = []
            self.accept_next_alert = True
            driver = self.driver
            url = "https://shopify.com/"
            # url = "https://apps.shopify.com/"

            # CREATE STORE
            createStoreMCMA = CreateTrialstore(driver)
            driver.get(url)
            driver.delete_all_cookies()
            
            print(f"step 1")

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
            password = 'password@12345678'
            keyword_1 = 'flash sale'
            keyword_2 = 'FLASH SALE'
            keyword_3 = 'Flash Sale'
            key_word = [keyword_1, keyword_2, keyword_3]

            # Email
            email = fake.ascii_free_email()
            value_email_1 = firstname + lastname + time_str + "@" + "gmail.com"
            value_email_2 = firstname + time_str + "@" + "gmail.com"
            value_email_3 = lastname + time_str + "@" + "gmail.com"
            value_email_4 = firstname + lastname + time_str + "@" + "hotmail.com"
            value_email_5 = firstname + time_str + "@" + "hotmail.com"
            value_email_6 = lastname + time_str + "@" + "hotmail.com"
            value_email_7 = firstname + lastname + time_str + "@" + "yahoo.com"
            value_email_8 = firstname + time_str + "@" + "yahoo.com"
            value_email_9 = lastname + time_str + "@" + "yahoo.com"
            value_email_10 = firstname + lastname + time_str + "@" + "yopmail.com"
            value_email_11 = firstname + time_str + "@" + "yopmail.com"
            value_email_12 = lastname + time_str + "@" + "yopmail.com"
            value_email = [value_email_1, value_email_2, value_email_3, value_email_4, value_email_5, value_email_6, value_email_7, value_email_8, value_email_9, value_email_10, value_email_11, value_email_12]

            print(f"step 2")

            #Steps
            # driver.maximize_window()
            createStoreMCMA.create_trial_btn()
            print(f"step 3")

            try:
                createStoreMCMA.click_skip_all_btn()
                print(f"step 4")
                createStoreMCMA.click_next_btn_1()
            except Exception as err:
                print(f"err button email")
            # createStoreMCMA.click_next_btn_1()
            # createStoreMCMA.click_next_btn_1()
            # createStoreMCMA.fill_store_name(random.choices(store_name))
            # createStoreMCMA.click_next_btn_2()
            print(f"step 5")

            createStoreMCMA.click_email_continue_btn()
            print(f"step 6")
            createStoreMCMA.fill_email(random.choices(value_email))
            print(f"step 7")
            createStoreMCMA.fill_pass(password)
            print(f"step 8")
            createStoreMCMA.click_create_shopify_id_btn()
            print(f"step 9")
            is_exits_click_add_apps_btn = createStoreMCMA.is_exits_click_add_apps_btn()
            is_exits_click_skip_help = False
            is_exits_click_email_continue_btn = False
            if is_exits_click_add_apps_btn == False:
                is_exits_click_skip_help = createStoreMCMA.is_exits_click_skip_help()
                if is_exits_click_skip_help == False:
                    is_exits_click_email_continue_btn = True

            print(f"step 9.0.1")
            # is_exits_click_skip_help = createStoreMCMA.is_exits_click_skip_help()
            print(f"step 9.0.2")
            # is_exits_click_email_continue_btn = createStoreMCMA.is_exits_click_email_continue_btn()
            print(f"step 9.0.3")

            if is_exits_click_add_apps_btn:
                print(f"step 9.1")
                createStoreMCMA.click_add_apps_btn()
            elif is_exits_click_skip_help:
                print(f"step 9.2")
                createStoreMCMA.click_skip_help()
                createStoreMCMA.click_add_apps_btn()
            elif is_exits_click_email_continue_btn:
                print(f"step 9.3")
                createStoreMCMA.click_email_continue_btn()
                createStoreMCMA.fill_email(random.choices(value_email))
                createStoreMCMA.fill_pass(password)
                createStoreMCMA.click_create_shopify_id_btn()
                try:
                    createStoreMCMA.click_add_apps_btn()
                except Exception as err:
                    createStoreMCMA.click_skip_help()
                    print(f"step 9.4")
                    createStoreMCMA.click_add_apps_btn()
                    print(f"err button click_add_apps_btn")
            print(f"step 10")
            createStoreMCMA.click_shopify_apps_store_btn()
            print(f"step 11")
            # driver.switch_to.window(driver.window_handles[1])
            self.driver.switch_to.window(self.driver.window_handles[1])
            print(f"step 12")
            createStoreMCMA.fill_keyword(random.choices(key_word))
            print(f"step 13")
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print(f"step 14")
            driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
            print(f"step 15")
            sleep(5)
            # createStoreMCMA.click_page_btn()
            createStoreMCMA.click_select_app_install()
            print(f"step 16")
            createStoreMCMA.click_app_shopify()
            print(f"step 17")
            self.driver.switch_to.window(self.driver.window_handles[2])
            print(f"step 18")
            sleep(5)
            createStoreMCMA.click_install_app_shopify()
            print(f"step 19")
            sleep(5)
            self.driver.close()
            print(f"step 20")
            self.driver.switch_to.window(self.driver.window_handles[1])
            print(f"step 21")
            self.driver.close()
            print(f"step 22")
            self.driver.switch_to.window(self.driver.window_handles[0])
            print(f"step 23")
            driver.delete_all_cookies()
            print(f"step 24")
            driver.get(url)
            print(f"step 25")
            self.driver.quit()

        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
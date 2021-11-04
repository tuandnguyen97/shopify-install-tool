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
from pages.reviewbox_Page import checkReviewbox
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep
from faker import Faker



class checkReview(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(2)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://alireviews.fireapps.io/install"
        product_url = "https://store-billing-10.myshopify.com/products/product-0109190742"
        store_admin = "https://store-billing-10.myshopify.com/admin"

        store_name = "store-billing-10"
        store_email = "alireview.extension@fireapps.vn"
        store_pass = "123321"
        csv_file = "C:\\Users\\PC\\Desktop\\alireviews_import_template.csv"

        reviewbox_Page = checkReviewbox(driver)

        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(0, 1):

            driver.get(url)
            driver.maximize_window()
            reviewbox_Page.set_fill_store_name(store_name)
            reviewbox_Page.click_login_btn()
            reviewbox_Page.set_fill_store_email(store_email)
            reviewbox_Page.click_next_btn()
            reviewbox_Page.set_fill_store_pass(store_pass)
            reviewbox_Page.click_login_btn_shopify()
            reviewbox_Page.click_install_app_btn()
            reviewbox_Page.click_choose_plan_btn()
            reviewbox_Page.click_start_free_trial_btn()
            driver.refresh()
            reviewbox_Page.click_get_review_btn()
            reviewbox_Page.click_review_btn()
            reviewbox_Page.click_import_review()
            reviewbox_Page.select_csv_file_btn()
            reviewbox_Page.set_add_csv_file(csv_file)
            reviewbox_Page.click_go_to_settings_btn()
            reviewbox_Page.click_import_reviews()
            reviewbox_Page.click_view_product()
            driver.switch_to.window(driver.window_handles[1])
            driver.execute_script("window.scrollTo(0, window.scrollY + 700)")
            sleep(15) 
            driver.switch_to.window(driver.window_handles[0])
            reviewbox_Page.select_delete_review()
            # Select(driver.find_element_by_xpath("//*[@id='product-item-5797444845735']/td[4]/div/select")).select_by_value('deleteAllReviewsModal')
            reviewbox_Page.click_delete_reviews()
            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[2])
            driver.get(store_admin)
            reviewbox_Page.click_apps()
            reviewbox_Page.click_apps()
            reviewbox_Page.select_delete_app()
            reviewbox_Page.select_delete_app_confirm()
            sleep(5)

     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()



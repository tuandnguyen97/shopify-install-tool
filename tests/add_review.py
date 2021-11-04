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
from pages.review_Page import writeReview
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from faker import Faker



class addReview(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.geckodriver_autoinstaller.install()
        # self.driver = webdriver.Firefox(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testcase_1(self):
        driver = self.driver
        url = "https://store-vile-11.myshopify.com/products/product-0109175402"

        # image
        image_1 = "C:\\Users\\PC\\Downloads\\anh-gif-dong-dep_054757287.gif"
        image_2 = "C:\\Users\\PC\\Downloads\\image1.png"
        choice_image = [image_1, image_2]

        # Name
        fake = Faker()
        name = fake.name()
        email = fake.ascii_free_email()
        content = fake.paragraphs()
        
        review_Page = writeReview(driver)

        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        for i in range(0, 10):
            fake = Faker()
            name = fake.name()
            email = fake.ascii_free_email()
            content = fake.paragraphs()

            
            driver.get(url)
            driver.maximize_window()
            sleep(4)
            review_Page.click_write_review_btn()
            sleep(5)
            review_Page.set_fill_review()
            sleep(2)
            review_Page.set_fill_name(name)
            sleep(2)
            review_Page.set_fill_email(email)
            sleep(2)
            review_Page.set_fill_content(content)
            sleep(2)
            # review_Page.set_add_photo(random.choice(choice_image))
            # sleep(2)
            review_Page.click_add_review_btn()
            sleep(5)
     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



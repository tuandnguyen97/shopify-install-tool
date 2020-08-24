from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from pages.locators import *

class writeReview:
    URL = "https://thinhtest100.myshopify.com/products/test-1"

    btn_write_review = (By.XPATH, WRITE_REVIEW_BTN_CLASS)
    fill_name = (By.ID, FILL_NAME_ID)
    fill_email = (By.ID, FILL_EMAIL_ID)
    fill_content = (By.ID, FILL_CONTENT_ID)
    add_photo = (By.XPATH, ADD_PHOTO_BTN_XPATH)
    btn_add_review = (By.ID, ADD_REVIEW_BTN_ID)

    # Setup driver
    def __init__(self,driver):
        self.driver = driver
    

    # Write Review
    def click_write_review_btn(self):
        btn_write_review = self.driver.find_element(*self.btn_write_review)
        btn_write_review.click()

    def set_fill_name(self, name):
        fill_name = self.driver.find_element(*self.fill_name)
        fill_name.send_keys(name)

    def set_fill_email(self, mail):
        fill_email = self.driver.find_element(*self.fill_email)
        fill_email.send_keys(mail)

    def set_fill_content(self, content):
        fill_content = self.driver.find_element(*self.fill_content)
        fill_content.send_keys(content)

    def set_add_photo(self, photo):
        add_photo = self.driver.find_element(*self.add_photo)
        add_photo.send_keys(photo)

    def click_add_review_btn(self):
        btn_add_review = self.driver.find_element(*self.btn_add_review)
        btn_add_review.click()

    
    # Element
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
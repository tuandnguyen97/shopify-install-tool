from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from Locator.locators import *

class addProducts:

    fill_email_shopify = (By.XPATH, FILL_EMAIL_SHOPIFY_XPATH)
    btn_next_shopify = (By.XPATH, NEXT_BTN_SHOPIFY_XPATH)
    fill_pasword_shopify = (By.XPATH, FILL_PASSWORD_SHOPIFY_XPATH)
    btn_login_shopify = (By.XPATH, LOGIN_BTN_SHOIFY_XPATH)
    btn_product_shopify = (By.XPATH, PRODUCT_BTN_XPATH)
    btn_add_product_shopify = (By.XPATH, ADD_PRODUCT_BTN_XPATH)
    fill_name_product_shopify = (By.XPATH, FILL_PRODUCT_NAME_XPATH)
    fill_price_product_shopify = (By.XPATH, FILL_PRICE_PRODUCT_XPATH)
    fill_quantity_product_shopify = (By.XPATH, FILL_QUANTITY_PRODUCT_XPATH)
    fill_type_product_shopify = (By.XPATH, FILL_TYPE_PRODUCT_XPATH)
    add_photo_product = (By.XPATH, ADD_PHOTO_PRODUCT_XPATH)
    btn_save_product_shopify = (By.XPATH, SAVE_PRODUCT_BTN_XPATH)


    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # Write Review

    def set_fill_email_shopify(self, email):
        fill_email_shopify = self.driver.find_element(*self.fill_email_shopify)
        fill_email_shopify.send_keys(email)

    def click_next_btn_shopify(self):
        btn_next_shopify = self.driver.find_element(*self.btn_next_shopify)
        btn_next_shopify.click()

    def set_fill_pass_shopify(self, password):
        fill_pasword_shopify = self.driver.find_element(*self.fill_pasword_shopify)
        fill_pasword_shopify.send_keys(password)

    def click_login_btn_shopify(self):
        btn_login_shopify = self.driver.find_element(*self.btn_login_shopify)
        btn_login_shopify.click()

    def click_product_btn_shopify(self):
        btn_product_shopify = self.driver.find_element(*self.btn_product_shopify)
        btn_product_shopify.click()

    def click_add_product_btn_shopify(self):
        btn_add_product_shopify = self.driver.find_element(*self.btn_add_product_shopify)
        btn_add_product_shopify.click()

    def set_fill_product_name_shopify(self, product):
        fill_name_product_shopify = self.driver.find_element(*self.fill_name_product_shopify)
        fill_name_product_shopify.send_keys(product)

    def set_fill_product_price_shopify(self, price):
        fill_price_product_shopify = self.driver.find_element(*self.fill_price_product_shopify)
        fill_price_product_shopify.send_keys(price)

    def set_fill_product_quantity_shopify(self, quantity):
        fill_quantity_product_shopify = self.driver.find_element(*self.fill_quantity_product_shopify)
        fill_quantity_product_shopify.send_keys(quantity)

    def set_fill_product_type_shopify(self, product_type):
        fill_type_product_shopify = self.driver.find_element(*self.fill_type_product_shopify)
        fill_type_product_shopify.send_keys(product_type)

    def set_add_photo_product(self, photo):
        add_photo_product = self.driver.find_element(*self.add_photo_product)
        add_photo_product.send_keys(photo)

    def click_save_product_btn_shopify(self):
        btn_save_product_shopify = self.driver.find_element(*self.btn_save_product_shopify)
        btn_save_product_shopify.click()

    # def set_fill_content(self, content):
    #     fill_content = self.driver.find_element(*self.fill_content)
    #     fill_content.send_keys(content)

    # def set_add_photo(self, photo):
    #     add_photo = self.driver.find_element(*self.add_photo)
    #     add_photo.send_keys(photo)

    # def click_add_review_btn(self):
    #     btn_add_review = self.driver.find_element(*self.btn_add_review)
    #     btn_add_review.click()

    
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
    
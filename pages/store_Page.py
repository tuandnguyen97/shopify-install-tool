from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from Locators.locators import *

class LoginShopify:

    btn_log_in = (By.XPATH, LOG_IN_BTN_XPATH)
    fill_email = (By.XPATH, FILL_EMAIL_XPATH)
    btn_next = (By.XPATH, BTN_NEXT_XPATH)
    fill_pass = (By.XPATH, FILL_PASS_XPATH)
    login_btn = (By.XPATH, BTN_LOGIN_XPATH)
    store_page = (By.XPATH, STORE_PAGE_XPATH)
    btn_add = (By.XPATH, BTN_ADD_STORE_XPATH)
    btn_select_dev = (By.XPATH, BTN_SELECT_DEV_STORE_XPATH)
    fill_store_name = (By.XPATH, FILL_STORE_NAME_XPATH)
    fill_pass_store = (By.XPATH, FILL_PASS_STORE_XPATH)
    fill_confirm_pass_store = (By.XPATH, FILL_CONFIRM_PASS_STORE_XPATH)
    fill_address = (By.XPATH, FILL_ADDRESS_XPATH)
    fill_city = (By.XPATH, FILL_CITY_XPATH)
    fill_zipcode = (By.XPATH, FILL_ZIPCODE_XPATH)
    btn_save_app = (By.XPATH, BTN_SAVE_XPATH)
    btn_product_app = (By.XPATH, BTN_PRODUCT_XPATH)
    btn_import_app = (By.XPATH, BTN_IMPORT_REVIEW_XPATH)
    btn_select_file = (By.XPATH, BTN_SELECT_FILE_XPATH)
    btn_select_store_link = (By.XPATH, BTN_STORE_XPATH)
    btn_select_change_pass = (By.XPATH, BTN_CHANGE_PASS_XPATH)
    btn_fill_pass = (By.XPATH, BTN_FILL_PASS_XPATH)
    btn_save_pass = (By.XPATH, BTN_SAVE_PASS_XPATH)
    iframe_store = (By.XPATH, IFRAME_FILL_PASS_XPATH)




    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(driver):
    #     driver.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # Login Shopify Partner
    def login_page(self):
        btn_log_in = self.driver.find_element(*self.btn_log_in)
        btn_log_in.click()

    def set_fill_email(self,email):
        
        fill_email = self.driver.find_element(*self.fill_email)
        fill_email.send_keys(email)

    def click_btn_next(self):
        btn_next = self.driver.find_element(*self.btn_next)
        btn_next.click()

    def set_fill_password(self,password):
        
        fill_pass = self.driver.find_element(*self.fill_pass)
        fill_pass.send_keys(password)

    def click_btn_log_in(self):
        login_btn = self.driver.find_element(*self.login_btn)
        login_btn.click()

    def go_to_store(self):
        store_page = self.driver.find_element(*self.store_page)
        store_page.click()
    
    def add_new_store(self):
        btn_add = self.driver.find_element(*self.btn_add)
        btn_add.click()

    def select_mode(self):
        btn_select_dev = self.driver.find_element(*self.btn_select_dev)
        btn_select_dev.click()

    def set_store_name(self, name):
       fill_store_name = self.driver.find_element(*self.fill_store_name)
       fill_store_name.send_keys(name)

    def set_passwpord(self,password):
        fill_pass_store = self.driver.find_element(*self.fill_pass_store)
        fill_pass_store.send_keys(password)

    def set_confirm_password(self,password):
        fill_confirm_pass_store = self.driver.find_element(*self.fill_confirm_pass_store)
        fill_confirm_pass_store.send_keys(password)

    def set_address(self, address):
        fill_address = self.driver.find_element(*self.fill_address)
        fill_address.send_keys(Keys.CONTROL, "a")
        fill_address.send_keys(Keys.DELETE)
        sleep(1)
        fill_address.send_keys(address)

    def set_city(self,city):
        fill_city = self.driver.find_element(*self.fill_city)
        fill_city.send_keys(Keys.CONTROL, "a")
        fill_city.send_keys(Keys.DELETE)
        sleep(1)
        fill_city.send_keys(city)

    def set_zip_code(self,zipcode):
        fill_zipcode = self.driver.find_element(*self.fill_zipcode)
        fill_zipcode.send_keys(Keys.CONTROL, "a")
        fill_zipcode.send_keys(Keys.DELETE)
        sleep(1)
        fill_zipcode.send_keys(zipcode)

    def select_save_btn(self):
        btn_save_app = self.driver.find_element(*self.btn_save_app)
        btn_save_app.click()

    def select_product_btn(self):
        btn_product_app = self.driver.find_element(*self.btn_product_app)
        btn_product_app.click()

    def select_import_btn(self):
        btn_import_app = self.driver.find_element(*self.btn_import_app)
        btn_import_app.click()

    def click_import_btn(self, file):
        btn_select_file = self.driver.find_element(*self.btn_select_file)
        btn_select_file.send_keys(file)

    def select_store_online_btn(self):
        btn_select_store_link = self.driver.find_element(*self.btn_select_store_link)
        btn_select_store_link.click()
    
    def select_change_pass_btn(self):
        btn_select_change_pass = self.driver.find_element(*self.btn_select_change_pass)
        btn_select_change_pass.click()   

    def set_pass_store(self,pass_store):
        iframe_store = self.driver.find_element(*self.iframe_store)
        self.driver.switch_to.frame(iframe_store)
        btn_fill_pass = self.driver.find_element(*self.btn_fill_pass)
        btn_fill_pass.send_keys(Keys.CONTROL, "a")
        btn_fill_pass.send_keys(Keys.DELETE)
        sleep(1)
        btn_fill_pass.send_keys(pass_store)
        self.driver.switch_to.parent_frame()


    def select_save_pass(self):
        btn_save_pass = self.driver.find_element(*self.btn_save_pass)
        btn_save_pass.click()   

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
    
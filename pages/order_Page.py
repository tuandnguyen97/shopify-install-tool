from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import random
from Locator.locators import *

class createOrder:
    randomNumber = random.randint(1, 32)


    # btn_product_1 = (By.XPATH, '//*[@id="Collection"]/ul[1]/li["+str(randomNumber)+"]/div/a')
    btn_product = (By.XPATH, '//*[@id="Collection"]/ul[1]/li['+str(randomNumber)+']/div/a')
    btn_buy_it_now_btn = (By.XPATH, BUY_IT_NOW_BTN_XPATH)
    fill_name_phone = (By.XPATH, FILL_EMAIL_PHONE_XPATH)
    fill_first_name = (By.XPATH, FILL_FIRST_NAME_XPATH)
    fill_last_name = (By.XPATH, FILL_LAST_NAME_XPATH)
    fill_address = (By.XPATH, FILL_ADDRESS_XPATH)
    fill_city = (By.XPATH, FILL_CITY_XPATH)
    fill_postal_code= (By.XPATH, FILL_POSTAL_CODE_XPATH)
    btn_next = (By.XPATH, NEXT_BUTTON_XPATH)
    fill_number_card = (By.XPATH, NUMBER_CARD_XPATH)
    fill_name_card = (By.XPATH, NAME_CARD_XPATH)
    fill_expiry_card = (By.XPATH, EXPIRY_CARD_XPATH)
    fill_security_card = (By.XPATH, SECURITY_CARD_XPATH)
    iframe_card_number = (By.XPATH, IFRAME_REGISTER_CARD_NUMBER)
    iframe_card_name = (By.XPATH, IFRAME_REGISTER_CARD_NAME)
    iframe_card_expiry = (By.XPATH, IFRAME_REGISTER_CARD_EXPIRY)
    iframe_card_security = (By.XPATH, IFRAME_REGISTER_CARD_SECURITY)


    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # create Order
    def click_select_product_btn(self):
        randomNumber = random.randint(1, 8)
        btn_product = self.driver.find_element(By.XPATH, '//*[@id="Collection"]/ul[1]/li['+str(randomNumber)+']/div/a')
        btn_product.click()
        sleep(2)

    def click_buy_now(self):
        btn_buy_it_now_btn = self.driver.find_element(*self.btn_buy_it_now_btn)
        btn_buy_it_now_btn.click()
        sleep(2)

    def click_next_btn(self):
        btn_next = self.driver.find_element(*self.btn_next)
        btn_next.click()
        sleep(2)

    def set_fill_name_phone(self, phone):
        fill_name_phone = self.driver.find_element(*self.fill_name_phone)
        fill_name_phone.send_keys(phone)

    def set_fill_first_name(self, firstname):
        fill_first_name = self.driver.find_element(*self.fill_first_name)
        fill_first_name.send_keys(firstname)

    def set_fill_last_name(self, lastname):
        fill_last_name = self.driver.find_element(*self.fill_last_name)
        fill_last_name.send_keys(lastname)

    def set_fill_adress(self, address):
        fill_address = self.driver.find_element(*self.fill_address)
        fill_address.send_keys(address)

    def set_fill_city(self, city):
        fill_city = self.driver.find_element(*self.fill_city)
        fill_city.send_keys(city)

    def set_fill_postal_code(self, postalcode):
        fill_postal_code = self.driver.find_element(*self.fill_postal_code)
        fill_postal_code.send_keys(postalcode)

    # def switch_frame_card_number(self):
    #     iframe_card_number = self.driver.find_element(*self.iframe_card_number)
    #     self.driver.switch_to.frame(iframe_card_number)

    def set_fill_number_card(self, numbercard):
        iframe_card_number = self.driver.find_element(*self.iframe_card_number)
        self.driver.switch_to.frame(iframe_card_number)
        fill_number_card = self.driver.find_element(*self.fill_number_card)
        fill_number_card.send_keys(numbercard)
        self.driver.switch_to.parent_frame()

    def set_fill_name_card(self, namecard):
        iframe_card_name = self.driver.find_element(*self.iframe_card_name)
        self.driver.switch_to.frame(iframe_card_name)
        fill_name_card = self.driver.find_element(*self.fill_name_card)
        fill_name_card.send_keys(namecard)
        self.driver.switch_to.parent_frame()

    def set_fill_expiry_card(self, month, year):
        iframe_card_expiry = self.driver.find_element(*self.iframe_card_expiry)
        self.driver.switch_to.frame(iframe_card_expiry)
        fill_expiry_card = self.driver.find_element(*self.fill_expiry_card)
        fill_expiry_card.send_keys(month)
        fill_expiry_card.send_keys(year)
        self.driver.switch_to.parent_frame()

    def set_fill_security_card(self, code):
        iframe_card_security = self.driver.find_element(*self.iframe_card_security)
        self.driver.switch_to.frame(iframe_card_security)
        fill_security_card = self.driver.find_element(*self.fill_security_card)
        fill_security_card.send_keys(code)
        sleep(1)
        self.driver.switch_to.parent_frame()

    
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
    
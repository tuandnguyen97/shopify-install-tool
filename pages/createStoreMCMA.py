from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
from Locators.createStore_MCMA_locator import *
from selenium.webdriver.support import expected_conditions as EC



class CreateTrialstore:
    btn_create_trial = (By.XPATH, CREATE_START_TRIAL_BTN)
    btn_skip = (By.XPATH, SKIP_BTN)
    btn_next = (By.XPATH, NEXT_BTN_1)
    input_store_name = (By.XPATH, INPUT_STORE_NAME)
    btn_continue_email = (By.XPATH, CONTINUE_WITH_EMAIL_BTN)
    input_email = (By.XPATH, INPUT_EMAIL)
    input_pass = (By.XPATH, INPUT_PASS)
    btn_create_store = (By.XPATH, CREATE_STORE_BTN)


    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(driver):
    #     driver.maximize_window()

    def load(self,driver):
        self.driver.get(self.URL)

    # CREATE TRIAL STORE
    def create_trial_btn(self):
        btn_create_trial = self.driver.find_element(*self.btn_create_trial)
        btn_create_trial.click()

    def click_skip_btn(self):
        btn_skip = self.driver.find_element(*self.btn_skip)
        btn_skip.click()

    def click_next_btn(self):
        btn_next = self.driver.find_element(*self.btn_next)
        btn_next.click()


    def fill_store_name(self,storename):
        input_store_name = self.driver.find_element(*self.input_store_name)
        input_store_name.click()
        sleep(2)
        input_store_name.send_keys(storename)

    



from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import random
from pages.locators import *

class checkReviewbox:

    fill_name_store = (By.XPATH, FILL_STORE_NAME_XPATH)
    btn_login = (By.XPATH, LOGIN_BTN_AR_APP_XPATH)
    fill_email_shopify = (By.XPATH, FILL_EMAIL_SHOPIFY_XPATH)
    btn_next_shopify = (By.XPATH, NEXT_BTN_SHOPIFY_XPATH)
    fill_pasword_shopify = (By.XPATH, FILL_PASSWORD_SHOPIFY_XPATH)
    btn_login_shopify = (By.XPATH, LOGIN_BTN_SHOIFY_XPATH)
    btn_install_app = (By.XPATH, INSTALL_APP_BTN_XPATH)
    btn_choose_premium_plan = (By.XPATH, PREMIUM_BTN_XPATH)
    btn_start_trial = (By.XPATH, START_TRIAL_BTN_XPATH)
    # btn_close_trial = (By.XPATH, BTN_CLOSE_XPATH)
    click_get_review = (By.XPATH, REVIEW_BTN_XPATH)
    review_btn = (By.XPATH, IMPORT_REVIEW_TAB_XPATH)
    import_review_product = (By.XPATH, IMPORT_REVIEW_PRODUCT_XPATH)
    select_csv_file = (By.XPATH, SELECT_CSV_XPATH)
    add_csv_file = (By.XPATH, ADD_FILE_BTN_XPATH)
    go_to_settings_btn = (By.XPATH, GO_TO_SETTINGS_BTN_XPATH)
    btn_import_reviews = (By.XPATH, IMPORT_REVIEW_BTN_XPATH)
    btn_view_product = (By.XPATH, VIEW_PRODUCT_XPATH)
    buy_it_now_btn = (By.XPATH, BUY_IT_NOW_BTN_XPATH)
    select_apps = (By.XPATH, APPS_BTN_XPATH)
    delete_apps = (By.XPATH, BTN_DELETE_APPS)
    delete_apps_confirm = (By.XPATH, BTN_DELETE_APPS_CONFIRM)


    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # Install app 
    def set_fill_store_name(self, store_name):
        fill_name_store = self.driver.find_element(*self.fill_name_store)
        fill_name_store.send_keys(store_name)

    def click_login_btn(self):
        btn_login = self.driver.find_element(*self.btn_login)
        btn_login.click()

    def set_fill_store_email(self, store_email):
        fill_email_shopify = self.driver.find_element(*self.fill_email_shopify)
        fill_email_shopify.send_keys(store_email)

    def click_next_btn(self):
        btn_next_shopify = self.driver.find_element(*self.btn_next_shopify)
        btn_next_shopify.click()

    def set_fill_store_pass(self, store_pass):
        fill_pasword_shopify = self.driver.find_element(*self.fill_pasword_shopify)
        fill_pasword_shopify.send_keys(store_pass)
        
    def click_login_btn_shopify(self):
        btn_login_shopify = self.driver.find_element(*self.btn_login_shopify)
        btn_login_shopify.click()

    def click_install_app_btn(self):
        btn_install_app = self.driver.find_element(*self.btn_install_app)
        btn_install_app.click()

    def click_choose_plan_btn(self):
        btn_choose_premium_plan = self.driver.find_element(*self.btn_choose_premium_plan)
        btn_choose_premium_plan.click()

    def click_start_free_trial_btn(self):
        btn_start_trial = self.driver.find_element(*self.btn_start_trial)
        btn_start_trial.click()

    def click_get_review_btn(self):
        click_get_review = self.driver.find_element(*self.click_get_review)
        click_get_review.click()

    def click_review_btn(self):
        review_btn = self.driver.find_element(*self.review_btn)
        review_btn.click()

    def click_import_review(self):
        import_review_product = self.driver.find_element(*self.import_review_product)
        import_review_product.click()    
    
    def select_csv_file_btn(self):
        select_csv_file = self.driver.find_element(*self.select_csv_file)
        select_csv_file.click()

    def set_add_csv_file(self, csv_file):
        add_csv_file = self.driver.find_element(*self.add_csv_file)
        add_csv_file.send_keys(csv_file)

    def click_go_to_settings_btn(self):
        go_to_settings_btn = self.driver.find_element(*self.go_to_settings_btn)
        go_to_settings_btn.click()

    def click_import_reviews(self):
        btn_import_reviews = self.driver.find_element(*self.btn_import_reviews)
        btn_import_reviews.click()

    def click_view_product(self):
        btn_view_product = self.driver.find_element(*self.btn_view_product)
        btn_view_product.click()

    def click_apps(self):
        select_apps = self.driver.find_element(*self.select_apps)
        select_apps.click()

    def select_delete_app(self):
        delete_apps = self.driver.find_element(*self.delete_apps)
        delete_apps.click()
    
    def select_delete_app_confirm(self):
        delete_apps_confirm = self.driver.find_element(*self.delete_apps_confirm)
        delete_apps_confirm.click()




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
    
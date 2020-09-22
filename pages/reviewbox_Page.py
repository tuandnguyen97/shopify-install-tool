from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
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
    btn_select_delete_review = (By.XPATH, SELECT_DELETE_REVIEW_XPATH)
    btn_delete_review = (By.XPATH, BTN_DELETE_REVIEWS_XPATH)
    select_apps = (By.XPATH, APPS_BTN_XPATH)
    delete_apps = (By.XPATH, BTN_DELETE_APPS_XPATH)
    delete_apps_confirm = (By.XPATH, BTN_DELETE_APPS_CONFIRM_XPATH)


    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # Install app 
    def set_fill_store_name(self, store_name):
        try:
            fill_name_store = self.driver.find_element(*self.fill_name_store)
            fill_name_store.send_keys(store_name)
            sleep(1)
            print("Step 1: Fill Store name passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_login_btn(self):
        try:
            btn_login = self.driver.find_element(*self.btn_login)
            btn_login.click()
            sleep(1)
            print("Step 2: Click button passed")
        except Exception as err:
            print("Error {}".format(err))

    def set_fill_store_email(self, store_email):
        try:
            fill_email_shopify = self.driver.find_element(*self.fill_email_shopify)
            fill_email_shopify.send_keys(store_email)
            sleep(1)
            print("Step 3: Fill Store email passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_next_btn(self):
        try:   
            btn_next_shopify = self.driver.find_element(*self.btn_next_shopify)
            btn_next_shopify.click()
            sleep(1)
            print("Step 4: Click button passed")
        except Exception as err:
            print("Error {}".format(err))

    def set_fill_store_pass(self, store_pass):
        try:
            fill_pasword_shopify = self.driver.find_element(*self.fill_pasword_shopify)
            fill_pasword_shopify.send_keys(store_pass)
            sleep(1)
            print("Step 5: Fill Store password passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_login_btn_shopify(self):
        try:
            btn_login_shopify = self.driver.find_element(*self.btn_login_shopify)
            btn_login_shopify.click()
            sleep(3)
            print("Step 6: Click button Login passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_install_app_btn(self):
        try:
            btn_install_app = self.driver.find_element(*self.btn_install_app)
            btn_install_app.click()
            sleep(5)
            print("Step 7: Click Install button passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_choose_plan_btn(self):
        try:
            btn_choose_premium_plan = self.driver.find_element(*self.btn_choose_premium_plan)
            btn_choose_premium_plan.click()
            sleep(5)
            print("Step 8: Choose plan Premium passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_start_free_trial_btn(self):
        try:
            btn_start_trial = self.driver.find_element(*self.btn_start_trial)
            btn_start_trial.click()
            sleep(10)
            print("Step 9: Start free trial passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_get_review_btn(self):
        try:
            click_get_review = self.driver.find_element(*self.click_get_review)
            click_get_review.click()
            sleep(2)
            print("Step 10: Click get review passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_review_btn(self):
        try:
            review_btn = self.driver.find_element(*self.review_btn)
            review_btn.click()
            sleep(2)
            print("Step 11: Click review button passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_import_review(self):
        try:
            import_review_product = self.driver.find_element(*self.import_review_product)
            import_review_product.click() 
            sleep(2)   
            print("Step 12: Click Import review passed")
        except Exception as err:
            print("Error {}".format(err))

    def select_csv_file_btn(self):
        try:
            select_csv_file = self.driver.find_element(*self.select_csv_file)
            select_csv_file.click()
            sleep(3)
            print("Step 13: Select to import CSV passed")
        except Exception as err:
            print("Error {}".format(err))

    def set_add_csv_file(self, csv_file):
        try:
            add_csv_file = self.driver.find_element(*self.add_csv_file)
            add_csv_file.send_keys(csv_file)
            sleep(5)
            print("Step 14: Add file CSV passed ")
        except Exception as err:
            print("Error {}".format(err))

    def click_go_to_settings_btn(self):
        try:
            go_to_settings_btn = self.driver.find_element(*self.go_to_settings_btn)
            go_to_settings_btn.click()
            sleep(3)
            print("Step 15: Click Setting button passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_import_reviews(self):
        try:
            btn_import_reviews = self.driver.find_element(*self.btn_import_reviews)
            btn_import_reviews.click()
            sleep(10)
            print("Step 16: Click import reviews passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_view_product(self):
        try:
            btn_view_product = self.driver.find_element(*self.btn_view_product)
            btn_view_product.click()
            sleep(3)
            print("Step 17: View product passed")
        except Exception as err:
            print("Error {}".format(err))

    def select_delete_review(self):
        try:
            btn_select_delete_review = Select(self.driver.find_element(*self.btn_select_delete_review))
            btn_select_delete_review.select_by_value('deleteAllReviewsModal')
            sleep(5)
            print("Step 18: Select delete review passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_delete_reviews(self):
        try:
            btn_delete_review = self.driver.find_element(*self.btn_delete_review)
            btn_delete_review.click()
            sleep(10)
            print("Step 19: Delete review passed")
        except Exception as err:
            print("Error {}".format(err))

    def click_apps(self):
        try:
            select_apps = self.driver.find_element(*self.select_apps)
            select_apps.click()
            sleep(1)
            print("Step 20: Click to delete app passed")
        except Exception as err:
            print("Error {}".format(err))

    def select_delete_app(self):
        try:
            delete_apps = self.driver.find_element(*self.delete_apps)
            delete_apps.click()
            sleep(3)
            print("Step 21: Select delete app passed")
        except Exception as err:
            print("Error {}".format(err))

    def select_delete_app_confirm(self):
        try:
            delete_apps_confirm = self.driver.find_element(*self.delete_apps_confirm)
            # wait = WebDriverWait(driver, 10)
            # delete_apps_confirm = wait.until(EC.element_to_be_clickable(delete_apps_confirm))
            delete_apps_confirm.click()
            sleep(7)
            print("Step 22: Delete app passed")
        except Exception as err:
            print("Error {}".format(err))

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
    
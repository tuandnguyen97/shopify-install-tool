from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.locators import *

class addReviewJudge:

    FILL_EMAIL_SHOPIFY_XPATH = (By.XPATH, '//*[@id="account_email"]')
    NEXT_BTN_SHOPIFY_XPATH = (By.XPATH, '//button[@type="submit" and contains(@class, "ui-button ui-button--primary ui-button--size-large  captcha__submit")]')
    FILL_PASSWORD_SHOPIFY_XPATH = (By.XPATH, '//*[@id="account_password"]')
    LOGIN_BTN_SHOIFY_XPATH = (By.XPATH, '//*[@id="login_form"]/div[2]/ul/button')
    APPS_BTN_XPATH = (By.XPATH, '//a[.="Apps"]')
    IMPORT_APP_JUDGE_BTN_XPATH = (By.XPATH, '//ul[@class="Polaris-ResourceList_r589e"]//div[@class="style"]/div[.="AliExpress Review Importer"]')
    IMPORT_BTN_XPATH = (By.XPATH, '//span[@class="Polaris-Button__Text_yj3uv"][contains(.,"Import AliExpress Reviews")]')
    NEXT_BTN_SKIP_XPATH = (By.XPATH, ' //div[text()="Next"]')
    FILL_URL_AE_PRODUCT_XPATH = (By.XPATH, '//input[@id="external_product_url"]')
    FILL_PRODUCT_TITLE_XPATH = (By.XPATH, '//input[@id="product_title"]')
    SELECT_NUMBER_REVIEWS_XPATH = (By.XPATH, '//input[@id="max_reviews_count"]')
    UNCHECK_EMAIL_XPATH = (By.XPATH, '//input[@id="notify_shop"]')
    IMPORT_REVIEWS_BTN_XPATH = (By.XPATH, '//button[@class="btn btn-primary btn-raised ali-crawler-modal__submit-btn"]')
    CONTINUE_BTN_XPATH = (By.XPATH, '//button[@class="cancel"]')
    IFRAME_URL_1 = (By.XPATH, "//iframe[@name='app-iframe']")
    IFRAME_URL_2 = (By.XPATH, "//iframe[@id='internal-api-iframe']")


    def __init__(self,driver):
        self.driver = driver
    # def window_size(browser):
    #     browser.maximize_window()

    def load(self):
        self.driver.get(self.URL)

    # Write Review

    def set_fill_email_shopify(self, email):
        fill_email_shopify = self.driver.find_element(*self.FILL_EMAIL_SHOPIFY_XPATH)
        fill_email_shopify.send_keys(email)

    def click_next_btn_shopify(self):
        btn_next_shopify = self.driver.find_element(*self.NEXT_BTN_SHOPIFY_XPATH)
        btn_next_shopify.click()

    def set_fill_pass_shopify(self, password):
        fill_pasword_shopify = self.driver.find_element(*self.FILL_PASSWORD_SHOPIFY_XPATH)
        fill_pasword_shopify.send_keys(password)

    def click_login_btn_shopify(self):
        btn_login_shopify = self.driver.find_element(*self.LOGIN_BTN_SHOIFY_XPATH)
        btn_login_shopify.click()

    def click_apps_btn_shopify(self):
        btn_apps_shopify = self.driver.find_element(*self.APPS_BTN_XPATH)
        btn_apps_shopify.click()

    def click_judge_import(self):
        judge_import = self.driver.find_element(*self.IMPORT_APP_JUDGE_BTN_XPATH)
        judge_import.click()

    # def click_skip_button(self):
    #     skip_popup = self.driver.find_element(*self.NEXT_BTN_SKIP_XPATH)
    #     skip_popup.click()

    def click_import_button(self):
        import_button = self.driver.find_element(*self.IMPORT_BTN_XPATH)
        import_button.click()

    def set_fill_product_url(self, product_name, number):
        iframe_url_1 = self.driver.find_element(*self.IFRAME_URL_1)
        self.driver.switch_to.frame(iframe_url_1)
        iframe_url_2 = self.driver.find_element(*self.IFRAME_URL_2)
        self.driver.switch_to.frame(iframe_url_2)
        
        fill_product_url = self.driver.find_element(*self.FILL_URL_AE_PRODUCT_XPATH)
        fill_product_url.send_keys("https://www.aliexpress.com/item/33026237232.html")

        fill_product_name = self.driver.find_element(*self.FILL_PRODUCT_TITLE_XPATH)
        fill_product_name.send_keys(product_name)

        fill_number_reviews = self.driver.find_element(*self.SELECT_NUMBER_REVIEWS_XPATH)
        fill_number_reviews.clear()
        fill_number_reviews.send_keys(number)

    def uncheck_checkbox_mail(self):
        click_checkbox = self.driver.find_element(*self.UNCHECK_EMAIL_XPATH)
        click_checkbox.click()
        sleep(10)

    def click_import_review_judge(self):
        click_import = self.driver.find_element(*self.IMPORT_REVIEWS_BTN_XPATH)
        click_import.click()
        sleep(3)

    def click_continue_import(self):
        click_continue_import = self.driver.find_element(*self.CONTINUE_BTN_XPATH)
        click_continue_import.click()
        sleep(3)

    

    # def set_fill_product_type_shopify(self, product_type):
    #     fill_type_product_shopify = self.driver.find_element(*self.fill_type_product_shopify)
    #     fill_type_product_shopify.send_keys(product_type)

    # def set_add_photo_product(self, photo):
    #     add_photo_product = self.driver.find_element(*self.add_photo_product)
    #     add_photo_product.send_keys(photo)

    # def click_save_product_btn_shopify(self):
    #     btn_save_product_shopify = self.driver.find_element(*self.btn_save_product_shopify)
    #     btn_save_product_shopify.click()

    
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
    
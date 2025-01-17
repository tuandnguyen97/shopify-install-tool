from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from time import sleep
from Locators.createStore_MCMA_locator import *
from selenium.webdriver.support import expected_conditions as EC



class CreateTrialstore:
    btn_create_trial = (By.XPATH, CREATE_START_TRIAL_BTN)
    btn_skip = (By.XPATH, SKIP_BTN)
    btn_next_1 = (By.XPATH, NEXT_BTN_1)
    btn_next_2 = (By.XPATH, NEXT_BTN_2)
    btn_next_3 = (By.XPATH, NEXT_BTN_3)
    input_store_name = (By.XPATH, INPUT_STORE_NAME)
    btn_continue_email = (By.XPATH, CONTINUE_WITH_EMAIL_BTN)
    input_email = (By.XPATH, INPUT_EMAIL)
    input_pass = (By.XPATH, INPUT_PASS)
    btn_create_shopify_id = (By.XPATH, CREATE_SHOPIFY_ID_BTN)
    btn_add_apps = (By.XPATH, ADD_APPS_BTN)
    btn_shopify_apps_store = (By.XPATH, SHOPIFY_APP_STORE_BTN)
    textbox_search_keyword = (By.XPATH, SEARCH_APPS_TEXTBOX)
    iframe_review = (By.XPATH, IFRAME)
    page_3_btn = (By.XPATH, PAGE_3_BTN)
    page_6_btn = (By.XPATH, PAGE_6_BTN)
    page_8_btn = (By.XPATH, PAGE_8_BTN)
    page_9_btn = (By.XPATH, PAGE_9_BTN)
    select_app = (By.XPATH, SELECT_APP)
    btn_add_shopify_app = (By.XPATH, ADD_APP_SHOPIFY_BTN)
    btn_install_app = (By.XPATH, INSTALL_APP_BTN)
    btn_skip_help = (By.XPATH, SKIP_HELP_BTN)
    all_app = (By.XPATH, All_APP)
    create_account = (By.XPATH, CREATE_ACCOUNT)

    def __init__(self,driver):
        self.driver = driver
    
    # def window_size(driver):
    #     driver.maximize_window()

    def load(self,driver):
        self.driver.get(self.URL)

    # CREATE TRIAL STORE
    def create_trial_btn(self):
        try:
            btn_create_trial = self.driver.find_element(*self.btn_create_trial)
            btn_create_trial.click()
            sleep(5)
        except Exception as err:
            print("Error {}".format(err))

    def click_skip_all_btn(self):
        print(f"step 3.1")
        btn_skip = self.driver.find_element(*self.btn_skip)
        btn_skip.click()
        sleep(3)

    def click_skip_help(self):
        btn_skip_help = self.driver.find_element(*self.btn_skip_help)
        btn_skip_help.click()
        sleep(3)

    def click_next_btn_1(self):
        btn_next_1 = self.driver.find_element(*self.btn_next_1)
        btn_next_1.click()
        sleep(5)

    def fill_store_name(self,storename):
        input_store_name = self.driver.find_element(*self.input_store_name)
        input_store_name.click()
        sleep(2)
        input_store_name.send_keys(storename)
        sleep(3)   

    def click_next_btn_2(self):
        btn_next_2 = self.driver.find_element(*self.btn_next_2)
        btn_next_2.click()
        sleep(5)

    def click_next_btn_3(self):
        btn_next_3 = self.driver.find_element(*self.btn_next_3)
        btn_next_3.click()
        sleep(5)

    def click_email_continue_btn(self):
        btn_continue_email = self.driver.find_element(*self.btn_continue_email)
        btn_continue_email.click()
        sleep(3)

    def fill_email(self,email):
        input_email = self.driver.find_element(*self.input_email)
        input_email.click()
        sleep(2)
        input_email.send_keys(email)
        sleep(3)  

    def fill_pass(self,password):
        input_pass = self.driver.find_element(*self.input_pass)
        input_pass.click()
        sleep(2)
        input_pass.send_keys(password)
        sleep(10)  

    def click_create_account(self):
        create_account = self.driver.find_element(*self.create_account)
        create_account.click()
        sleep(10) 
        
    def click_create_shopify_id_btn(self):
        btn_create_shopify_id = self.driver.find_element(*self.btn_create_shopify_id)
        btn_create_shopify_id.click()
        sleep(10)

    def click_add_apps_btn(self):
        btn_add_apps = self.driver.find_element(*self.btn_add_apps)
        btn_add_apps.click()
        sleep(5)

    def click_shopify_apps_store_btn(self):
        btn_shopify_apps_store = self.driver.find_element(*self.btn_shopify_apps_store)
        btn_shopify_apps_store.click()
        sleep(10)

    def fill_keyword(self,keyword):
        textbox_search_keyword = self.driver.find_element(*self.textbox_search_keyword)
        textbox_search_keyword.click()
        sleep(2)
        textbox_search_keyword.send_keys(keyword)
        sleep(2)
        textbox_search_keyword.send_keys(Keys.ENTER)
        sleep(5)

    def search_app(self):
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
        # page_3_btn = self.driver.find_element(*self.page_3_btn)
        # self.driver.execute_script("arguments[0].click();", page_3_btn)
        # print('sang trang 3')
        # sleep(5)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
        # page_6_btn = self.driver.find_element(*self.page_6_btn)
        # self.driver.execute_script("arguments[0].click();", page_6_btn)
        # print('sang trang 6')
        # sleep(5)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
        # page_8_btn = self.driver.find_element(*self.page_8_btn)
        # self.driver.execute_script("arguments[0].click();", page_8_btn)
        # print('sang trang 8')
        # sleep(5)
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
        # page_9_btn = self.driver.find_element(*self.page_9_btn)
        # self.driver.execute_script("arguments[0].click();", page_9_btn)
        # print('sang trang 9')
        # sleep(5)
        # Lấy URL hiện tại
        current_url = self.driver.current_url
        # Thêm hoặc sửa đổi tham số page=9
        if "page=" not in current_url:
            new_url = current_url + "&page=7"
        else:
            new_url = current_url.split("&page=")[0] + "&page=7"
        # Chuyển hướng đến URL mới
        self.driver.get(new_url)
        sleep(5)
        # elements = self.driver.find_elements(*self.all_app)
        # for element in elements:
        #     if "Promofy" in element.text:
        #         print('find out')
        #         self.driver.execute_script("arguments[0].click();", element)
        # sleep(10)

    def click_page_btn(self):
        page_3_btn = self.driver.find_element(*self.page_3_btn)
        page_3_btn.click()
        sleep(5)

    def click_select_app_install(self):
        select_app = self.driver.find_element(*self.select_app)
        select_app.click()
        sleep(5)

    def click_app_shopify(self):
        btn_add_shopify_app = self.driver.find_element(*self.btn_add_shopify_app)
        btn_add_shopify_app.click()
        sleep(10)

    def click_install_app_shopify(self):
        btn_install_app = self.driver.find_element(*self.btn_install_app)
        btn_install_app.click()
        sleep(10)
    
    def is_exits_click_add_apps_btn(self):
        try:
            self.driver.find_element(*self.btn_add_apps)
            return True
        except NoSuchElementException:
            return False

    def is_exits_click_skip_help(self):
        try:
            self.driver.find_element(*self.btn_skip_help)
            return True
        except NoSuchElementException:
            return False

    def is_exits_click_email_continue_btn(self):
        try:
            self.driver.find_element(*self.btn_continue_email)
            return True
        except NoSuchElementException:
            return False


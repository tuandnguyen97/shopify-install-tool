# Add Review page
WRITE_REVIEW_BTN_XPATH = '//*[@id="shopify-ali-review"]/div/div/div/div/div[3]/div[2]'
FILL_NAME_ID = 'your_name'
FILL_EMAIL_ID = 'your_email'
FILL_CONTENT_ID = 'content'
ADD_PHOTO_BTN_XPATH = '//input[@type="file"]'
ADD_REVIEW_BTN_XPATH = '//*[@id="btn-add-review"]'


# Create Order
PRODUCT_1_XPATH = '//*[@id="Collection"]/ul[1]/li[1]/div/a'
PRODUCT_2_XPATH = '//*[@id="Collection"]/ul[1]/li[2]/div/a'
PRODUCT_3_XPATH = '//*[@id="Collection"]/ul[1]/li[3]/div/a'
BUY_IT_NOW_BTN_XPATH = '//*[text() = "Buy it now"]'
FILL_EMAIL_PHONE_XPATH = '//*[@id="checkout_email_or_phone"]'
FILL_FIRST_NAME_XPATH = '//*[@id="checkout_shipping_address_first_name"]'
FILL_LAST_NAME_XPATH = '//*[@id="checkout_shipping_address_last_name"]'
FILL_ADDRESS_XPATH = '//*[@id="checkout_shipping_address_address1"]'
FILL_CITY_XPATH = '//*[@id="checkout_shipping_address_city"]'
FILL_POSTAL_CODE_XPATH = '//*[@id="checkout_shipping_address_zip"]'
NEXT_BUTTON_XPATH = '//*[@id="continue_button"]'


# Add card test
IFRAME_REGISTER_CARD_NUMBER = '//iframe[@title="Field container for: Card number"]'
IFRAME_REGISTER_CARD_NAME = "//iframe[@title='Field container for: Name on card']"
IFRAME_REGISTER_CARD_EXPIRY = "//iframe[@title='Field container for: Expiration date (MM / YY)']"
IFRAME_REGISTER_CARD_SECURITY = "//iframe[@title='Field container for: Security code']"
NUMBER_CARD_XPATH = '//*[@id="number"]'
# NUMBER_CARD_XPATH = '//*[class="field__input field__input--iframe-container"]'
NAME_CARD_XPATH = '//*[@id="name"]'
EXPIRY_CARD_XPATH = '//*[@id="expiry"]'
SECURITY_CARD_XPATH = '//*[@id="verification_value"]'


# Add product 
FILL_EMAIL_SHOPIFY_XPATH = '//*[@id="account_email"]'
# NEXT_BTN_SHOPIFY_XPATH = '//*[@id="body-content"]/div[1]/div[2]/div/form/button'
NEXT_BTN_SHOPIFY_XPATH = '//button[@type="submit" and contains(@class, "ui-button ui-button--primary ui-button--size-large  captcha__submit")]'
FILL_PASSWORD_SHOPIFY_XPATH = '//*[@id="account_password"]'
LOGIN_BTN_SHOIFY_XPATH = '//*[@id="login_form"]/div[2]/ul/button'
PRODUCT_BTN_XPATH = '//span[text()="Products"]/ancestor::a'
ADD_PRODUCT_BTN_XPATH = '//span[text()="Add product"]/ancestor::a'
FILL_PRODUCT_NAME_XPATH = '//input[@name="title"]'
FILL_PRICE_PRODUCT_XPATH = '//input[@name="price"]'
FILL_QUANTITY_PRODUCT_XPATH = '//*[@id="AdjustQuantityPopoverTextFieldActivator"]'
FILL_TYPE_PRODUCT_XPATH = '//input[@placeholder="e.g. Shirts"]'
ADD_PHOTO_PRODUCT_XPATH = '//input[@type="file"]'
SAVE_PRODUCT_BTN_XPATH = '//span[text()="Save"]/ancestor::button' 

# Review Box page
FILL_STORE_NAME_XPATH = '//input[@placeholder="Store Name"]'
LOGIN_BTN_AR_APP_XPATH = '//button[@type="button" and contains(@class, "button button--primary wow fadeInUp buttn__submit")]'
INSTALL_APP_BTN_XPATH = '//button[@type="submit" and contains(@class, "ui-button ui-button--primary")]'
PREMIUM_BTN_XPATH = '//button[@href="submit" and contains(@class, "button button-border-gray button-ab-testing")]'
START_TRIAL_BTN_XPATH = '//button[@type="submit" and contains(@class, "ui-button ui-button--primary ui-button--full-width js-btn-loadable has-loading")]'
# BTN_CLOSE_XPATH = '//button[@type="button" and contains(@class, "button button--close")]'
REVIEW_BTN_XPATH = '/html/body/div[2]/aside/div/ul/li[2]'
IMPORT_REVIEW_TAB_XPATH = '//*[@id="reviews"]/div/ul/li[1]'
IMPORT_REVIEW_PRODUCT_XPATH = '//*[@id="product-item-5797444845735"]/td[5]/button'
SELECT_CSV_XPATH = '//*[@id="modalSelectTypeGetReview"]/div/div/div[2]/div/div[2]/div[2]'
ADD_FILE_BTN_XPATH = '//input[@type="file"]'
GO_TO_SETTINGS_BTN_XPATH = '//*[@id="csv_import_reviews"]/div[1]/div[3]/button[2]'
IMPORT_REVIEW_BTN_XPATH = '//*[@id="csv_import_reviews"]/div[2]/div[9]/button[2]'
SELECT_DELETE_REVIEW_XPATH = '//*[@id="product-item-5797444845735"]/td[4]/div/select'
BTN_DELETE_REVIEWS_XPATH = '//button[@type="submit" and contains(@class, "button button--default w-105px mar-r-5")]'
VIEW_PRODUCT_XPATH = '//*[@href="https://store-billing-10.myshopify.com/products/product-0109190742"]'
APPS_BTN_XPATH = '//span[text()="Apps"]/ancestor::a'
BTN_DELETE_APPS_XPATH = '//button[@type="button" and contains(@class, "Polaris-Button_r99lw Polaris-Button--destructive_zy6o5 Polaris-Button--plain_2z97r")]'
BTN_DELETE_APPS_CONFIRM_XPATH = '//button[@type="button" and contains(@class, "Polaris-Button_r99lw Polaris-Button--primary_7k9zs Polaris-Button--destructive_zy6o5")]'

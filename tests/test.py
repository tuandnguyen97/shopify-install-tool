# selenium 4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
sleep(3)

# Opens a new tab
driver.execute_script("window.open()")
sleep(3)

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])
sleep(3)
# Navigate to new URL in new tab
driver.get("https://google.com")
# Run other commands in the new tab here
sleep(3)

# Switch to original tab
# driver.switch_to.window(driver.window_handles[0])
# sleep(3)

# # Close original tab
# driver.close()
# sleep(3)

# # Switch back to newly opened tab, which is now in position 0
# driver.switch_to.window(driver.window_handles[0])
# sleep(3)
driver.close()
sleep(3)

# Switch back to original tab
driver.switch_to.window(driver.window_handles[0])
sleep(3)

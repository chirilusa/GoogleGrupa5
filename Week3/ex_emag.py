import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
delay = 20  # seconds
try:
    myElem = WebDriverWait(browser, delay)
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

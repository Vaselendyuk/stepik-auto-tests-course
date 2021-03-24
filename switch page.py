from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    a_element = browser.find_element_by_css_selector("#input_value")
    a = a_element.text
    x = str(math.log(abs(12 * math.sin(int(a)))))
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(x)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(10)
    browser.quit()

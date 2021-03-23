from selenium import webdriver
import time
from selenium.webdriver.support.ui import Se
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_element = browser.find_element_by_css_selector("#num1")
    b_element = browser.find_element_by_css_selector("#num2")
    a = a_element.text
    b = b_element.text
    x = int(a)+int(b)
    select = Select(browser.find_element_by_tag_name("#dropdown"))
    select.select_by_visible_text(str(x))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
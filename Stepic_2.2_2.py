import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)
    check_box = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
    check_box.click()
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "[name = firstname]")
    first_name.send_keys("Tom")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name = lastname]")
    last_name.send_keys("Gorand")
    email = browser.find_element(By.CSS_SELECTOR, "[name = email]")
    email.send_keys("123@mail.us")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, "file.txt")
    print(file_path)
    file_send = browser.find_element(By.ID, "file")
    file_send.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
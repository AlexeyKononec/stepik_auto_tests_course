import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button_click = browser.find_element(By.CLASS_NAME, "btn-primary")
    button_click.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()

    #submit_button = browser.find_element(By.CLASS_NAME, "btn-primary")
    #submit_button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
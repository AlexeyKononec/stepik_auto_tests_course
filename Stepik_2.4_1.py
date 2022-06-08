import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/wait1.html"
    #link = "http://suninjuly.github.io/cats.html"
    browser.get(link)
    button_click = browser.find_element(By.ID, "verify")
    button_click.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
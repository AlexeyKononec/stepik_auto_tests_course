import time
from selenium import webdriver

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # открываем страницу
    browser.get("http://suninjuly.github.io/get_attribute.html")
    # поиск картинки сундука
    treasure = browser.find_element_by_id("treasure")
    # считываение х
    x = treasure.get_attribute("valuex")
    y = calc(x)
    # ввод у
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)
    # поиск checkbox
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    # поиск radiobutton
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    # поиск кнопки
    submit = browser.find_element_by_css_selector("[type = submit]")
    submit.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
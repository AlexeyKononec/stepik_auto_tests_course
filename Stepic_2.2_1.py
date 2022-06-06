import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    # открываем страницу
    browser.get("http://suninjuly.github.io/selects1.html")
    # поиск чисел
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum = str(int(num1) + int(num2))
    print(sum)
    # поиск списка
    browser.find_element_by_id("dropdown").click()
    # поиск нужной цифры в списке
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(sum)
    # поиск кнопки
    submit = browser.find_element_by_css_selector("[type = submit]")
    submit.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
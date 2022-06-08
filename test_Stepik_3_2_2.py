import unittest
import time
from selenium import webdriver

class Test_text_assert(unittest.TestCase):
    #def test_start_browser(self):
    #    self.browser = webdriver.Chrome()
    #    time.sleep(1)
    #    self.browser.quit()

    def test_text_assert_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)
        input1 = browser.find_element_by_css_selector("div.first_class input:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.second_class input:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.third_class input:required")
        input3.send_keys("Smolensk@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Not Equal")

        time.sleep(1)
        self.browser.quit()

    def test_text_assert_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link)
        input1 = browser.find_element_by_css_selector("div.first_class input:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.second_class input:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.third_class input:required")
        input3.send_keys("Smolensk@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Not Equal")

        time.sleep(1)
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()

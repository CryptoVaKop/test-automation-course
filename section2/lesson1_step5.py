from selenium import webdriver
import time
import math


# Математическаю функцию от x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # 1.Открыть страницу http://suninjuly.github.io/math.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    # 2 Считать значение для переменной x
    x = browser.find_element_by_id("input_value").text

    # 3.Посчитать математическую функцию от x
    answer = calc(x)

    # 4.Ввести ответ в текстовое поле.
    browser.find_element_by_id("answer").send_keys(answer)

    # 5.Отметить checkbox "I'm the robot".
    browser.find_element_by_id("robotCheckbox").click()

    # 6.Выбрать radiobutton "Robots rule!".
    browser.find_element_by_id("robotsRule").click()

    # 7.Нажать на кнопку Submit.
    browser.find_element_by_class_name("btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()

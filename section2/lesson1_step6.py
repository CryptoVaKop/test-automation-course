from selenium import webdriver
import time
import math

# Математическаю функцию от x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # 1.Открыть страницу http://suninjuly.github.io/get_attribute.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # 2.Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    element = browser.find_element_by_id("treasure")

    # 3.Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = element.get_attribute("valuex")

    # 4.Посчитать математическую функцию от x
    answer = calc(x)

    # 5.Ввести ответ в текстовое поле
    browser.find_element_by_id("answer").send_keys(answer)

    # 6.Отметить checkbox "I'm the robot"
    browser.find_element_by_id("robotCheckbox").click()

    # 7.Выбрать radiobutton "Robots rule!"
    browser.find_element_by_id("robotsRule").click()

    # 8.Нажать на кнопку Submit
    browser.find_element_by_class_name("btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
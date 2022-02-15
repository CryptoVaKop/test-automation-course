from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    # 1.Открыть страницу http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    # 2. Посчитать сумму заданных чисел
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    result = str(num1 + num2)

    # 3. Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    # 4.Нажать на кнопку Submit
    browser.find_element_by_class_name("btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
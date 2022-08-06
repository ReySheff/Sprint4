# Страница "Про Аренду"

from selenium.webdriver.common.by import By
from pages.order_approve_page import OrderApprovePage
import allure


class OrderAboutPage:
    when = [By.CSS_SELECTOR, '[placeholder*="огда"]']
    how_long = [By.CSS_SELECTOR, '[class="Dropdown-placeholder"]']
    one_day = [By.XPATH, "(.//div[contains(text(), 'сут')])[1]"]
    black_color = [By.CSS_SELECTOR, '[for="black"]']
    comment = [By.CSS_SELECTOR, '[placeholder*="ментар"]']
    order_button_in_footer = [By.XPATH, "(.//button[contains(text(), 'казат')])[2]"]
    one_day_calendar = [By.XPATH, '(.//*[@class="react-datepicker__week"])[2]//*[@tabindex="0"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'Заполняем поле "Когда" и кликаем на дату из календаря')
    def set_when(self, when):
        self.driver.find_element(*self.when).send_keys(when)
        self.driver.find_element(*self.one_day_calendar).click()

    @allure.step(f'Заполняем поле "Срок аренды" и выбираем его из списка')
    def set_how_long(self):
        self.driver.find_element(*self.how_long).click()
        self.driver.find_element(*self.one_day).click()

    @allure.step('Выбор "Цвет самоката" "чёрный жемчуг"')
    def set_black_color(self):
        self.driver.find_element(*self.black_color).click()

    @allure.step(f'Заполняем поле комментарий')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    @allure.step('Клик на кнопку "Заказать" и переход на "Подтверждение заказа')
    def end_with_filling_info(self):
        self.driver.find_element(*self.order_button_in_footer).click()
        return OrderApprovePage(self.driver)

    @allure.step('Заполняем все поля в форме')
    def fill_order_form_second(self, when, comment):
        self.set_when(when)
        self.set_how_long()
        self.set_black_color()
        self.set_comment(comment)

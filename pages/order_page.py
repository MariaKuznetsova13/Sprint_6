import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Ожидание отображения формы заказа")
    def wait_element_located(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.ORDER_FORM))

    @allure.step("Заполнение поля 'Имя'")
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).click()
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    @allure.step("Заполнение поля 'Фамилия'")
    def fill_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).click()
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    @allure.step("Заполнение поля 'Адрес: куда привезти самокат'")
    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).click()
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step("Заполнение поля 'Станция метро'")
    def choose_metro_station(self, metro):
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.METRO_DROP_DOWN))
        self.driver.find_element(*metro).click()

    @allure.step("Заполнение поля 'Телефон: на него позвонит курьер'")
    def fill_phone_number(self, phone_number):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.PHONE_NUMBER_FIELD))
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).click()
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.BACK_BUTTON))

    @allure.step("Заполнение поля 'Когда привезти самокат'")
    def choose_date(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.CALENDAR))
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)
        self.driver.find_element(*OrderPageLocators.RENT_TITLE).click()

    @allure.step("Заполнение поля 'Срок аренды'")
    def choose_period(self, chosen_period_locator):
        self.driver.find_element(*OrderPageLocators.PERIOD_FIELD).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.PERIOD_DROP_DOWN))
        self.driver.find_element(*chosen_period_locator).click()

    @allure.step("Заполнение чек-бокса 'Цвет самоката'")
    def choose_color(self, color_checkbox_locator):
        self.driver.find_element(*color_checkbox_locator).click()

    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).click()
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(comment)

    @allure.step("Клик по кнопке 'Заказать' в форме заказа")
    def click_form_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_FORM_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.ORDER_CONFIRMATION_POPUP))
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_BUTTON).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.SUCCESS_POPUP))

    @allure.step("Извлекаем текст об успешном оформлении заказа")
    def check_success_result(self):
        return self.driver.find_element(*OrderPageLocators.SUCCESS_POPUP).text

    @allure.step("Полный флоу заполнения формы заказа")
    def form_order(self, name, surname, address, metro, phone_number, date,
                   chosen_period_locator, color_checkbox_locator, comment):
        self.wait_element_located()
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.choose_metro_station(metro)
        self.fill_phone_number(phone_number)
        self.click_next_button()
        self.choose_date(date)
        self.choose_period(chosen_period_locator)
        self.choose_color(color_checkbox_locator)
        self.fill_comment(comment)
        self.click_form_order_button()

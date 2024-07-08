import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Ожидание отображения формы заказа")
    def wait_order_form_located(self):
        self.wait_element_located(OrderPageLocators.ORDER_FORM)

    @allure.step("Заполнение поля 'Имя'")
    def fill_name(self, name):
        self.click_element(OrderPageLocators.NAME_FIELD)
        self.enter_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Заполнение поля 'Фамилия'")
    def fill_surname(self, surname):
        self.click_element(OrderPageLocators.SURNAME_FIELD)
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step("Заполнение поля 'Адрес: куда привезти самокат'")
    def fill_address(self, address):
        self.click_element(OrderPageLocators.ADDRESS_FIELD)
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Заполнение поля 'Станция метро'")
    def choose_metro_station(self, metro):
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.wait_element_located(OrderPageLocators.METRO_DROP_DOWN)
        self.click_element(metro)

    @allure.step("Заполнение поля 'Телефон: на него позвонит курьер'")
    def fill_phone_number(self, phone_number):
        self.element_to_be_clickable(OrderPageLocators.PHONE_NUMBER_FIELD)
        self.click_element(OrderPageLocators.PHONE_NUMBER_FIELD)
        self.enter_text(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.wait_element_located(OrderPageLocators.BACK_BUTTON)

    @allure.step("Заполнение поля 'Когда привезти самокат'")
    def choose_date(self, date):
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.wait_element_located(OrderPageLocators.CALENDAR)
        self.enter_text(OrderPageLocators.DATE_FIELD, date)
        self.click_element(OrderPageLocators.RENT_TITLE)

    @allure.step("Заполнение поля 'Срок аренды'")
    def choose_period(self, chosen_period_locator):
        self.click_element(OrderPageLocators.PERIOD_FIELD)
        self.wait_element_located(OrderPageLocators.PERIOD_DROP_DOWN)
        self.click_element(chosen_period_locator)

    @allure.step("Заполнение чек-бокса 'Цвет самоката'")
    def choose_color(self, color_checkbox_locator):
        self.click_element(color_checkbox_locator)

    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def fill_comment(self, comment):
        self.click_element(OrderPageLocators.COMMENT_FIELD)
        self.enter_text(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Клик по кнопке 'Заказать' в форме заказа")
    def click_form_order_button(self):
        self.click_element(OrderPageLocators.ORDER_FORM_BUTTON)
        self.wait_element_located(OrderPageLocators.ORDER_CONFIRMATION_POPUP)
        self.click_element(OrderPageLocators.CONFIRMATION_BUTTON)
        self.wait_element_located(OrderPageLocators.SUCCESS_POPUP)

    @allure.step("Извлекаем текст об успешном оформлении заказа")
    def check_success_result(self):
        return self.get_text(OrderPageLocators.SUCCESS_POPUP)

    @allure.step("Полный флоу заполнения формы заказа")
    def form_order(self, name, surname, address, metro, phone_number, date,
                   chosen_period_locator, color_checkbox_locator, comment):
        self.wait_order_form_located()
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

import allure

from locators.base_page_locators import BasePageLocators
from locators.info_page_locators import InfoPageLocators
from pages.base_page import BasePage


class InfoPage(BasePage):

    @allure.step("Ожидание отображения заголовка на главной")
    def wait_header_located(self):
        self.wait_element_located(BasePageLocators.HOME_HEADER)

    @allure.step("Скролл к разделу 'Вопросы о важном'")
    def go_to_faq(self):
        self.go_to_section(InfoPageLocators.DROP_DOWN)

    @allure.step("Извлечение вопроса")
    def get_question(self, question_locator):
        self.element_to_be_clickable(question_locator)
        self.click_element(question_locator)
        return self.get_text(question_locator)

    @allure.step("Извлечение ответа")
    def get_answer(self, answer_locator):
        return self.get_text(answer_locator)

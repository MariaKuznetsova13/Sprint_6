import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.info_page_locators import InfoPageLocators
from pages.base_page import BasePage


class InfoPage(BasePage):
    @allure.step("Скролл к разделу 'Вопросы о важном'")
    def go_to_faq(self):
        element = self.driver.find_element(*InfoPageLocators.DROP_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Извлечение вопроса")
    def get_question(self, question_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(question_locator))
        self.driver.find_element(*question_locator).click()
        return self.driver.find_element(*question_locator).text

    @allure.step("Извлечение ответа")
    def get_answer(self, answer_locator):
        return self.driver.find_element(*answer_locator).text

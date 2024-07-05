import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from constants import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на сайт")
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step("Ожидание отображения заголовка на главной")
    def wait_element_located(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(BasePageLocators.HOME_HEADER))

    @allure.step("Согласие с куками")
    def accept_cookies(self):
        self.driver.find_element(*BasePageLocators.ACCEPT_COOKIES).click()

    @allure.step("Клик на кнопку 'Заказать'")
    def click_order_button(self, button_locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(button_locator))
        self.driver.find_element(*button_locator).click()

    @allure.step("Клик на лого 'Самокат'")
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(BasePageLocators.HOME_HEADER))

    @allure.step("Получаем текущий урл")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Клик на лого 'Яндекс'")
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    @allure.step("Переключение вкладки")
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 15).until(EC.url_to_be(Urls.DZEN_REDIRECT_PAGE_URL))

import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from constants import Urls


class TestLogo:
    @allure.title('Проверка клика на логотип "Самокат"')
    @allure.description('Проверяем, что по клику на логотип "Самокат" открывается главная страница "Самоката"')
    def test_scooter_logo(self, driver):
        page = BasePage(driver)
        page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        page.click_order_button(BasePageLocators.ORDER_BUTTON_HEADER)
        page.click_scooter_logo()
        current_url = page.get_current_url()
        assert current_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка клика на логотип "Яндекс"')
    @allure.description('Проверяем, что по клику на логотип "Яндекс" открывается главная страница Дзена')
    def test_yandex_logo(self, driver):
        page = BasePage(driver)
        page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        page.click_yandex_logo()
        page.switch_tab()
        current_url = page.get_current_url()
        assert current_url == Urls.DZEN_REDIRECT_PAGE_URL

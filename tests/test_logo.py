import allure
from pages.info_page import InfoPage
from locators.base_page_locators import BasePageLocators
from constants import Urls


class TestLogo:
    @allure.title('Проверка клика на логотип "Самокат"')
    @allure.description('Проверяем, что по клику на логотип "Самокат" открывается главная страница "Самоката"')
    def test_scooter_logo(self, driver):
        page = InfoPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_order_button(BasePageLocators.ORDER_BUTTON_HEADER)
        page.click_scooter_logo()
        current_url = page.get_current_url()
        assert current_url == Urls.MAIN_PAGE_URL

    @allure.title('Проверка клика на логотип "Яндекс"')
    @allure.description('Проверяем, что по клику на логотип "Яндекс" открывается главная страница Дзена')
    def test_yandex_logo(self, driver):
        page = InfoPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.click_yandex_logo()
        page.switch_tab()
        current_url = page.get_current_url()
        assert current_url == Urls.DZEN_REDIRECT_PAGE_URL

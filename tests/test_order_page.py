import pytest
import allure

from locators.base_page_locators import BasePageLocators
from pages.order_page import OrderPage
from constants import ListOrders
from constants import Urls


class TestOrderPage:
    @allure.title('Проверка позитивного флоу формы заказа самоката')
    @allure.description('Проверяем, что с двумя разными наборами данных заказ оформляется. '
                        'Тест проверяет оформление заказа с двух кнопок "Заказать"')
    @pytest.mark.parametrize('order_button, test_params', [
                                 (BasePageLocators.ORDER_BUTTON_HEADER, ListOrders.LIST_ORDERS['order_1']),
                                 (BasePageLocators.ORDER_BUTTON_HEADER, ListOrders.LIST_ORDERS['order_2']),
                                 (BasePageLocators.ORDER_BUTTON_FOOTER, ListOrders.LIST_ORDERS['order_1']),
                                 (BasePageLocators.ORDER_BUTTON_FOOTER, ListOrders.LIST_ORDERS['order_2']),
                             ])
    def test_order(self, driver, order_button, test_params):
        page = OrderPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.accept_cookies()
        page.click_order_button(order_button)
        page.form_order(test_params['name'], test_params['surname'], test_params['address'], test_params['metro'],
                        test_params['phone_number'], test_params['date'],
                        test_params['chosen_period_locator'], test_params['color_checkbox_locator'],
                        test_params['comment'])
        success_result = page.check_success_result()
        assert 'Заказ оформлен' in success_result

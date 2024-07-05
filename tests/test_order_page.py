import pytest
import allure
from pages.order_page import OrderPage
from constants import FaqConstants
from constants import ListOrders


class TestOrderPage:
    @allure.title('Проверка позитивного флоу формы заказа самоката')
    @allure.description('Проверяем, что с двумя разными наборами данных заказ оформляется')
    @pytest.mark.parametrize('test_params', ListOrders.LIST_ORDERS)
    def test_order(self, driver, test_params):
        page = OrderPage(driver)
        page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        page.accept_cookies()
        page.click_order_button(test_params['button'])
        page.form_order(test_params['name'], test_params['surname'], test_params['address'], test_params['metro'],
                        test_params['phone_number'], test_params['date'],
                        test_params['chosen_period_locator'], test_params['color_checkbox_locator'],
                        test_params['comment'])
        success_result = page.check_success_result()
        assert 'Заказ оформлен' in success_result
import pytest
import allure
from pages.info_page import InfoPage
from constants import FaqConstants
from constants import Urls


class TestInfoPage:
    @allure.title('Проверка выпадающего списка "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается ответ с соответствующим текстом')
    @pytest.mark.parametrize('test_params', FaqConstants.LIST_QUESTIONS_AND_ANSWERS)
    def test_check_faq(self, driver, test_params):
        page = InfoPage(driver)
        page.go_to_site(Urls.MAIN_PAGE_URL)
        page.wait_header_located()
        page.go_to_faq()
        page.accept_cookies()
        question_text = page.get_question(test_params['question_locator'])
        answer_text = page.get_answer(test_params['answer_locator'])
        assert question_text == test_params['question'] and answer_text == test_params['answer']

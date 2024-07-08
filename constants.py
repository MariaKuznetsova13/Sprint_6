from locators.info_page_locators import InfoPageLocators
from locators.order_page_locators import OrderPageLocators


class Urls:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_REDIRECT_PAGE_URL = 'https://dzen.ru/?yredirect=true'


class FaqConstants:
    # Данные для раздела "Вопросы о важном"
    HOW_MUCH_QUESTION = 'Сколько это стоит? И как оплатить?'
    HOW_MUCH_ANSWER = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    HOW_MANY_SCOOTERS_QUESTION = 'Хочу сразу несколько самокатов! Так можно?'
    HOW_MANY_SCOOTERS_ANSWER = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    TIME_QUESTION = 'Как рассчитывается время аренды?'
    TIME_ANSWER = ('Допустим, вы оформляете заказ на 8 мая. '
                   'Мы привозим самокат 8 мая в течение дня. '
                   'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                   'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    TODAY_ORDER_QUESTION = 'Можно ли заказать самокат прямо на сегодня?'
    TODAY_ORDER_ANSWER = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    HOW_LONG_QUESTION = 'Можно ли продлить заказ или вернуть самокат раньше?'
    HOW_LONG_ANSWER = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    CHARGER_QUESTION = 'Вы привозите зарядку вместе с самокатом?'
    CHARGER_ANSWER = ('Самокат приезжает к вам с полной зарядкой. '
                      'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                      'Зарядка не понадобится.')
    CANCEL_QUESTION = 'Можно ли отменить заказ?'
    CANCEL_ANSWER = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    MKAD_QUESTION = 'Я жизу за МКАДом, привезёте?'
    MKAD_ANSWER = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    LIST_QUESTIONS_AND_ANSWERS = [
        {
            'question_locator': InfoPageLocators.HOW_MUCH_QUESTION,
            'answer_locator': InfoPageLocators.HOW_MUCH_ANSWER,
            'question': HOW_MUCH_QUESTION,
            'answer': HOW_MUCH_ANSWER
        },
        {
            'question_locator': InfoPageLocators.HOW_MANY_SCOOTERS_QUESTION,
            'answer_locator': InfoPageLocators.HOW_MANY_SCOOTERS_ANSWER,
            'question': HOW_MANY_SCOOTERS_QUESTION,
            'answer': HOW_MANY_SCOOTERS_ANSWER
        },
        {
            'question_locator': InfoPageLocators.TIME_QUESTION,
            'answer_locator': InfoPageLocators.TIME_ANSWER,
            'question': TIME_QUESTION,
            'answer': TIME_ANSWER
        },
        {
            'question_locator': InfoPageLocators.TODAY_ORDER_QUESTION,
            'answer_locator': InfoPageLocators.TODAY_ORDER_ANSWER,
            'question': TODAY_ORDER_QUESTION,
            'answer': TODAY_ORDER_ANSWER
        },
        {
            'question_locator': InfoPageLocators.HOW_LONG_QUESTION,
            'answer_locator': InfoPageLocators.HOW_LONG_ANSWER,
            'question': HOW_LONG_QUESTION,
            'answer': HOW_LONG_ANSWER
        },
        {
            'question_locator': InfoPageLocators.CHARGER_QUESTION,
            'answer_locator': InfoPageLocators.CHARGER_ANSWER,
            'question': CHARGER_QUESTION,
            'answer': CHARGER_ANSWER
        },
        {
            'question_locator': InfoPageLocators.CANCEL_QUESTION,
            'answer_locator': InfoPageLocators.CANCEL_ANSWER,
            'question': CANCEL_QUESTION,
            'answer': CANCEL_ANSWER
        },
        {
            'question_locator': InfoPageLocators.MKAD_QUESTION,
            'answer_locator': InfoPageLocators.MKAD_ANSWER,
            'question': MKAD_QUESTION,
            'answer': MKAD_ANSWER
        }
    ]


class ListOrders:
    # Данные для заказа самоката
    LIST_ORDERS = {
        'order_1': {
            'name': 'Мария',
            'surname': 'Попова',
            'address': 'Левашова 3',
            'metro': OrderPageLocators.CHOSEN_METRO_STATION_1,
            'phone_number': '+79999785743',
            'date': '13.09.2024',
            'chosen_period_locator': OrderPageLocators.CHOSEN_PERIOD_ONE_DAY,
            'color_checkbox_locator': OrderPageLocators.SCOOTER_BLACK_COLOR,
            'comment': 'Позвоните у дома'
        },
        'order_2': {
            'name': 'Ваня',
            'surname': 'Петров',
            'address': 'Суфтина 9',
            'metro': OrderPageLocators.CHOSEN_METRO_STATION_2,
            'phone_number': '+79816758365',
            'date': '25.08.2024',
            'chosen_period_locator': OrderPageLocators.CHOSEN_PERIOD_TWO_DAYS,
            'color_checkbox_locator': OrderPageLocators.SCOOTER_GREY_COLOR,
            'comment': 'Спасибо за доставку'
        }
    }

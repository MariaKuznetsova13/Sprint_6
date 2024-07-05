from selenium.webdriver.common.by import By


class InfoPageLocators:
    # Локаторы раздела "Вопросы о важном"
    DROP_DOWN = (By.XPATH, '//div[@class="accordion"]')
    HOW_MUCH_QUESTION = (By.XPATH, '//div[text() = "Сколько это стоит? И как оплатить?"]')
    HOW_MUCH_ANSWER = (By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')
    HOW_MANY_SCOOTERS_QUESTION = (By.XPATH,
                                  '//div[@class="accordion__button" and text() = "Хочу сразу несколько самокатов! Так можно?"]')
    HOW_MANY_SCOOTERS_ANSWER = (By.XPATH,
                                '//p[text() = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]')
    TIME_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Как рассчитывается время аренды?" ]')
    TIME_ANSWER = (
        By.XPATH, '//p[text() = "Допустим, вы оформляете заказ на 8 мая. '
                  'Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                  'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." ]')
    TODAY_ORDER_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Можно ли заказать самокат прямо на сегодня?"]')
    TODAY_ORDER_ANSWER = (By.XPATH, '//p[text() = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')
    HOW_LONG_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Можно ли продлить заказ или вернуть самокат раньше?" ]')
    HOW_LONG_ANSWER = (By.XPATH, '//p[text() = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')
    CHARGER_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Вы привозите зарядку вместе с самокатом?"]')
    CHARGER_ANSWER = (By.XPATH,
                      '//p[text() = "Самокат приезжает к вам с полной зарядкой. '
                      'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
                      'Зарядка не понадобится." ]')
    CANCEL_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Можно ли отменить заказ?"]')
    CANCEL_ANSWER = (By.XPATH, '//p[text() = "Да, пока самокат не привезли. '
                               'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')
    MKAD_QUESTION = (By.XPATH, '//div[@class="accordion__button" and text() = "Я жизу за МКАДом, привезёте?"]')
    MKAD_ANSWER = (By.XPATH, '//p[text() = "Да, обязательно. Всем самокатов! И Москве, и Московской области."]')

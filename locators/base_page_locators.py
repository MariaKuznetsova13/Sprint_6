from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локаторы главной страницы
    HOME_HEADER = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    ACCEPT_COOKIES = [By.XPATH, "//button[.='да все привыкли']"]

    SCOOTER_LOGO = (By.XPATH, ".//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru"]')

from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локаторы формы заказа
    ORDER_FORM = (By.XPATH, '//div[@class="Order_Form__17u6u"]')
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    DATE_FIELD = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")
    METRO_DROP_DOWN = (By.XPATH, '//div[@class="select-search__select"]')
    PERIOD_FIELD = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    SCOOTER_BLACK_COLOR = (By.XPATH, '//label[text() = "чёрный жемчуг"]')
    SCOOTER_GREY_COLOR = (By.XPATH, '//label[text() = "серая безысходность"]')
    COMMENT_FIELD = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, '//button[text()="Назад"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')
    CALENDAR = (By.XPATH, '//div[@class="react-datepicker__month-container"]')
    RENT_TITLE = (By.XPATH, '//div[text()="Про аренду"]')
    PERIOD_DROP_DOWN = (By.XPATH, '//div[@class="Dropdown-menu"]')
    ORDER_CONFIRMATION_POPUP = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    ORDER_FORM_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    CONFIRMATION_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_POPUP = (By.XPATH, '//div[text()="Заказ оформлен"]')

    CHOSEN_PERIOD_ONE_DAY = (By.XPATH, '//div[text()="сутки"]')
    CHOSEN_PERIOD_TWO_DAYS = (By.XPATH, '//div[text()="двое суток"]')
    CHOSEN_PERIOD_THREE_DAYS = (By.XPATH, '//div[text()="трое суток"]')
    CHOSEN_METRO_STATION_1 = (By.XPATH, '//div[text() = "Черкизовская"]')
    CHOSEN_METRO_STATION_2 = (By.XPATH, '//div[text() = "Сокольники"]')

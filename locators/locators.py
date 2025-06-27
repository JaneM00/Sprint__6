# locators/locators.py
from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для FAQ
    FAQ_QUESTION = {
        "question1": (By.CSS_SELECTOR, "[data-question='question1']"),
        "question2": (By.CSS_SELECTOR, "[data-question='question2']"),
        "question3": (By.CSS_SELECTOR, "[data-question='question3']"),
        "question4": (By.CSS_SELECTOR, "[data-question='question4']"),
        "question5": (By.CSS_SELECTOR, "[data-question='question5']"),
        "question6": (By.CSS_SELECTOR, "[data-question='question6']"),
        "question7": (By.CSS_SELECTOR, "[data-question='question7']"),
        "question8": (By.CSS_SELECTOR, "[data-question='question8']")
    }
    FAQ_ANSWER = {
        "question1": (By.CSS_SELECTOR, "[data-answer='question1']"),
        "question2": (By.CSS_SELECTOR, "[data-answer='question2']"),
        "question3": (By.CSS_SELECTOR, "[data-answer='question3']"),
        "question4": (By.CSS_SELECTOR, "[data-answer='question4']"),
        "question5": (By.CSS_SELECTOR, "[data-answer='question5']"),
        "question6": (By.CSS_SELECTOR, "[data-answer='question6']"),
        "question7": (By.CSS_SELECTOR, "[data-answer='question7']"),
        "question8": (By.CSS_SELECTOR, "[data-answer='question8']")
    }
    # Логотип
    LOGO = (By.CSS_SELECTOR, ".header-logo")  

class OrderPageLocators:
    # Локаторы формы заказа
    NAME_INPUT = (By.NAME, "name")
    SURNAME_INPUT = (By.NAME, "surname")
    ADDRESS_INPUT = (By.NAME, "address")
    PHONE_INPUT = (By.NAME, "phone")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]") 

class MainPageHeaderLocators:
    # Локатор для кнопки заказа сверху
    ORDER_TOP_BUTTON = (By.CSS_SELECTOR, ".order-top")  
    # Локатор для кнопки заказа снизу
    ORDER_BOTTOM_BUTTON = (By.CSS_SELECTOR, ".order-bottom")  

class ConfirmationLocators:
    # Локатор сообщения об успешном заказе
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".Order_Modal__Title")  

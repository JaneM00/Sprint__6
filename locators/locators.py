# locators/locators.py

# Локаторы для главной страницы
MAIN_PAGE_LOCATORS = {
    "faq_questions": {
        "question1": ("ID", "question1_id"),
        "question2": ("ID", "question2_id"),
    },
    "faq_answers": {
        "question1": ("ID", "question1_answer"),
        "question2": ("ID", "question2_answer"),
    },
    "order_button_top": ("CLASS_NAME", "Button_Button__ra12g"),
    "order_button_bottom": ("CLASS_NAME", "Button_Button__ra12g"),
    "logo_scooter": ("CLASS_NAME", "Header_Logo__fYF0X"),
    "logo_yandex": ("CSS_SELECTOR", 'a[href="https://dzen.ru/"]'),
}

# Локаторы для страницы заказа
ORDER_PAGE_LOCATORS = {
    "first_name": ("NAME", "name"),
    "second_name": ("NAME", "surname"),
    "address": ("NAME", "address"),
    "phone": ("NAME", "phone"),
    "submit_button": ("CSS_SELECTOR", 'button[type="submit"]'),
    "success_message": ("CLASS_NAME", "Order_Modal__YZ-d3"),
}

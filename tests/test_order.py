# tests/test_order.py

import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

# Определите локаторы для кнопок заказа
ORDER_BUTTON_TOP = (By.CSS_SELECTOR, ".order-top")     # замените на актуальный локатор
ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, ".order-bottom")  # замените на актуальный локатор

@pytest.mark.parametrize("name,surname,address,phone,order_button_locator", [
    ("Иван", "Иванов", "ул. Ленина д.1", "+79991112233", ORDER_BUTTON_TOP),
    ("Петр", "Петров", "пр. Мира д.10", "+79994445566", ORDER_BUTTON_BOTTOM)
])
def test_order_flow(driver, name, surname, address, phone, order_button_locator):
    page = MainPage(driver)
    page.open()
    
    order_page = OrderPage(driver)
    
    # Кликаем по нужной кнопке заказа
    order_page.click_order_button(order_button_locator)
    
    order_page.fill_order_form(name, surname, address, phone)
    order_page.submit_order()
    
    # Проверка сообщения об успешном заказе
    message = order_page.get_success_message()
    assert "Заказ успешно создан" in message or message == "Ваш заказ начали готовить"

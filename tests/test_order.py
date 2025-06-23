# tests/test_order.py

import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.mark.parametrize("name,surname,address,phone,order_button_type", [
    ("Иван", "Иванов", "ул. Ленина д.1", "+79991112233", "top"),
    ("Петр", "Петров", "пр. Мира д.10", "+79994445566", "bottom")
])
def test_order_flow(driver, name, surname, address, phone, order_button_type):
    page = MainPage(driver)
    page.open()
    
    # Выбираем кнопку для заказа на основе параметра
    if order_button_type == "top":
        page.click_order_top()
    elif order_button_type == "bottom":
        page.click_order_bottom()
    else:
        pytest.fail(f"Неизвестный тип кнопки заказа: {order_button_type}")
    
    order_page = OrderPage(driver)
    
    order_page.fill_order_form(name, surname, address, phone)
    order_page.submit_order()
    
    # Проверка сообщения об успешном заказе
    message = order_page.get_success_message()
    assert "Заказ успешно создан" in message or message == "Ваш заказ начали готовить"

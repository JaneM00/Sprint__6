# tests/test_order.py

import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.mark.parametrize("order_button", ["top", "bottom"])
@pytest.mark.parametrize("name,surname,address,phone", [
    ("Иван", "Иванов", "ул. Ленина д.1", "+79991112233"),
    ("Петр", "Петров", "пр. Мира д.10", "+79994445566")
])
def test_order_flow(driver, name, surname, address, phone, order_button):
    page = MainPage(driver)
    page.open()
    
    # В зависимости от параметра выбираем кнопку для заказа
    if order_button == "top":
        page.click_order_top()
    else:
        page.click_order_bottom()
    
    order_page = OrderPage(driver)
    
    order_page.fill_order_form(name, surname, address, phone)
    order_page.submit_order()
    
    # Проверка сообщения об успешном заказе
    message = order_page.get_success_message()
    assert "Заказ успешно создан" in message or message == "Ваш заказ начали готовить"

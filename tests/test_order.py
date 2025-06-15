import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.mark.parametrize("name,surname,address,phone", [
    ("Иван", "Иванов", "ул. Ленина д.1", "+79991112233"),
    ("Петр", "Петров", "пр. Мира д.10", "+79994445566")
])
def test_order_flow(driver, name, surname, address, phone):
    page = MainPage(driver)
    
    page.open()
    
    # Можно выбрать точку входа: верхняя или нижняя кнопка заказа
    page.click_order_top()
    
    order_page = OrderPage(driver)
    
    order_page.fill_order_form(name,surname,address,phone)
    
    order_page.submit_order()
    
     # Проверка сообщения об успешном заказе 
     message = order_page.get_success_message()
     assert "Заказ успешно создан" in message or message == "Ваш заказ начали готовить"

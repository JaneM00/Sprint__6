from .base_page import BasePage
from locators import ORDER_PAGE_LOCATORS as loc

class OrderPage(BasePage):

    def fill_order_form(self, name, surname, address, phone):
        self.input_text(loc["first_name"], name)
        self.input_text(loc["second_name"], surname)
        self.input_text(loc["address"], address)
        self.input_text(loc["phone"], phone)

    def submit_order(self):
        self.click(loc["submit_button"])

    def get_success_message(self):
        return self.find(loc["success_message"]).text

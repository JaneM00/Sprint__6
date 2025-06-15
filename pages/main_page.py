from .base_page import BasePage
from locators import MAIN_PAGE_LOCATORS as loc

class MainPage(BasePage):
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_faq_question(self, question_key):
        locator_type, locator_value = loc["faq_questions"][question_key]
        self.click((locator_type, locator_value))

    def get_faq_answer_text(self, question_key):
        locator_type, locator_value = loc["faq_answers"][question_key]
        return self.find((locator_type, locator_value)).text

    def click_order_top(self):
        locator_type, locator_value = loc["order_button_top"]
        self.click((locator_type, locator_value))

    def click_order_bottom(self):
        locator_type, locator_value = loc["order_button_bottom"]
        self.click((locator_type, locator_value))

    def click_logo_scooter(self):
        locator_type, locator_value = loc["logo_scooter"]
        self.click((locator_type, locator_value))

    def click_logo_yandex(self):
        locator_type, locator_value = loc["logo_yandex"]
        self.click((locator_type, locator_value))

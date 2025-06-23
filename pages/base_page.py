import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент по локатору: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание появления элемента: {locator} с таймаутом {timeout} секунд")
    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

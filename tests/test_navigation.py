# tests/test_navigation.py

import pytest
from pages.main_page import MainPage

def test_click_logo_redirects_to_homepage(driver):
    page = MainPage(driver)
    page.open()
    
    # Кликаем по логотипу
    page.click_logo()
    
    # Проверяем, что оказались на главной странице
    assert page.is_on_homepage()

# Аналогичный тест, выполненный по аналогии с предыдущим сценарием
@pytest.mark.parametrize("description", ["через логотип"])
def test_logo_click_leads_to_main_page(driver, description):
    page = MainPage(driver)
    page.open()
    
    # Кликаем по логотипу
    page.click_logo()
    
    # Проверяем, что мы на главной странице
    assert page.is_on_homepage()

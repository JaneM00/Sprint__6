import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize("question_key", ["question1", "question2"])
def test_faq_answer_display(driver, question_key):
    page = MainPage(driver)
    page.open()
    
    # Нажать на стрелочку вопроса и проверить ответ
    page.click_faq_question(question_key)
    
    answer_text = page.get_faq_answer_text(question_key)
    
    expected_texts = {
        "question1": "Ответ на вопрос 1",
        "question2": "Ответ на вопрос 2",
    }
    
    assert answer_text == expected_texts[question_key]

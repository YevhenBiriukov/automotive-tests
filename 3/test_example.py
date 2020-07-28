import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    #@pytest.fixture(autouse=True)
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        #catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
            #assert catalog_text == "Каталог", \
            #f"Wrong language, got {catalog_text} instead of 'Каталог'"

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        #assert a == b, "Значения разные"
        #assert user_is_authorised(), "User is guest"

    #@pytest.mark.smoke
    #@pytest.mark.win10 #pytest -s -v -m "smoke and win10" test_fixture81.py
    #@pytest.mark.skip
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10


#pytest scripts/drafts.py::test_register_new_user_parametrized
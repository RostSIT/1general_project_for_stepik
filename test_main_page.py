from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest

SIMPLE_LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = SIMPLE_LINK
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина.
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(3)

    def test_guest_should_see_login_link(self, browser):
        link = SIMPLE_LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = SIMPLE_LINK
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.all_tests()

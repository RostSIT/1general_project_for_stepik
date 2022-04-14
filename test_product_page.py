import pytest
import faker
from random import choice

from .pages.product_page import PageObject
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

PROMO_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
SIMPLE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
LOGIN_LINK = 'https://selenium1py.pythonanywhere.com/accounts/login/'


@pytest.mark.login
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = LOGIN_LINK
        page = LoginPage(browser, link)
        page.open()
        fake = faker.Faker()
        page.register_new_user(fake.email(), fake.password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = SIMPLE_LINK
        page = PageObject(browser, link)
        page.open()
        cart_functions = PageObject(browser, browser.current_url)
        cart_functions.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = PROMO_LINK
        page = PageObject(browser, link)
        page.open_click_solve()
        cart_functions = PageObject(browser, browser.current_url)
        cart_functions.add_product_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = PROMO_LINK
    page = PageObject(browser, link)
    page.open_click_solve()
    cart_functions = PageObject(browser, browser.current_url)
    cart_functions.add_product_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = SIMPLE_LINK
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.all_tests()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = SIMPLE_LINK
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


def test_guest_cant_see_success_message(browser):
    link = SIMPLE_LINK
    page = PageObject(browser, link)
    page.open()
    cart_functions = PageObject(browser, browser.current_url)
    cart_functions.guest_cant_see_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = PROMO_LINK
    page = PageObject(browser, link)
    page.open_click_solve()
    cart_functions = PageObject(browser, browser.current_url)
    cart_functions.guest_cant_see_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = SIMPLE_LINK
    page = PageObject(browser, link)
    page.open_click_solve()
    cart_functions = PageObject(browser, browser.current_url)
    cart_functions.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = SIMPLE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

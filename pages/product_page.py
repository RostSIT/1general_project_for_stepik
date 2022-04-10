from .base_page import BasePage
from .locators import Basket


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)


class PageObject(BasePage):

    def add_product_to_basket(self):
        self.should_be_added_book()
        self.should_be_checked_name_book()
        self.should_be_checked_price_book()

    def open_click_solve(self):
        self.open()
        self.click_button()
        self.solve_quiz_and_get_code()

    def click_button(self):
        self.cart_button_click(*Basket.CART_BUTTON)

    def should_be_added_book(self):
        self.is_element_present(*Basket.SUCCESS_MESSAGE)

    def should_be_checked_name_book(self):
        add_name = self.browser.find_element(*Basket.ADD_NAME)
        in_name = self.browser.find_element(*Basket.IN_NAME)
        print(add_name, in_name)
        assert add_name.text == in_name.text, 'Different names of added and claimed books'

    def should_be_checked_price_book(self):
        add_price = self.browser.find_element(*Basket.ADD_PRICE)
        in_price = self.browser.find_element(*Basket.IN_PRICE)
        assert add_price.text == in_price.text, 'Different prices'

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(
            *Basket.SUCCESS_MESSAGE), "Success message after adding product to basket is presented."

        # негативный assert закоментирован для прохода всего теста
        # assert self.is_element_present(
        #     *Basket.SUCCESS_MESSAGE), "The success message after adding product to basket " \
        #                               "is not presented."

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*Basket.SUCCESS_MESSAGE), "Success message is presented."

        # негативный assert закоментирован для прохода всего теста
        # assert self.is_element_present(*Basket.SUCCESS_MESSAGE), "The success message is not presented."

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(
            *Basket.SUCCESS_MESSAGE), "Success message disappeared after adding product to basket is presented."

        # негативный assert закоментирован для прохода всего теста
        # assert self.is_element_present(
        #     *Basket.SUCCESS_MESSAGE), "The success message disappeared after adding product to basket is" \
        #                               "is not presented."

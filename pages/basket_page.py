from .base_page import BasePage
from .locators import Basket


class BasketPage(BasePage):
    def all_tests(self):
        self.message_is_presence()
        # self.negative_message_is_presence()
        self.basket_is_empty()
        # self.negative_test_basket_is_empty()

    def message_is_presence(self):
        message_empty = self.browser.find_element(*Basket.BASKET_IS_EMPTY)
        assert self.is_element_present(*Basket.BASKET_IS_EMPTY), 'not_element_present'
        assert 'Your basket is empty.' in message_empty.text, 'The message does not match the TOR.' \


    # def negative_message_is_presence(self):
    #     assert self.is_not_element_present(*Basket.BASKET_IS_EMPTY), 'element_present'

    # def negative_test_basket_is_empty(self):
    #     assert self.is_element_present(*Basket.ITEMS_TO_BUY_NOW), 'Book is not presence'

    def basket_is_empty(self):
        assert self.is_not_element_present(*Basket.ITEMS_TO_BUY_NOW), 'Book is presence, to buy now'

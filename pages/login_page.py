from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import random
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url, 'The link does not contain the word "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Missing login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Missing registration form'

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = random.randint(1000000000, 9999999999)
        self.browser.find_element(*BasePageLocators.MAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*BasePageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*BasePageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT).click()

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class Basket:
    CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')
    ADD_NAME = (By.CSS_SELECTOR, 'article>div:nth-child(1)>div:nth-child(2) h1')
    IN_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ADD_PRICE = (By.CSS_SELECTOR, 'article>div:nth-child(1)>div:nth-child(2) p.price_color')
    IN_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div  strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

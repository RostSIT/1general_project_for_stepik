from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class Basket:
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs > div > h2')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    CART_PAGE = (By.CSS_SELECTOR, 'div[class="basket-mini pull-right hidden-xs"] >span > a')
    CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(2) > div')
    ADD_NAME = (By.CSS_SELECTOR, 'article>div:nth-child(1)>div:nth-child(2) h1')
    IN_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ADD_PRICE = (By.CSS_SELECTOR, 'article>div:nth-child(1)>div:nth-child(2) p.price_color')
    IN_PRICE = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div  strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    MAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, " #id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[type='password'][name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')

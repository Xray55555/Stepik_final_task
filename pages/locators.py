from selenium.webdriver.common.by import By

class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASS_FIELD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASS_FIELD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')
    REG_SUCCESS = (By.CSS_SELECTOR, '.alertinner i.icon-ok-sign')

class ProductPageLocators():
    basket_btn = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    add_title = (By.CSS_SELECTOR, "div.alertinner")
    prod_name = (By.CSS_SELECTOR, "div.product_main h1")
    in_bask_name = (By.CSS_SELECTOR, "div.alertinner strong")
    price_title = (By.CSS_SELECTOR, "div.alertinner > p:nth-child(1)")
    prod_price = (By.CSS_SELECTOR, "p.price_color")
    in_bask_price = (By.CSS_SELECTOR, "div.alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    go_to_basket_btn = (By.CSS_SELECTOR, 'a.btn.btn-default[href*="/basket/"]')
    product_title = (By.CLASS_NAME, 'basket-title')
    no_product_title = (By.CSS_SELECTOR, '#content_inner > p')

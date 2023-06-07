from selenium.webdriver.common.by import By

class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    basket_btn = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    add_title = (By.CSS_SELECTOR, "div.alertinner")
    prod_name = (By.CSS_SELECTOR, "div.product_main h1")
    in_bask_name = (By.CSS_SELECTOR, "div.alertinner strong")
    price_title = (By.CSS_SELECTOR, "div.alertinner > p:nth-child(1)")
    prod_price = (By.CSS_SELECTOR, "p.price_color")
    in_bask_price = (By.CSS_SELECTOR, "div.alertinner p strong")
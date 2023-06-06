from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.basket_btn), "Basket button is not presented"
        basket_button = self.browser.find_element(*ProductPageLocators.basket_btn)
        assert basket_button.is_enabled(), "Basket button is not clickable"
        basket_button.click()

    def get_code(self):
        assert self.solve_quiz_and_get_code(), "You couldn't get promo-code"

    def check_add(self):
        assert self.is_element_present(*ProductPageLocators.add_title), "There is no added-to-basket message"

    def check_product_name(self):
        product_name = self.element_text(*ProductPageLocators.prod_name)
        in_basket_name = self.element_text(*ProductPageLocators.in_bask_name)
        assert in_basket_name == product_name, "Product names in product page and basket are not the same"

    def check_price_title(self):
        assert self.is_element_present(*ProductPageLocators.price_title), "Basket price title is not presented"

    def check_product_price(self):
        product_price = self.element_text(*ProductPageLocators.prod_price)
        in_basket_price = self.element_text(*ProductPageLocators.in_bask_price)
        assert in_basket_price == product_price, "Product price in product page and basket are not the same"

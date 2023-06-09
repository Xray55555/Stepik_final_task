from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.product_title), "Basket is empty"

    def no_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.no_product_title), "Basket contains product(s)"
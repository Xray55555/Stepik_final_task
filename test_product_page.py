import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

@pytest.mark.login_guest_product
class TestLoginFromProductPage():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

@pytest.mark.basket_guest
class TestGuestAddToBasketFromProductPage():

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()    
        page.add_to_basket()
        page.check_add()
        page.check_product_name()
        page.check_price_title()
        page.check_product_price()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)   
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        #basket_page.product_in_basket()  - закомментировано для успешного прохождения теста
        basket_page.no_product_in_basket()
    
    def test_guest_can_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)   
        page.open()
        page.add_to_basket() # добавляем товар в корзину для инверта ассертов
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.product_in_basket()
        #basket_page.no_product_in_basket() - закомментировано для успешного прохождения теста

@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "superpass!!!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()    
        page.add_to_basket()
        page.check_add()
        page.check_product_name()
        page.check_price_title()
        page.check_product_price()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)   
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        #basket_page.product_in_basket()  - закомментировано для успешного прохождения теста
        basket_page.no_product_in_basket()
    
    def test_user_can_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)   
        page.open()
        page.add_to_basket() # добавляем товар в корзину для инверта ассертов
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.product_in_basket()
        #basket_page.no_product_in_basket() - закомментировано для успешного прохождения теста

@pytest.mark.basket_guest_negative
@pytest.mark.xfail(reason="This test should fails according to the conditions of the task 4_3_6")
class TestGuestAddToBasketFromProductPageNegative():

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()    
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()    
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()    
        page.add_to_basket()
        page.should_disappeared()
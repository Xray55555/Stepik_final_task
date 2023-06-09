import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()    
    page.add_to_basket()
    #page.get_code()
    page.check_add()
    page.check_product_name()
    page.check_price_title()
    page.check_product_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)   
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    #basket_page.product_in_basket()  - закомментировано для успешного прохождения теста
    basket_page.no_product_in_basket()
    
#@pytest.mark.new
def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)   
    page.open()
    page.add_to_basket() # в отличие от предыдущего теста тут добавляем товар в корзину для инверта ассертов
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.product_in_basket()
    #basket_page.no_product_in_basket() - закомментировано для успешного прохождения теста
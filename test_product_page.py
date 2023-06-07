import pytest
from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
@pytest.mark.xfail(reason="Bug in this promo-link")
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()    
    page.add_to_basket()
    page.get_code()
    page.check_add()
    page.check_product_name()
    page.check_price_title()
    page.check_product_price()

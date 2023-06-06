from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()    
    page.add_to_basket()
    page.get_code()
    page.check_add()
    page.check_product_name()
    page.check_price_title()
    page.check_product_price()

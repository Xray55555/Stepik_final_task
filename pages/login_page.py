from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Login link goes to wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)

        assert self.is_element_present(*LoginPageLocators.PASS_FIELD1), "1st password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASS_FIELD1).send_keys(password)

        assert self.is_element_present(*LoginPageLocators.PASS_FIELD2), "2nd password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASS_FIELD2).send_keys(password)

        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Register button is not presented"
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BTN)
        assert reg_button.is_enabled(), "Register button is not clickable"
        reg_button.click()
        
        assert self.is_element_present(*LoginPageLocators.REG_SUCCESS), "There is no registration success message"
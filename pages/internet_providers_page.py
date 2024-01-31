from locators.base_page_locators import BasePageSbp, InternetProviders
from pages.base_page import BasePage


class AddressPlaceholder(BasePage):
    def fill_in_the_address(self):
        self.element_is_visible(BasePageSbp.WRITE_THE_STREET).send_keys('Тестовая линия')
        self.element_is_visible(BasePageSbp.CLICK_ON_THE_STREET).click()
        self.element_is_visible(BasePageSbp.WRITE_THE_HOUSE).send_keys('1')
        self.element_is_visible(BasePageSbp.CLICK_ON_THE_HOUSE).click()
        self.element_is_visible(BasePageSbp.SELECT_CONNECTION_TYPE).click()
        self.element_is_visible(BasePageSbp.CLICK_ON_CONNECTION_TYPE).click()
        self.element_is_visible(BasePageSbp.SHOW_RATES).click()


class ApplicationForInternetConnection(BasePage):

    def create_application(self):
        self.element_is_visible(InternetProviders.CLOSE_ADVERTISING).click()
        for items in range(5):
            self.element_is_visible(InternetProviders.CONNECT_THE_INTERTNET).click()
            self.element_is_visible(InternetProviders.WRITE_MOBILE_PHONE).send_keys('1111111111')
            self.element_is_visible(InternetProviders.SUBMIT_MY_APPLICATION).click()
            self.element_is_visible(InternetProviders.CLICK_ON_THANK_YOU).click()
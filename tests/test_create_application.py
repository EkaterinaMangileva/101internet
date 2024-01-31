from pages.internet_providers_page import AddressPlaceholder, ApplicationForInternetConnection


class TestOneHundredInternet:

    def test_application(self, driver):
        internet_page = AddressPlaceholder(driver, "https://piter-online.net/")
        internet_page.open()
        internet_page.fill_in_the_address()
        internet_providers = ApplicationForInternetConnection(driver,
                                                              "https://piter-online.net/leningradskaya-oblast/rates")
        internet_providers.create_application()

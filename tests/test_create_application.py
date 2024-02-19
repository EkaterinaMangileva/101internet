from pages.internet_providers_page import AddressPlaceholder, ApplicationForInternetConnection
import telebot

bot = telebot.TeleBot("6528485256:AAFr27qVMMB-A_Ig_YeX3DSK-kvWBr-TR3U")
chat_id = 456437503


class TestOneHundredInternet:

    def test_application(self, driver):
        try:
            internet_page = AddressPlaceholder(driver, "https://piter-online.net/")
            internet_page.open()
            internet_page.fill_in_the_address()
            internet_providers = ApplicationForInternetConnection(driver,
                                                                  "https://piter-online.net/leningradskaya-oblast/rates")
            internet_providers.create_application()
        finally:
            bot.send_message(chat_id, "Заявки отправлены, отчет смотри здесь")

    def test_second_ap(self, driver):
        try:
            internet_page = AddressPlaceholder(driver, "https://piter-online.net/")
            internet_page.open()
            internet_page.fill_in_the_address()
        finally:
            bot.send_message(chat_id, "Заявки отправлены, отчет смотри здесь")

    def test_third(self):
        assert 1 == 2

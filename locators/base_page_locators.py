from selenium.webdriver.common.by import By
from random import randint


class BasePageSbp:
    WRITE_THE_STREET = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[1]")
    CLICK_ON_THE_STREET = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    WRITE_THE_HOUSE = (By.XPATH, "(//input[@datatest='main_input_street_home_new'])[2]")
    CLICK_ON_THE_HOUSE = (By.XPATH, "//li[@datatest='dropdown_list_main']")
    SELECT_CONNECTION_TYPE = (By.XPATH, "(//input[@value='В квартиру '])[1]")
    CLICK_ON_CONNECTION_TYPE = (By.XPATH, "(//Li[@class='app193'])[1]")
    SHOW_RATES = (By.XPATH, "(//div[contains(text(), 'показать тарифы')])[1]")


class InternetProviders:
    CLOSE_ADVERTISING = (By.XPATH, "//div[@datatest='close_popup1_from_quiz_input_tel']")
    CONNECT_THE_INTERTNET = (By.XPATH, f"(//span[contains(text(), 'Подключить')])[{randint(0, 30)}]")
    WRITE_MOBILE_PHONE = (By.XPATH, "(//input[@type='tel'])[2]")
    SUBMIT_MY_APPLICATION = (By.XPATH, "//div[contains(text(), 'Оставить заявку')]")
    CLICK_ON_THANK_YOU = (By.XPATH, "//div[contains(text(), 'Спасибо!')]")

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sign_up_page import SignUpPage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.sign_up_page = SignUpPage(driver)
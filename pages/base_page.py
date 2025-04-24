from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_main_page(self, url="https://soft.reelly.io"):
        self.driver.get(url)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()

    def login(self, email, password):
        email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        continue_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'login-button') and text()='Continue']")))
        email_input.send_keys(email)
        password_input.send_keys(password)
        continue_btn.click()

    def click_off_plan(self):
        try:
            off_plan_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class, 'g-menu-text') and text()='Off-plan']")))
            off_plan_btn.click()
        except:
            raise Exception("❌ Off-plan button not clickable.")

    def filter_by_out_of_stock(self):
        try:
            filter_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Sale status']")))
            filter_button.click()
            out_of_stock_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Out of Stocks']")))
            out_of_stock_option.click()
        except:
            raise Exception("❌ Could not apply Out of Stocks filter.")

    def verify_all_products_out_of_stock(self):
        products = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class, 'tag') and text()='Out of Stocks']")))
        assert len(products) > 0, "❌ No products marked as 'Out of Stocks'"
from app.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def browser_init(context):
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

def before_scenario(context, scenario):
    print(f"\nStarted scenario: {scenario.name}")
    browser_init(context)
    context.app = Application(context.driver)

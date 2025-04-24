from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)  # Initialize the base page

def browser_init(context):
    """Start a fresh browser instance on the context."""
    driver_path = ChromeDriverManager().install()  # Install driver
    service = Service(driver_path)  # Get driver service
    context.driver = webdriver.Chrome(service=service)  # Initialize the driver
    context.driver.maximize_window()  # Maximize the browser window
    context.driver.implicitly_wait(10)  # Global implicit wait for elements

def before_scenario(context, scenario):
    """Runs before each scenario."""
    print(f"\nStarted scenario: {scenario.name}")
    browser_init(context)  # Initialize browser and attach to context
    context.app = Application(context.driver)  # Attach Application instance to context

def before_step(context, step):
    """Runs before each step."""
    print(f"Started step: {step.name}")

def after_step(context, step):
    """Runs after each step."""
    if step.status == 'failed':
        print(f"Step failed: {step.name}")
        context.driver.save_screenshot(f"failure_screenshot_{step.name}.png")  # Screenshot on failure

def after_scenario(context, scenario):
    """Runs after each scenario."""
    if hasattr(context, 'driver'):
        context.driver.quit()  # Ensure the driver is closed after each scenario



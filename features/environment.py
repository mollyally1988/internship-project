from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from support.logger import logger

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    #BrowserStack
   # bs_user = 'alinadorofeyeva_7fPT6J'
   # bs_key = 'XqWykR2vLcmYu6UU7pGu'
   # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
   # options = Options()
   # bstack_options = {
   #      "os": "Windows",
   #      "osVersion": "11",
   #      'browserName': 'chrome',
   #      'sessionName': scenario_name,
   #  }
   # options.set_capability('bstack:options', bstack_options)
   # context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)

    # Set up app object
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

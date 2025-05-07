from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from support.logger import logger

from app.application import Application

#Command to run tests with Allure & Behave:
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature
def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    #BrowserStack from https://www.browserstack.com/accounts/settings
    bs_user = 'alinadorofeyeva_7fPT6J'
    bs_key = 'XqWykR2vLcmYu6UU7pGu'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {

        "os": "Windows",
        "osVersion": "13.0",
        "deviceName": "Google Pixel 7",
        "realMobile": "true",
        "browserName": 'chrome',
        "sessionName": scenario_name,
        # "interactiveDebugging" : True,

   #      "os": "Windows",
   #      "osVersion": "11",
   #      'browserName': 'chrome',
   #      'sessionName': scenario_name,
     }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)

    # Set up app object
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed {step}')
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()

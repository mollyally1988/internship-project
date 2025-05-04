#from behave import given, when, then
#from selenium import webdriver
#from pages.base_page import BasePage

#@given("the user is on the main page")
#def step_open_main_page(context):
 #   context.driver = webdriver.Chrome()
  #  context.app = BasePage(context.driver)
   # context.app.go_to_main_page()

#@when("the user logs in")
#def step_user_logs_in(context):
 #   context.app.login(email="********", password="******")

#@when('the user clicks on "Off-plan" in the menu')
#def step_click_off_plan(context):
 #   context.app.click_off_plan()

#@then("the correct page should open")
#def step_check_off_plan_opened(context):
 #   assert "off-plan" in context.driver.current_url, "❌ Off-plan page did not open."

#@when('the user filters by "Out of Stocks"')
#def step_filter_out_of_stocks(context):
 #   context.app.filter_by_out_of_stock()
#
#@then('all listed products should be marked as "Out of Stocks"')
#def step_verify_out_of_stock_products(context):
#    context.app.verify_all_products_out_of_stock()
 #   context.driver.quit()
from behave import given, when, then


@given('the user is on the sign-up page')
def open_sign_up_page(context):
    context.app.sign_up_page.open_sign_up_page()


@when('fill out the form')
def fill_out_form(context):
    context.app.sign_up_page.fill_out_form()


@when('click create account button')
def click_create_account_btn(context):
    context.app.sign_up_page.click_create_account_btn()

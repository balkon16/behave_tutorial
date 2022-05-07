import requests

from behave import *


@given('I open the home page')
def step_impl(context):
    assert True


@then('I get a general greeting')
def step_impl(context):
    resp = requests.get("http://localhost:5000")
    print(resp.text)
    assert resp.text == "<h1>Hello! Testing `behave`</h1>"

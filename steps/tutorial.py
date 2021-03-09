from behave import *
import requests
from datetime import date

@given('today is {day}')
def step_impl(context, day):
    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    today = date.today()
    assert today.weekday() is days[day]

@when('I request the BBC homepage')
def step_impl(context):
    context.response = requests.get('https://cosmos.tools.bbc.co.uk/')

@then('the I should get a 200 response')
def step_impl(context):
    assert context.response.status_code is 200

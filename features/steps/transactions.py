from behave import *

from models.transaction import Transaction, TransactionSet


@given('a set of transactions')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = TransactionSet()
    for row in context.table:
        context.model.add_transaction(Transaction(int(row["transaction ID"]), row["name"], row["status"]))


@when('I count the number of transactions by type')
def step_impl(context):
    context.summary = context.model.get_summary_by_status()


@then('I get 2 transactions with a status "completed"')
def step_impl(context):
    assert context.summary['completed'] == 2


@then('I get 1 transaction with a status "in progress"')
def step_impl(context):
    assert context.summary['in progress'] == 1

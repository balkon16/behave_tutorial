from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello! Testing `behave`</h1>"


@app.route("/transactions/<transaction_id>")
def get_transaction(transaction_id):
    completed_transactions = set(range(1, 10))
    try:
        transaction_id = int(transaction_id)
        if transaction_id in completed_transactions:
            msg = f"Found transaction no. {transaction_id}."
        else:
            msg = f"Transaction no. {transaction_id} does not exist."

    except ValueError:
        msg = "Incorrect value for a transaction."

    return f"<p>Server response: {msg}<p>"

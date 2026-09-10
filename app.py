from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get(
    "DB_URL", "sqlite:///bank.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# db is package and Model is class
# Here BankAccount is inheriting Model class
class BankAccount(db.Model):
    __tablename__ = "bank_accounts"

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    account_holder = db.Column(db.String(100), nullable=False)
    account_type = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)

    def json(self):
        return {
            "id": self.id,
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "account_type": self.account_type,
            "balance": self.balance
        }


with app.app_context():
    db.create_all()


@app.route("/test", methods=["GET"])
def test():
    return make_response(
        jsonify({"message": "Bank Management System is working"}),
        200
    )


# Create a new bank account
@app.route("/accounts", methods=["POST"])
def create_account():
    try:
        data = request.get_json()

        if not data or "account_number" not in data or "account_holder" not in data or "account_type" not in data:
            return make_response(
                jsonify({
                    "message": "account_number, account_holder and account_type are required"
                }),
                400
            )

        new_account = BankAccount(
            account_number=data["account_number"],
            account_holder=data["account_holder"],
            account_type=data["account_type"],
            balance=data.get("balance", 0.0)
        )

        db.session.add(new_account)
        db.session.commit()

        return make_response(
            jsonify({"message": "bank account created"}),
            201
        )

    except Exception:
        return make_response(
            jsonify({"message": "error creating bank account"}),
            500
        )


# Get all bank accounts
@app.route("/accounts", methods=["GET"])
def get_accounts():
    try:
        accounts = BankAccount.query.all()

        return make_response(
            jsonify([account.json() for account in accounts]),
            200
        )

    except Exception:
        return make_response(
            jsonify({"message": "error getting accounts"}),
            500
        )


# Get a particular bank account
@app.route("/accounts/<int:id>", methods=["GET"])
def get_account(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if account:
            return make_response(
                jsonify({"account": account.json()}),
                200
            )

        return make_response(
            jsonify({"message": "account not found"}),
            404
        )

    except Exception:
        return make_response(
            jsonify({"message": "error getting account"}),
            500
        )


# Update bank account details
@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if not account:
            return make_response(
                jsonify({"message": "account not found"}),
                404
            )

        data = request.get_json()

        if not data:
            return make_response(
                jsonify({"message": "no data provided"}),
                400
            )

        account.account_number = data.get(
            "account_number",
            account.account_number
        )

        account.account_holder = data.get(
            "account_holder",
            account.account_holder
        )

        account.account_type = data.get(
            "account_type",
            account.account_type
        )

        db.session.commit()

        return make_response(
            jsonify({"message": "account updated"}),
            200
        )

    except Exception:
        return make_response(
            jsonify({"message": "error updating account"}),
            500
        )


# Delete bank account
@app.route("/accounts/<int:id>", methods=["DELETE"])
def delete_account(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if account:
            db.session.delete(account)
            db.session.commit()

            return make_response(
                jsonify({"message": "account deleted"}),
                200
            )

        return make_response(
            jsonify({"message": "account not found"}),
            404
        )

    except Exception:
        return make_response(
            jsonify({"message": "error deleting account"}),
            500
        )


# Deposit money
@app.route("/accounts/<int:id>/deposit", methods=["PUT"])
def deposit_money(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if not account:
            return make_response(
                jsonify({"message": "account not found"}),
                404
            )

        data = request.get_json()

        if not data or "amount" not in data:
            return make_response(
                jsonify({"message": "amount is required"}),
                400
            )

        amount = float(data["amount"])

        if amount <= 0:
            return make_response(
                jsonify({"message": "deposit amount must be greater than zero"}),
                400
            )

        account.balance += amount

        db.session.commit()

        return make_response(
            jsonify({
                "message": "money deposited successfully",
                "balance": account.balance
            }),
            200
        )

    except Exception:
        return make_response(
            jsonify({"message": "error depositing money"}),
            500
        )


# Withdraw money
@app.route("/accounts/<int:id>/withdraw", methods=["PUT"])
def withdraw_money(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if not account:
            return make_response(
                jsonify({"message": "account not found"}),
                404
            )

        data = request.get_json()

        if not data or "amount" not in data:
            return make_response(
                jsonify({"message": "amount is required"}),
                400
            )

        amount = float(data["amount"])

        if amount <= 0:
            return make_response(
                jsonify({"message": "withdraw amount must be greater than zero"}),
                400
            )

        if amount > account.balance:
            return make_response(
                jsonify({"message": "insufficient balance"}),
                400
            )

        account.balance -= amount

        db.session.commit()

        return make_response(
            jsonify({
                "message": "money withdrawn successfully",
                "balance": account.balance
            }),
            200
        )

    except Exception:
        return make_response(
            jsonify({"message": "error withdrawing money"}),
            500
        )


# Check balance
@app.route("/accounts/<int:id>/balance", methods=["GET"])
def check_balance(id):
    try:
        account = BankAccount.query.filter_by(id=id).first()

        if not account:
            return make_response(
                jsonify({"message": "account not found"}),
                404
            )

        return make_response(
            jsonify({
                "account_number": account.account_number,
                "account_holder": account.account_holder,
                "balance": account.balance
            }),
            200
        )

    except Exception:
        return make_response(
            jsonify({"message": "error checking balance"}),
            500
        )


if __name__ == "__main__":
    app.run(debug=True)
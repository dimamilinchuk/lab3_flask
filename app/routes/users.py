from flask import Blueprint, request, jsonify
from app.models import User, db, Account, Currency
from app.schemas import DepositSchema, UserSchema
from marshmallow import ValidationError

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    schema = UserSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create the user
    user = User(name=validated_data['name'], default_currency_id=validated_data['default_currency_id'])
    db.session.add(user)
    db.session.commit()

    # Create the account for the user
    account = Account(user_id=user.id, currency_id=validated_data['default_currency_id'])
    db.session.add(account)
    db.session.commit()

    return jsonify({"id": user.id, "name": user.name, "default_currency_id": user.default_currency_id}), 201


@bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users]), 200


@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name}), 200


@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    schema = UserSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = User.query.get_or_404(user_id)

    # Currency validation logic
    if 'default_currency_id' in validated_data:
        new_currency = Currency.query.get_or_404(validated_data['default_currency_id'])
        if user.account.balance != 0.0:
            return jsonify({"error": "Cannot change currency with non-zero balance"}), 400
        user.account.currency = new_currency
        user.default_currency = new_currency

    # Update other user fields if needed
    if 'name' in validated_data:
        user.name = validated_data['name']

    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "default_currency_id": user.default_currency_id}), 200


@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200

@bp.route('/<int:user_id>/deposit', methods=['POST'])
def deposit(user_id):
    data = request.get_json()
    schema = DepositSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user = User.query.get_or_404(user_id)
    account = Account.query.filter_by(user_id=user.id).first_or_404()
    
    if validated_data['currency_id'] != account.currency_id:
        return jsonify({"error": "Currency does not match account's currency"}), 400
    
    account.balance += validated_data['amount']
    db.session.commit()
    
    return jsonify({
        "user_id": user.id,
        "balance": account.balance,
        "currency_id": account.currency_id
    }), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_account(user_id):
    account = Account.query.filter_by(user_id=user_id).first_or_404()
    return jsonify({
        "user_id": account.user_id,
        "balance": account.balance,
        "currency_id": account.currency_id
    }), 200

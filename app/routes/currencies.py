from flask import Blueprint, request, jsonify
from app.models import Currency, User, db

bp = Blueprint('currencies', __name__, url_prefix='/currencies')

@bp.route('/', methods=['POST'])
def create_currency():
    data = request.json
    currency = Currency(code=data['code'], name=data['name'])
    db.session.add(currency)
    db.session.commit()
    return jsonify({"id": currency.id, "code": currency.code, "name": currency.name}), 201

@bp.route('/', methods=['GET'])
def get_currencies():
    currencies = Currency.query.all()
    return jsonify([{"id": currency.id, "code": currency.code, "name": currency.name} for currency in currencies]), 200

@bp.route('/<int:currency_id>', methods=['GET'])
def get_currency(currency_id):
    currency = Currency.query.get_or_404(currency_id)
    return jsonify({"id": currency.id, "code": currency.code, "name": currency.name}), 200

@bp.route('/<int:currency_id>', methods=['PUT'])
def update_currency(currency_id):
    data = request.json
    currency = Currency.query.get_or_404(currency_id)
    currency.code = data['code']
    currency.name = data['name']
    db.session.commit()
    return jsonify({"id": currency.id, "code": currency.code, "name": currency.name}), 200

@bp.route('/<int:currency_id>', methods=['DELETE'])
def delete_currency(currency_id):
    currency = Currency.query.get_or_404(currency_id)
    db.session.delete(currency)
    db.session.commit()
    return jsonify({"message": "Currency deleted"}), 200
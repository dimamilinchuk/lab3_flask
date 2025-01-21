from flask import Blueprint, request, jsonify
from app.models import Record, User, Category, db

bp = Blueprint('records', __name__, url_prefix='/records')

@bp.route('/', methods=['POST'])
def create_record():
    data = request.json
    user = User.query.get_or_404(data['user_id'])
    category = Category.query.get_or_404(data['category_id'])
    record = Record(
        user_id=user.id,
        category_id=category.id,
        amount=data['amount'],
        currency_id=data.get('currency_id', user.default_currency_id)
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({"id": record.id, "amount": record.amount}), 201

@bp.route('/', methods=['GET'])
def get_records():
    records = Record.query.all()
    return jsonify([
        {
            "id": record.id,
            "user_id": record.user_id,
            "category_id": record.category_id,
            "amount": record.amount,
            "currency_id": record.currency_id
        } for record in records
    ]), 200

@bp.route('/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = Record.query.get_or_404(record_id)
    return jsonify({
        "id": record.id,
        "user_id": record.user_id,
        "category_id": record.category_id,
        "amount": record.amount,
        "currency_id": record.currency_id
    }), 200

@bp.route('/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    data = request.json
    record = Record.query.get_or_404(record_id)
    record.amount = data['amount']
    record.category_id = data['category_id']
    record.currency_id = data.get('currency_id', record.currency_id)
    db.session.commit()
    return jsonify({"id": record.id, "amount": record.amount}), 200

@bp.route('/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    record = Record.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Record deleted"}), 200
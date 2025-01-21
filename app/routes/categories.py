from flask import Blueprint, request, jsonify
from app.models import Category, db

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({"id": category.id, "name": category.name}), 201

@bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{"id": category.id, "name": category.name} for category in categories]), 200

@bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify({"id": category.id, "name": category.name}), 200

@bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    category = Category.query.get_or_404(category_id)
    category.name = data['name']
    db.session.commit()
    return jsonify({"id": category.id, "name": category.name}), 200

@bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"}), 200
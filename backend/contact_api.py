from flask import Blueprint, request, jsonify
from models import Contact, db

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    required_fields = ['name', 'email', 'phone', 'address', 'message']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    contact = Contact(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        message=data['message']
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({'message': 'Contact form submitted successfully!'}), 201

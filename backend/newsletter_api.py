from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import NewsletterSubscriber, db

newsletter_api = Blueprint('newsletter_api', __name__)

@newsletter_api.route('/api/newsletter/subscribe', methods=['POST', 'OPTIONS'])
@cross_origin()
def subscribe():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required.'}), 400
    email = data['email'].strip().lower()
    if not email:
        return jsonify({'error': 'Email cannot be empty.'}), 400
    # Check if already subscribed
    if NewsletterSubscriber.query.filter_by(email=email).first():
        return jsonify({'message': 'Already subscribed.'}), 200
    try:
        subscriber = NewsletterSubscriber(email=email)
        db.session.add(subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscribed successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

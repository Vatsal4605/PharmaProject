from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from models import Contact, NewsletterSubscriber, db

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/api/contact', methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()
def contact():
    print("Received request:", request.method)
    
    if request.method == 'OPTIONS':
        print("Handling OPTIONS request")
        return jsonify({}), 200
        
    if request.method == 'GET':
        return jsonify({'message': 'GET not supported on this endpoint. Please use POST.'}), 405
        
    try:
        print("Getting JSON data from request")
        data = request.get_json()
        print("Received data:", data)
        
        required_fields = ['name', 'email', 'phone', 'address', 'message']
        if not data or not all(field in data for field in required_fields):
            missing_fields = [field for field in required_fields if not data or field not in data]
            print(f"Error: Missing required fields: {missing_fields}")
            return jsonify({'error': f'Missing required fields: {missing_fields}'}), 400

        print("Creating new contact")
        contact = Contact(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            message=data['message']
        )
        
        print("Adding to database")
        db.session.add(contact)
        db.session.commit()
        print("Successfully saved to database")
        
        return jsonify({'message': 'Contact form submitted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        import traceback
        print("Traceback:", traceback.format_exc())
        return jsonify({'error': error_msg}), 500
    
    return jsonify({'error': 'Method Not Allowed'}), 405

@contact_api.route('/api/newsletter', methods=['POST', 'OPTIONS'])
@cross_origin()
def subscribe_newsletter():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    try:
        data = request.get_json()
        email = data.get('email')
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        # Check if already subscribed
        if NewsletterSubscriber.query.filter_by(email=email).first():
            return jsonify({'message': 'Already subscribed!'}), 200
        subscriber = NewsletterSubscriber(email=email)
        db.session.add(subscriber)
        db.session.commit()
        return jsonify({'message': 'Subscribed successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

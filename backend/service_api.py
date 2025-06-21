from flask import Blueprint, request, jsonify
from models import db, Service
from datetime import datetime

service_api = Blueprint('service_api', __name__, url_prefix='/api/services')

@service_api.route('/', methods=['GET'])
def get_services():
    """Get all services"""
    try:
        services = Service.query.order_by(Service.created_at.desc()).all()
        services_list = []
        for service in services:
            services_list.append({
                'id': service.id,
                'title': service.title,
                'description': service.description,
                'image_path': service.image_path,
                'created_at': service.created_at.isoformat() if service.created_at else None
            })
        return jsonify({'services': services_list, 'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@service_api.route('/<int:service_id>', methods=['GET'])
def get_service(service_id):
    """Get a specific service by ID"""
    try:
        service = Service.query.get_or_404(service_id)
        return jsonify({
            'service': {
                'id': service.id,
                'title': service.title,
                'description': service.description,
                'image_path': service.image_path,
                'created_at': service.created_at.isoformat() if service.created_at else None
            },
            'success': True
        }), 200
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@service_api.route('/', methods=['POST'])
def create_service():
    """Create a new service"""
    try:
        data = request.get_json()
        
        if not data or not data.get('title') or not data.get('description') or not data.get('image_path'):
            return jsonify({'error': 'Title, description, and image_path are required', 'success': False}), 400
        
        new_service = Service(
            title=data['title'],
            description=data['description'],
            image_path=data['image_path']
        )
        
        db.session.add(new_service)
        db.session.commit()
        
        return jsonify({
            'service': {
                'id': new_service.id,
                'title': new_service.title,
                'description': new_service.description,
                'image_path': new_service.image_path,
                'created_at': new_service.created_at.isoformat() if new_service.created_at else None
            },
            'success': True,
            'message': 'Service created successfully'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e), 'success': False}), 500

@service_api.route('/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    """Update a service"""
    try:
        service = Service.query.get_or_404(service_id)
        data = request.get_json()
        
        if data.get('title'):
            service.title = data['title']
        if data.get('description'):
            service.description = data['description']
        if data.get('image_path'):
            service.image_path = data['image_path']
        
        db.session.commit()
        
        return jsonify({
            'service': {
                'id': service.id,
                'title': service.title,
                'description': service.description,
                'image_path': service.image_path,
                'created_at': service.created_at.isoformat() if service.created_at else None
            },
            'success': True,
            'message': 'Service updated successfully'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e), 'success': False}), 500

@service_api.route('/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    """Delete a service"""
    try:
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Service deleted successfully'
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e), 'success': False}), 500 
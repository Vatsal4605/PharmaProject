from flask import Blueprint, request, jsonify
from models import db, Research
from datetime import datetime

research_api = Blueprint('research_api', __name__)

@research_api.route('/api/research', methods=['GET'])
def get_research():
    """Get all research items"""
    try:
        research_items = Research.query.order_by(Research.created_at.desc()).all()
        research_list = []
        
        for item in research_items:
            research_list.append({
                'id': item.id,
                'heading': item.heading,
                'description': item.description,
                'category': item.category,
                'date': item.date,
                'image_link': item.image_link,
                'external_link': item.external_link,
                'created_at': item.created_at.isoformat() if item.created_at else None
            })
        
        return jsonify({
            'success': True,
            'data': research_list,
            'message': 'Research items retrieved successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving research items: {str(e)}'
        }), 500

@research_api.route('/api/research', methods=['POST'])
def add_research():
    """Add a new research item"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['heading', 'description', 'category', 'date', 'image_link']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    'success': False,
                    'message': f'Missing required field: {field}'
                }), 400
        
        # Create new research item
        new_research = Research(
            heading=data['heading'],
            description=data['description'],
            category=data['category'],
            date=data['date'],
            image_link=data['image_link'],
            external_link=data.get('external_link', None)
        )
        
        db.session.add(new_research)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Research item added successfully',
            'data': {
                'id': new_research.id,
                'heading': new_research.heading,
                'description': new_research.description,
                'category': new_research.category,
                'date': new_research.date,
                'image_link': new_research.image_link,
                'external_link': new_research.external_link,
                'created_at': new_research.created_at.isoformat() if new_research.created_at else None
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error adding research item: {str(e)}'
        }), 500

@research_api.route('/api/research/<int:research_id>', methods=['PUT'])
def update_research(research_id):
    """Update a research item"""
    try:
        research = Research.query.get(research_id)
        if not research:
            return jsonify({
                'success': False,
                'message': 'Research item not found'
            }), 404
        
        data = request.get_json()
        
        # Update fields if provided
        if 'heading' in data:
            research.heading = data['heading']
        if 'description' in data:
            research.description = data['description']
        if 'category' in data:
            research.category = data['category']
        if 'date' in data:
            research.date = data['date']
        if 'image_link' in data:
            research.image_link = data['image_link']
        if 'external_link' in data:
            research.external_link = data['external_link']
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Research item updated successfully',
            'data': {
                'id': research.id,
                'heading': research.heading,
                'description': research.description,
                'category': research.category,
                'date': research.date,
                'image_link': research.image_link,
                'external_link': research.external_link,
                'created_at': research.created_at.isoformat() if research.created_at else None
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error updating research item: {str(e)}'
        }), 500

@research_api.route('/api/research/<int:research_id>', methods=['DELETE'])
def delete_research(research_id):
    """Delete a research item"""
    try:
        research = Research.query.get(research_id)
        if not research:
            return jsonify({
                'success': False,
                'message': 'Research item not found'
            }), 404
        
        db.session.delete(research)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Research item deleted successfully'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error deleting research item: {str(e)}'
        }), 500 
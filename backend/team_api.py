from flask import Blueprint, jsonify
from models import TeamMember

team_api = Blueprint('team_api', __name__, url_prefix='/api')

@team_api.route('/team', methods=['GET'])
def get_team():
    try:
        members = TeamMember.query.all()
        members_list = []
        for member in members:
            members_list.append({
                'id': member.id,
                'name': member.name,
                'role': member.role,
                'image_path': member.image_path,
                'instagram_link': member.instagram_link,
                'facebook_link': member.facebook_link,
                'twitter_link': member.twitter_link
            })
        return jsonify({'team': members_list, 'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500 
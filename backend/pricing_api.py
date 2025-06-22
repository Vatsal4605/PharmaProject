# backend/pricing_api.py
from flask import Blueprint, jsonify
from models import PricePackage

pricing_api = Blueprint('pricing_api', __name__)

@pricing_api.route('/api/pricing', methods=['GET'])
def get_pricing_packages():
    """Retrieves all pricing packages from the database."""
    try:
        packages = PricePackage.query.all()
        package_list = [
            {
                "id": pkg.id,
                "name": pkg.name,
                "description": pkg.description,
                "price": pkg.price,
                "benefits": pkg.benefits.split('|'),
                "get_started_link": pkg.get_started_link
            }
            for pkg in packages
        ]
        return jsonify(package_list)
    except Exception as e:
        print(f"Error fetching pricing packages: {e}")
        return jsonify({"error": "Could not retrieve pricing packages"}), 500 
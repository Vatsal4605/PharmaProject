from app import app
from models import db, Service

with app.app_context():
    new_service = Service(
        title='Premium Plan',
        description='Unlock all features with the Premium Plan including full support.',
        image_path='https://via.placeholder.com/150'  # Replace if needed
    )
    db.session.add(new_service)
    db.session.commit()
    print("✅ Dummy service added successfully.")

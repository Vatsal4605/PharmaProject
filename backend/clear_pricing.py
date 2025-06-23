from app import app, db
from models import PricePackage

def clear_pricing_packages():
    with app.app_context():
        num_deleted = PricePackage.query.delete()
        db.session.commit()
        print(f"Deleted {num_deleted} pricing packages.")

if __name__ == '__main__':
    clear_pricing_packages() 
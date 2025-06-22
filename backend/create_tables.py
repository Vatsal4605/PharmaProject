from app import app, db
from models import Blog, Contact, NewsletterSubscriber, Service, TeamMember, PricePackage

def create_tables():
    """Drops all existing tables and creates new ones based on the models."""
    with app.app_context():
        print("Dropping all database tables...")
        db.drop_all()
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    create_tables() 
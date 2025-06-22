from app import app, db
from models import Blog, Contact, Newsletter, Service, TeamMember

def create_tables():
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    create_tables() 
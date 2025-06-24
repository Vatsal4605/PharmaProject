from app import app, db
from models import Service

def add_sample_services():
    with app.app_context():
        # Check if services already exist to avoid duplicates and data loss
        if Service.query.first() is not None:
            print("Services already exist. Skipping population.")
            return
        
        # Sample services data with actual images from service_images folder
        sample_services = [
            {
                'title': 'Diagnostic Testing',
                'description': 'Comprehensive diagnostic testing services for accurate disease detection and monitoring.',
                'image_path': 'assets/service_images/diagnostic.webp'
            },
            {
                'title': 'Laboratory Services',
                'description': 'State-of-the-art laboratory services with advanced equipment and expert technicians.',
                'image_path': 'assets/service_images/laboratory.webp'
            },
            {
                'title': 'Clinical Research',
                'description': 'Cutting-edge clinical research services to advance medical knowledge and treatments.',
                'image_path': 'assets/service_images/research.webp'
            },
            {
                'title': 'Molecular Testing',
                'description': 'Advanced molecular testing for genetic analysis and personalized medicine.',
                'image_path': 'assets/service_images/molecular.webp'
            },
            {
                'title': 'Data Analysis',
                'description': 'Comprehensive data analysis services for research and clinical decision support.',
                'image_path': 'assets/service_images/data.png'
            },
            {
                'title': 'Quality Control',
                'description': 'Rigorous quality control processes to ensure accuracy and reliability of all tests.',
                'image_path': 'assets/service_images/quality.png'
            }
        ]
        
        # Add services to database
        for service_data in sample_services:
            service = Service(**service_data)
            db.session.add(service)
        
        db.session.commit()
        print("Sample services added successfully!")
        print("Images used:")
        for service in sample_services:
            print(f"- {service['title']}: {service['image_path']}")

if __name__ == '__main__':
    add_sample_services() 
from app import app, db
from models import PricePackage

def add_sample_pricing_packages():
    with app.app_context():
        # Check if pricing packages already exist
        if PricePackage.query.first() is not None:
            print("Pricing packages already exist. Skipping population.")
            return

        # Sample pricing packages based on the existing HTML
        sample_packages = [
            {
                'name': 'Standard Package',
                'description': 'Id vitae nunc scelerisque et. Enim lobortis eu in ipsum.',
                'price': '₹499/month',
                'benefits': (
                    'Velit elementum lectus suspendisse facilisis.|'
                    'Interdum auctor molestie elementum egestas.|'
                    'Aliquam mauris neque sit tristique id pretium.'
                ),
                'get_started_link': 'contact.html'
            },
            {
                'name': 'Premium Package',
                'description': 'Id vitae nunc scelerisque et. Enim lobortis eu in ipsum.',
                'price': '₹699/month',
                'benefits': (
                    'Velit elementum lectus suspendisse facilisis.|'
                    'Interdum auctor molestie elementum egestas.|'
                    'Aliquet mauris neque sit tristique id pretium.|'
                    'Vel quis sollicitudin ultricies diam nec ut.'
                ),
                'get_started_link': 'contact.html'
            },
            {
                'name': 'Elite Package',
                'description': 'Id vitae nunc scelerisque et. Enim lobortis eu in ipsum.',
                'price': '₹899/month',
                'benefits': (
                    'Velit elementum lectus suspendisse facilisis.|'
                    'Interdum auctor molestie elementum egestas.|'
                    'Aliquam mauris neque sit tristique id pretium.|'
                    'Vel quis sollicitudin ultricies diam nec ut.|'
                    'Ut auctor nullam elementum volutpat.'
                ),
                'get_started_link': 'contact.html'
            }
        ]

        # Add each package to the database
        for package_data in sample_packages:
            package = PricePackage(**package_data)
            db.session.add(package)
            print(f"Added pricing package: {package_data['name']}")

        db.session.commit()
        print("Sample pricing packages added successfully!")

if __name__ == '__main__':
    add_sample_pricing_packages() 
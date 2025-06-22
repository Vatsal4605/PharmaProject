from app import app, db
from models import Research

def add_sample_research():
    with app.app_context():
        # Check if research data already exists
        existing_research = Research.query.first()
        if existing_research:
            print("Sample research data already exists. Skipping...")
            return

        # Sample research data based on the existing HTML
        sample_research = [
            {
                'heading': 'Advancing Gene Editing & Therapy',
                'description': 'Egestas lacinia malesuada tortor habitant quam eu pretium tempus. Elementum nisi sed vulputate sed.',
                'category': 'Biotechnology',
                'date': 'January 2024',
                'image_link': 'research_image/research1.webp',
                'external_link': 'https://example.com/gene-editing-research'
            },
            {
                'heading': 'Gene Expression & Mutation Analysis',
                'description': 'Odio blandit adipiscing natoque volutpat venenatis. Nec ultrices felis augue feugiat vitae.',
                'category': 'Genetics',
                'date': 'August 2024',
                'image_link': 'research_image/research2.webp',
                'external_link': 'https://example.com/gene-expression-research'
            },
            {
                'heading': 'Clinical Trials and Drug Development',
                'description': 'Quis lectus vestibulum mauris gravida sollicitudin feugiat ultricies. Enim donec ultrices aliquet duis interdum iaculis dignissim.',
                'category': 'Pharmacology',
                'date': 'September 2024',
                'image_link': 'research_image/research3.webp',
                'external_link': 'https://example.com/clinical-trials-research'
            },
            {
                'heading': 'Pollution Control for Ecosystem',
                'description': 'Viverra morbi magna ante in vitae aliquet eu. Nullam in massa et diam tristique et potenti.',
                'category': 'Environmental',
                'date': 'November 2024',
                'image_link': 'research_image/research4.webp',
                'external_link': 'https://example.com/pollution-control-research'
            }
        ]

        # Add each research item to the database
        for research_data in sample_research:
            research = Research(**research_data)
            db.session.add(research)
            print(f"Added research: {research_data['heading']}")

        db.session.commit()
        print("Sample research data added successfully!")

if __name__ == '__main__':
    add_sample_research() 
from app import app, db
from models import TeamMember

def add_team_members():
    """Adds sample team members to the database."""
    with app.app_context():
        db.create_all()

        # Check if there are any members already to avoid duplicates
        if TeamMember.query.count() > 0:
            print("Team members already exist. Skipping population.")
            return

        team_members = [
            {
                "name": "Dr. Evelyn Reed",
                "role": "Chief Scientist",
                "image_path": "assets/team_images/member1.webp",
                "instagram_link": "#",
                "facebook_link": "#",
                "twitter_link": "#"
            },
            {
                "name": "Dr. Marcus Chen",
                "role": "Lead Researcher",
                "image_path": "assets/team_images/member2.webp",
                "instagram_link": "#",
                "facebook_link": "#",
                "twitter_link": "#"
            },
            {
                "name": "Dr. Sofia Al-Jamil",
                "role": "Pharmacology Expert",
                "image_path": "assets/team_images/member3.webp",
                "instagram_link": "#",
                "facebook_link": "#",
                "twitter_link": "#"
            },
            {
                "name": "Dr. Ben Carter",
                "role": "Lab Director",
                "image_path": "assets/team_images/member4.webp",
                "instagram_link": "#",
                "facebook_link": "#",
                "twitter_link": "#"
            }
        ]

        for member_data in team_members:
            new_member = TeamMember(**member_data)
            db.session.add(new_member)

        try:
            db.session.commit()
            print("Successfully added sample team members.")
        except Exception as e:
            db.session.rollback()
            print(f"Failed to add team members: {e}")

if __name__ == '__main__':
    add_team_members() 
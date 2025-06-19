from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Example {self.name}>'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    message = db.Column(db.String(5000), nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'

class NewsletterSubscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)

    def __repr__(self):
        return f'<NewsletterSubscriber {self.email}>'

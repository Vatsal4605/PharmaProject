from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from contact_api import contact_api
from newsletter_api import newsletter_api
from blog_api import blog_api
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/pharmadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contact_api)
app.register_blueprint(newsletter_api)
app.register_blueprint(blog_api)

@app.route('/')
def home():
    return {'message': 'PharmaProject Flask API is running!'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

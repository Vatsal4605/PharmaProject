from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from contact_api import contact_api
from newsletter_api import newsletter_api
from blog_api import blog_api
from service_api import service_api
from team_api import team_api
from pricing_api import pricing_api
from research_api import research_api
import os

load_dotenv()

app = Flask(__name__)
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/pharmadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contact_api)
app.register_blueprint(newsletter_api)
app.register_blueprint(blog_api)
app.register_blueprint(service_api)
app.register_blueprint(team_api)
app.register_blueprint(pricing_api)
app.register_blueprint(research_api)

@app.route('/')
def home():
    return {'message': 'PharmaProject Flask API is running!'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5000, debug=True)

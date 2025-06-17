from flask import Flask
from dotenv import load_dotenv
from models import db
from contact_api import contact_api
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///pharmadb.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contact_api)

@app.route('/')
def home():
    return {'message': 'PharmaProject Flask API is running!'}

if __name__ == '__main__':
    app.run(debug=True)

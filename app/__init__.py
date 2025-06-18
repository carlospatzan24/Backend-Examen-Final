from flask import Flask
from flask_cors import CORS
from .config import Config
from .models import db
from .schemas import ma
from .routes import contact_bp, reasons_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(contact_bp)
    app.register_blueprint(reasons_bp)
    
    return app
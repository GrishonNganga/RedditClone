from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin

from config import config

from datetime import datetime

migrate = Migrate()
manager = LoginManager()

def create_app(config_type):    
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    
    from models import mysql

    mysql.init_app(app)
    
    migrate.init_app(app, mysql)
    manager.init_app(app)

    from blue import main
    
    app.register_blueprint(main)

    return app

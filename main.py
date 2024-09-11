from flask import Flask
from flask_security import Security
from application.models import db, User, Role
from application.sec import datastore
from config import DevelopmentConfig
from application.registeration import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)
    app.security = Security(app, datastore)
    with app.app_context():
        import application.views

    return app

app= create_app()

if __name__ == '__main__':
    app.run(debug=True)
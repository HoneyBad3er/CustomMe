import os
from flask import Flask

from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['RUN_TYPE'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from app.routes import custom_me
    app.register_blueprint(custom_me)

    return app

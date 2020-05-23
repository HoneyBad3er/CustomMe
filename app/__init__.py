
import os
from flask import Flask

from .database import db
from .login import login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['RUN_TYPE'])

    login_manager.init_app(app)
    login_manager.login_view = 'custom_me.login'

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from app.routes import custom_me
    app.register_blueprint(custom_me)

    return app

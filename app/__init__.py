import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['RUN_TYPE'])
    from app.routes import custom_me
    app.register_blueprint(custom_me)

    return app

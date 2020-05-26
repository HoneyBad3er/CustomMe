
from sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.database import db
from app.login import login_manager


class UserData(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    devices = db.relationship('DevicesData', backref='owner', lazy='dynamic')

    def __str__(self):
        return self.name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return UserData.query(int(user_id))


@event.listens_for(UserData, 'before_insert')
def event_before_insert(mapper, connection, target):
    pass


@event.listens_for(UserData, 'before_update')
def event_before_update(mapper, connection, target):
    pass


@event.listens_for(UserData, 'after_delete')
def event_after_delete(mapper, connection, target):
    pass


class DevicesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(100), nullable=False, unique=True)
    eq_set_filename = db.Column(db.String(1000))
    device_info = db.Column(db.String(100), index=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user_data.id'))

    def __str__(self):
        return self.name

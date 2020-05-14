from sqlalchemy import event

from app.database import db


class DbEntity(db.model):
    __tablename__= 'user_data'

    id = db.Column(db.Integer, primary_key=True)
    password_has = db.Column(db.String(128))
    name = db.Column(db.String(100), nullable=False, unique=True)
    devices = db.Column(db.String(1000))
    eq_sets = db.Column(db.String(1000))

    def __str__(self):
        return self.name


@event.listens_for(DbEntity, 'before_insert')
def event_before_insert(mapper, connection, target):
    pass


@event.listens_for(DbEntity, 'before_update')
def event_before_update(mapper, connection, target):
    pass


@event.listens_for(DbEntity, 'after_delete')
def event_after_delete(mapper, connection, target):
    pass
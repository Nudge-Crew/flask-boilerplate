from app import db
from .abstract_base_class import BaseModel, MetaBaseModel


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)
    email = db.Column(db.String(300), unique=True)
    access_token = db.Column(db.String(300))

    def __init__(self, first_name, last_name, email, access_token):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.access_token = access_token

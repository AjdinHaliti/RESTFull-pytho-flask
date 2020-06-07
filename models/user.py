import sqlite3
from mydb import mydb

class UserModel(mydb.Model):
    __tablename__ = 'users'

    id = mydb.Column(mydb.Integer, primary_key=True)
    username = mydb.Column(mydb.String(80))
    password = mydb.Column(mydb.String(80))
    email = mydb.Column(mydb.String(80))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save_to_db(self):
        mydb.session.add(self)
        mydb.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

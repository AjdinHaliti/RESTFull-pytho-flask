# ki objekti osht si nje storage pr tdhonat
import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        mydata = UserRegister.parser.parse_args()

        if UserModel.find_by_username(mydata['username']):
            return {"message": "User with that name already exists, pick other name."}, 400

        user = UserModel(mydata['username'], mydata['password'], mydata['email'])
        user.save_to_db()

        return {"message": "User created."}, 201


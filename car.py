import string
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('engintype',
        type=string,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('cartype',
        type=string,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required() #duhet te autentikohena pare se mos e thir metoden get
    def get(self, name):
        #do ta kthije cherin e par me emrin prkates qe do ta gjeje me funksionin next,
        #ngjajshem si me bo :
        # for car in cars:
        #     if car['name'] == name:
        #         return car
        #return {'car': next(filter(lambda x: x['name'] == name, cars), None)}
        car = self.find_by_name(name)
        if car:
            return car
        return {'message': 'Car does not exist :('}, 404


    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1], 'engintype': row[2], 'cartype': row[3]}}

    def post(self, id, name, engintype, cartype):
        # #dua qe siclli car tkijet unique name, pr kt arsyje...
        # if next(filter(lambda x: x['name'] == name, cars), None) is not None:
        #     return {'message': "An car with name '{}' already exists.".format(name)}
        #
        # data = Car.parser.parse_args()
        #
        # car = {'id': id, 'name': name, 'price': data['price'], 'engintype': data['engintype'], 'cartype': data['cartype']}
        # cars.append(car)
        # return car, 201
        if self.find_by_name(name):
            return {'message': "A car with name '{}' exists, pick other name.".format(name)}, 400

        data = Car.parser.parse_args()

        car = {'name': name, 'price': data['price'], 'engintype': data['engintype'], 'cartype': data['cartype']}

        try:
            Car.insert(car)
        except:
            return {"message": "Error happened when with inserting the car."}, 500

        return car

    @classmethod
    def insert(cls, car):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?, ?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (car['name'], car['price'], car['engintype'], car['cartype']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Car deleted'}

    @jwt_required()
    def put(self, name):
        data = Car.parser.parse_args()
        car = self.find_by_name(name)
        updated_car = {'name': name, 'price': data['price'], 'engintype': data['engintype'], 'cartype': ['cartype']}
        if car is None:
            try:
                Car.insert(updated_car)
            except:
                return {"message": " ERROR! Can't insert that car."}
        else:
            try:
                Car.update(updated_car)
            except:
                return {"message": "ERROR! Can't update that car."}
        return updated_car

    @classmethod
    def update(cls, car):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=?, engintype=?, cartype?  WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (car['price'], car['engintype'], car['cartype'], car['name']))

        connection.commit()
        connection.close()

class CarList(Resource):
    TABLE_NAME = 'cars'

    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        cars = []
        for row in result:
            cars.append({'name': row[0], 'price': row[1], 'engintype': row[2], 'cartype': row[3]})
        connection.close()

        return {'cars': cars}
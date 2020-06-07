import string
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.car import CarModel

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
    parser.add_argument('autosalon_id',
                        type=int,
                        required=True,
                        help="Every car needs a store id!!!"
                        )

    @jwt_required() #duhet te autentikohena pare se mos e thir metoden get
    def get(self, name):
        #do ta kthije cherin e par me emrin prkates qe do ta gjeje me funksionin next,
        #ngjajshem si me bo :
        # for car in cars:
        #     if car['name'] == name:
        #         return car
        #return {'car': next(filter(lambda x: x['name'] == name, cars), None)}
        car = CarModel.find_by_name(name)
        if car:
            return car.json() #it is gona return the car itself
        return {'message': 'Car does not exist :('}, 404

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
        if CarModel.find_by_name(name):
            return {'message': "A car with name '{}' exists, pick other name.".format(name)}, 400

        mydata = Car.parser.parse_args()

        car = CarModel (name, mydata['price'], mydata['engintype'], mydata['cartype'], mydata['autosalon_id'])

        try:
            car.save_to_db()
        except:
            return {"message": "Error happened when u try to save the car to database."}, 500

        return car.json()

    @jwt_required()
    def delete(self, name):
        car = CarModel.find_by_name(name)
        if car:
            car.delete_from_db()

    @jwt_required()
    def put(self, name):
        mydata = Car.parser.parse_args()

        car = CarModel.find_by_name(name)

        if car is None:
            car = CarModel(name, mydata['price'], mydata['engintype'], mydata['cartype'], mydata['autosalon_id'])
        else:
            car = (mydata['price'], mydata['engintype'], mydata['cartype'], mydata['autosalon_id'])

        car.save_to_db()

        return car.json()


class CarList(Resource):
    def get(self):
        return {'cars': [car.json() for car in CarModel.query.all()]}


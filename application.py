from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from authentication import authenticate, identity
from resources.user import UserRegister
from resources.autosallon import AutosalonList, Autosalon
from resources.car import Car, CarList
from mydb import mydb

application = Flask(__name__)
application.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
# application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # kur objekti ndryshon por nuk ruhet ndatabaz, sqlalchemy tracker esht  ma i majr se flask-sqlalchemy
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
application.secret_key = 'ajdin' #nese do ta publikojsha normal kjo d duhi tjese e mchefur dikund dhe shum ma e gjat dhe ma complicated...
api = Api(application)

#pr ti krijau tabelat automatikisht,
@application.before_first_request #kjo t ekzekurtohet para requestit tpar napi
def create_table():
    mydb.create_all()


jwt = JWT(application, authenticate, identity) #/auth

api.add_resource(Autosalon ,'/autosalon/<string:name>')
api.add_resource(Car, '/car/<string:name>')
api.add_resource(CarList, '/cars')
api.add_resource(AutosalonList ,'/autosalons')
api.add_resource(UserRegister, '/register')

#debug true is to return a good html page for errors
if __name__ == '__main__':
    mydb.init_app(application)
    application.run(host="localhost", port=8000, debug=True)

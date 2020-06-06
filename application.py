from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from authentication import authenticate, identity
from user import UserRegister
from car import Car, CarList

application = Flask(__name__)
application.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
application.secret_key = 'ajdin' #nese do ta publikojsha normal kjo d duhi tjese e mchefur dikund dhe shum ma e gjat dhe ma complicated...
api = Api(application)

jwt = JWT(application, authenticate, identity) #/auth


api.add_resource(Car, '/car/<string:name>')
api.add_resource(CarList, '/cars')
api.add_resource(UserRegister, '/register')

#debug true is to return a good html page for errors
if __name__ == '__main__':
    application.run(host="localhost", port=8000, debug=True)

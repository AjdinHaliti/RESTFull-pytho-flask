from flask_restful import Resource
from models.autosallon import AutosallonModel


class Autosalon(Resource):
    def get(self, name):
        autosalon = AutosallonModel.find_by_name(name)
        if autosalon:
            return autosalon.json()
        return {'message': 'Autosalon is not existing :O'}, 404

    def post(self, name):
        if AutosallonModel.find_by_name(name):
            return {'message': "A autosalon with name '{}' is in datbase, pick another one.".format(name)}, 400

        autosalon = AutosallonModel(name)
        try:
            autosalon.save_to_db()
        except:
            return {"message": "An error occurred saving the autosalon in db."}, 500

        return autosalon.json(), 201

    def delete(self, name):
        autosalon = AutosallonModel.find_by_name(name)
        if autosalon:
            autosalon.delete_from_db()

        return {'message': 'Autosalon deleted'}


class AutosalonList(Resource):
    def get(self):
        return {'autosalons': list(map(lambda x: x.json(), AutosallonModel.query.all()))}
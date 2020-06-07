from mydb import mydb

class AutosallonModel(mydb.Model):
    __tablename__ = 'autosalon'

    id = mydb.Column(mydb.Integer, primary_key=True)
    nameofsalon = mydb.Column(mydb.String(80))
    address = mydb.Column(mydb.String(80))
    numofemployees = mydb.Column(mydb.Float)
    #kjo na mundson ti shohm cillt car i kina n cars table many to 1, many cars with the same autosalon id
    cars = mydb.relationship('CarModel')

    def __init__(self, nameofsalon, address, numofemployees ):
        self.name = nameofsalon
        self.address = address
        self.numofemployees = numofemployees


    def json(self):
        return {'name': self.nameofsalon, 'address': self.address, 'cars': [car.json() for car in self.cars] , 'numofemployees': self.numofemployees}

    @classmethod
    def find_by_name(cls, nameofsalon):
        return cls.query.filter_by(nameofsalon=nameofsalon).first()

    def save_to_db(self):
        mydb.session.add(self)
        mydb.session.commit()

    def delete_from_db(self):
        mydb.session.delete(self)
        mydb.session.commit()
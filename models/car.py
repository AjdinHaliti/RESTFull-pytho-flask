from mydb import mydb

class CarModel(mydb.Model):
    __tablename__ = 'cars'

    id = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(80))
    price = mydb.Column(mydb.Float(precision=2))
    engintype = mydb.Column(mydb.String(80))
    cartype = mydb.Column(mydb.String(80))
    #ktu i lidhi car tabeln me autosalon table
    autosalon_id = mydb.Column(mydb.Integer, mydb.ForeignKey('autosalon.id'))
    autosalon = mydb.relationship('AutoSalon')

    def __init__(self, name, price, engintype, cartype, autosalon_id):
        self.name = name
        self.price = price
        self.engintype = engintype
        self.cartype = cartype
        self.autosalon_id = autosalon_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'engintype': self.engintype, 'cartype': self.cartype}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        mydb.session.add(self)
        mydb.session.commit()

    def delete_from_db(self):
        mydb.session.delete(self)
        mydb.session.commit()
from app import Constants
from app.models_configuration import *

class Reseller_Model(db.Model):

    __tablename__ = Constants.T_RESELLER

    id_reseller = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    create_date = db.Column(db.DATETIME, nullable=False)
    salt_password = db.Column(db.String(128), nullable=False)
    hash_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(45), nullable=False, unique=True)
    street = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(128))
    country = db.Column(db.String(255))
    zip_code = db.Column(db.String(15))
    phone = db.Column(db.String(25))
    is_active = db.Column(db.BOOLEAN, nullable=False)
    last_updated = db.Column(db.DATETIME, nullable=False)


    def init(self, email, create_date, salt_password, hash_password, first_name, last_name,
                 cpf, isactive, last_updated, street = '', city = '', state = '', country = '', zipcode = '', phone = ''):

        self.email = email
        self.create_date = create_date
        self.salt_password = salt_password
        self.hash_password = hash_password
        self.first_name = first_name
        self.last_name = last_name
        self.cpf = cpf
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode
        self.phone = phone
        self.isactive = isactive
        self.last_updated = last_updated





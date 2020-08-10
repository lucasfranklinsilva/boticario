from sqlalchemy.orm import relationship, backref

from app import constants
from app.models_configuration import *

class Cashback_Model(db.Model):

    __tablename__ = constants.T_CASH_BACK

    id_cashback = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=True)
    purchase_amount = db.Column(db.FLOAT, nullable=False)
    percentage = db.Column(db.FLOAT, nullable=False)
    is_active = db.Column(db.BOOLEAN, nullable=False)

    def __init__(self, purchase_amount, percentage):
        self.purchase_amount = purchase_amount
        self.percentage = percentage
        self.is_active = 1

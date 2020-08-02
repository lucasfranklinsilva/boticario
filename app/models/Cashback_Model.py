from app import Constants
from app.models_configuration import *


class Cashback_Model(db.Model):

    __tablename__ = Constants.T_CASH_BACK

    id_cashback = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=True)
    purchase_amount = db.Column(db.FLOAT, nullable=False)
    percentage = db.Column(db.FLOAT, nullable=False)

    def __init__(self, purchase_amount, percentage):
        self.purchase_amount = purchase_amount
        self.percentage = percentage

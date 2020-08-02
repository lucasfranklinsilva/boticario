from app.models_configuration import *


class Purchase_Model(db.Model):

    __tablename__ = 'Purchase'

    id_purchase = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=True)
    product_code = db.Column(db.String(45), nullable=False)
    product_price = db.Column(db.FLOAT, nullable=False)
    date = db.Column(db.DATETIME, nullable=False)
    reseller_id = db.Column(db.BigInteger, db.ForeignKey("Reseller.id_reseller"))
    purchase_status_id = db.Column(db.BigInteger, db.ForeignKey("Purchase_Status.id_purchase_status"))
    cash_back_id = db.Column(db.BigInteger, db.ForeignKey("Cashback.id_cashback"))


    def __init__(self, product_code, product_price, date, reseller_id, purchase_status_id, cash_back_id):
        self.product_code = product_code
        self.product_price = product_price
        self.date = date
        self.reseller_id = reseller_id
        self.purchase_status_id = purchase_status_id
        self.cash_back_id = cash_back_id

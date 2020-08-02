from app.models_configuration import *


class Purchase_Status_Model(db.Model):

    __tablename__ = 'Purchase_Status'

    id_purchase_status = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False, autoincrement=True)
    status = db.Column(db.String(45), unique=True, nullable=False)
    is_active = db.Column(db.BOOLEAN, nullable=False)

    def __init__(self, status, is_active):
        self.status = status
        self.is_active = is_active

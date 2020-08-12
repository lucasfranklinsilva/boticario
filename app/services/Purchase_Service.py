import json
import re
import logging
import sys

from flask import current_app
from flask_jsonpify import jsonify
from sqlalchemy import desc

from ..models.Purchase_Model import Purchase_Model as Purchase
from ..models.Reseller_Model import Reseller_Model as Reseller
from ..models.Cashback_Model import Cashback_Model as Cashback
from ..models.Purchase_Status_Model import Purchase_Status_Model as Purchase_Status
from ..serealizer import Purchase_Schema

from ..constants import PURCHASE_DEFAULT_STATUS_ID, PURCHASE_APROVED_STATUS_ID, PURCHASE_USER_EXCEPTION, \
    F_PURCHASE_STATUS_ID, F_RESELLER_ID, J_CPF, ACTIVE_STATUS, F_CASHBACK_PERCENT, J_PRODUCT_PRICE, SUCCESS_MESSAGE


class Purchase_Service:

    logger = logging.getLogger()

    def get_all_purchases(self):

        result = Purchase.query.all()

        result = self.aditional_data(result)

        return Purchase_Schema(many=True).jsonify(result)

    def get_purchase(self, id_purchase):

        result = Purchase.query.filter(Purchase.id_purchase == id_purchase)

        result = self.aditional_data(result)

        return Purchase_Schema(many=True).jsonify(result)

    def get_reseller_purchases(self, reseller_cpf):

        reseller_id = self.get_resseler_id(reseller_cpf)

        result = Purchase.query.filter(Purchase.reseller_id == reseller_id)

        result = self.aditional_data(result)

        return Purchase_Schema(many=True).jsonify(result)

    def new_purchase(self, json_data):

        try:

            data = json.loads(json.dumps(json_data))

            data[F_PURCHASE_STATUS_ID] = self.set_purchase_status(data[J_CPF])

            data[J_CPF] = re.sub("[^0-9]", "", data[J_CPF])

            data[F_RESELLER_ID] = self.get_resseler_id(data[J_CPF])

            data.pop(J_CPF)

            data[F_CASHBACK_PERCENT] = self.set_cash_back(data[J_PRODUCT_PRICE])

            post = Purchase(**data)

            current_app.db.session.add(post)

            current_app.db.session.commit()

            return Purchase_Schema().jsonify(post)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})

    def update_purchase(self, id_purchase, json_data):

        try:

            query = Purchase.query.filter(Purchase.id_purchase == id_purchase)

            query.update(json_data)

            current_app.db.session.commit()

            return jsonify(SUCCESS_MESSAGE)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})


    def delete_purchase(self, id_purchase):

        try:

            Purchase.query.filter(Purchase.id_purchase == id_purchase).delete()

            current_app.db.session.commit()

            return jsonify(SUCCESS_MESSAGE)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})


    def set_purchase_status(self, resseler_cpf):

        if PURCHASE_USER_EXCEPTION == resseler_cpf:
            return PURCHASE_APROVED_STATUS_ID

        return PURCHASE_DEFAULT_STATUS_ID

    def get_resseler_id(self, resseler_cpf):

        result = Reseller.query.filter(Reseller.cpf == resseler_cpf).all()

        return result[0].id_reseller

    def get_resseler_cpf(self, resseler_id):

        result = Reseller.query.filter(Reseller.id_reseller == resseler_id).all()

        if result[0]:
            return result[0].cpf

        return None

    def set_cash_back(self, purchase_amount):

        cash_back = Cashback.query.filter(Cashback.is_active == ACTIVE_STATUS). \
            order_by(desc(Cashback.purchase_amount)).all()

        for cash in cash_back:
            if purchase_amount > cash.purchase_amount:
                return cash.percentage / 100

        return 0

    def get_purchase_status(self, purchase_status_id):

        result = Purchase_Status.query.filter(Purchase_Status.id_purchase_status == purchase_status_id,
                                              Purchase_Status.is_active == ACTIVE_STATUS).all()


        if result[0]:
            return result[0].status

        return None

    def aditional_data(self, result):

        for purchase in result:
            Purchase.cash_back_amount = property(lambda self: self.product_price * purchase.cash_back)
            purchase.status = self.get_purchase_status(purchase.purchase_status_id)
            purchase.cpf = self.get_resseler_cpf(purchase.reseller_id)

        return result


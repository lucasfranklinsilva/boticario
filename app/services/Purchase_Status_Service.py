import json
import logging
import sys

from flask import current_app
from flask_jsonpify import jsonify

from ..constants import SUCCESS_MESSAGE
from ..models.Purchase_Status_Model import Purchase_Status_Model as Purchase_Status
from ..serealizer import Purchase_Status_Schema


class Purchase_Status_Service:

    logger = logging.getLogger()

    def get_all_purchase_status(self):

        result = Purchase_Status.query.all()

        return Purchase_Status_Schema(many=True).jsonify(result)

    def get_purchase_status(self, id_purchase_status):

        result = Purchase_Status.query.filter(Purchase_Status.id_purchase_status == id_purchase_status)

        return Purchase_Status_Schema(many=True).jsonify(result)

    def new_purchase_status(self, json_data):

        try:

            data = json.loads(json.dumps(json_data))

            post = Purchase_Status(**data)

            current_app.db.session.add(post)

            current_app.db.session.commit()

            return Purchase_Status_Schema().jsonify(post)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})


    def update_purchase_status(self, id_purchase_status, json_data):

        try:

            query = Purchase_Status.query.filter(Purchase_Status.id_purchase_status == id_purchase_status)

            query.update(json_data)

            current_app.db.session.commit()

            return jsonify(SUCCESS_MESSAGE)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})


    def delete_purchase_status(self, id_purchase_status):

        try:

            Purchase_Status.query.filter(Purchase_Status.id_purchase_status == id_purchase_status).delete()

            current_app.db.session.commit()

            return jsonify(SUCCESS_MESSAGE)

        except:

            self.logger.error(sys.exc_info()[0])

        return jsonify({'message': 'Something unexpected happened!'})



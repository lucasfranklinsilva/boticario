import json

from flask import current_app
from flask_jsonpify import jsonify
from ..models.Purchase_Model import Purchase_Model as Purchase
from ..serealizer import Purchase_Schema


class Purchase_Service:

    def get_all_purchases(self):

        result = Purchase.query.all()

        return Purchase_Schema(many=True).jsonify(result)

    def get_purchase(self, id_purchase):

        result = Purchase.query.filter(Purchase.id_purchase == id_purchase)

        return Purchase_Schema(many=True).jsonify(result)

    def new_purchase(self, json_data):

        data = json.loads(json.dumps(json_data))

        post = Purchase(**data)

        current_app.db.session.add(post)

        current_app.db.session.commit()

        return Purchase_Schema().jsonify(post)

    def update_purchase(self, id_purchase, json_data):

        query = Purchase.query.filter(Purchase.id_purchase == id_purchase)

        query.update(json_data)

        current_app.db.session.commit()

        return jsonify('Success')

    def delete_purchase(self, id_purchase):

        Purchase.query.filter(Purchase.id_purchase == id_purchase).delete()

        current_app.db.session.commit()

        return jsonify('Success')



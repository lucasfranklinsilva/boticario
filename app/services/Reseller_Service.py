import json

from flask import current_app
from flask_jsonpify import jsonify
from ..models.Reseller_Model import Reseller_Model as Reseller
from ..serealizer import Reseller_Schema


class Reseller_Service:

    def get_all_resellers(self):

        result = Reseller.query.all()

        return Reseller_Schema(many=True).jsonify(result)

    def get_reseller(self, id_reseller):

        result = Reseller.query.filter(Reseller.id_reseller == id_reseller)

        return Reseller_Schema(many=True).jsonify(result)

    def new_reseller(self, json_data):

        data = json.loads(json.dumps(json_data))

        post = Reseller(**data)

        current_app.db.session.add(post)

        current_app.db.session.commit()

        return Reseller_Schema().jsonify(post)

    def update_reseller(self, id_reseller, json_data):

        query = Reseller.query.filter(Reseller.id_reseller == id_reseller)

        query.update(json_data)

        current_app.db.session.commit()

        return jsonify('Success')

    def delete_reseller(self, id_reseller):

        Reseller.query.filter(Reseller.id_reseller == id_reseller).delete()

        current_app.db.session.commit()

        return jsonify('Success')

import json

from flask import current_app
from flask_jsonpify import jsonify

from .. import Constants
from ..models.Cashback_Model import Cashback_Model as Cashback
from ..serealizer import Cashback_Schema


class Cashback_Service:

    def get_all_cashbacks(self):

        result = Cashback.query.all()

        return Cashback_Schema(many=True).jsonify(result)

    def get_cashback(self, id_cashback):

        result = Cashback.query.filter(Cashback.id_cashback == id_cashback)

        print(result)

        return Cashback_Schema(many=True).jsonify(result)

    def new_cashback(self, json_data):

        data = json.loads(json.dumps(json_data))

        post = Cashback(**data)

        current_app.db.session.add(post)

        current_app.db.session.commit()

        return Cashback_Schema().jsonify(post)

    def update_cashback(self, id_cashback, json_data):

        query = Cashback.query.filter(Cashback.id_cashback == id_cashback)

        query.update(json_data)

        current_app.db.session.commit()

        return jsonify(Constants.SUCCESS_MESSAGE)


    def delete_cashback(self, id_cashback):

        Cashback.query.filter(Cashback.id_cashback == id_cashback).delete()

        current_app.db.session.commit()

        return jsonify(Constants.SUCCESS_MESSAGE)


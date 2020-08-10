import json
import re
from datetime import datetime, timedelta

import jwt
from flask import current_app
from flask_jsonpify import jsonify

from ..constants import J_CPF, SUCCESS_MESSAGE, J_PASSWORD, F_PASSWORD, F_SALT_PASSWORD, CHAR_ENCODE
from ..models.Reseller_Model import Reseller_Model as Reseller
from ..serealizer import Reseller_Schema
import bcrypt


class Reseller_Service:

    def get_all_resellers(self):

        result = Reseller.query.all()

        return Reseller_Schema(many=True).jsonify(result)


    def get_reseller_by_id(self, id_reseller):

        result = Reseller.query.filter(Reseller.id_reseller == id_reseller)

        return Reseller_Schema(many=True).jsonify(result)

    def get_reseller(self, cpf):
        result = Reseller.query.filter(Reseller.cpf == cpf)

        return Reseller_Schema(many=True).jsonify(result)

    def new_reseller(self, json_data):

        data = json.loads(json.dumps(json_data))

        salt = bcrypt.gensalt()

        data[J_CPF] = re.sub("[^0-9]", "", data[J_CPF])

        data[F_PASSWORD] = bcrypt.hashpw(data[J_PASSWORD].encode(), salt).decode(CHAR_ENCODE)

        data[F_SALT_PASSWORD] = salt.decode(CHAR_ENCODE)

        data.pop(J_PASSWORD)

        post = Reseller(**data)

        current_app.db.session.add(post)

        current_app.db.session.commit()

        return Reseller_Schema().jsonify(post)

    def update_reseller(self, id_reseller, json_data):

        query = Reseller.query.filter(Reseller.id_reseller == id_reseller)

        query.update(json_data)

        current_app.db.session.commit()

        return jsonify(SUCCESS_MESSAGE)

    def delete_reseller(self, id_reseller):

        Reseller.query.filter(Reseller.id_reseller == id_reseller).delete()

        current_app.db.session.commit()

        return jsonify( SUCCESS_MESSAGE)
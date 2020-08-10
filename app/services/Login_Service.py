import json
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request
from flask_jsonpify import jsonify

from ..constants import JWT_EXP_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM, CHAR_ENCODE, J_USER_EMAIL, J_PASSWORD, \
    PAYLOAD_USER, PAYLOAD_PASSWORD, PAYLOAD_EXPIRATION
from ..models.Reseller_Model import Reseller_Model as Reseller
import bcrypt


class Login_Service:

    def authenticate(self, json_data):

        data = json.loads(json.dumps(json_data))

        if data[J_USER_EMAIL] and data[J_PASSWORD]:

            result = Reseller.query.filter(Reseller.email == data[J_USER_EMAIL]).all()

            if result[0]:

                hashed_password = bcrypt.hashpw(data[J_PASSWORD].encode(), result[0].salt_password.encode())

                if result[0].hash_password.encode() == hashed_password:

                    token = self.get_token(data[J_USER_EMAIL], result[0].hash_password)

                    return jsonify({'token': token})

                else:

                    return jsonify({'message': 'Credentials doesn\'t match!'})

        return jsonify({'message': 'Invalid Parameters'})

    def get_token(self, user_email, user_password):

        payload = {
            PAYLOAD_USER: user_email,
            PAYLOAD_PASSWORD: user_password,
            PAYLOAD_EXPIRATION: datetime.utcnow() + timedelta(minutes=JWT_EXP_MINUTES)
        }

        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)

        return token.decode(CHAR_ENCODE)

    @staticmethod
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):

            token = request.headers.get('Authorization')

            if not token:

                return jsonify({'message': 'Token is missing!'})

            try:
                payload = jwt.decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)

                valid_user = Login_Service.login(Login_Service, payload[PAYLOAD_USER], payload[PAYLOAD_PASSWORD])

                if not valid_user:

                    return jsonify({'message': 'Invalid Credentials!'})

            except jwt.ExpiredSignatureError:

                return jsonify({'message': 'Signature expired. Please log in again!'})

            except jwt.InvalidTokenError:

                return jsonify({'message': 'Invalid token. Please log in again!'})

            return f(*args, **kwargs)

        return decorated

    @staticmethod
    def login(self, user_email, user_password):

        result = Reseller.query.filter(Reseller.email == user_email,
                                       Reseller.hash_password == user_password).all()

        if len(result) > 0:
            return True

        return False


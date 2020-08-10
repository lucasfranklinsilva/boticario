from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify

from ..constants import HTTP_SUCCESS, HTTP_BAD_REQUEST
from ..services.Login_Service import Login_Service

login_bp = Blueprint('login', __name__)

login_service = Login_Service()


@login_bp.route('/authentication', methods=['POST'])
def authentication():

    try:

        return login_service.authenticate(request.json), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

def error_hanlder(e):

    error = str(e.__cause__)

    return jsonify(error), HTTP_BAD_REQUEST

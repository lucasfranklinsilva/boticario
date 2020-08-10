from flask import Blueprint, current_app, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify
import logging

from ..constants import HTTP_CREATED, HTTP_SUCCESS, HTTP_BAD_REQUEST
from ..services.Purchase_Service import Purchase_Service
from ..services.Login_Service import Login_Service as Auth

logger = logging.getLogger()
purchase_bp = Blueprint('purchase', __name__)
purchase_service = Purchase_Service()


@purchase_bp.route('/purchase/new', methods=['POST'])
def create():

    try:

        return purchase_service.new_purchase(request.json), HTTP_CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)

@purchase_bp.route('/purchase', methods=['GET'])
def get_all():

    return purchase_service.get_all_purchases(), HTTP_SUCCESS



@purchase_bp.route('/purchase/<id_purchase>', methods=['GET'])
def get(id_purchase):

    try:

        return purchase_service.get_purchase(id_purchase), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_bp.route('/purchase/update/<id_purchase>', methods=['PUT'])
def update(id_purchase):

    try:

        return purchase_service.update_purchase(id_purchase, request.json), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_bp.route('/purchase/delete/<id_purchase>', methods=['DELETE'])
def delete(id_purchase):

    try:

        return purchase_service.delete_purchase(id_purchase), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


def error_hanlder(e):

    error = str(e.__cause__)

    logger.error(error)

    return jsonify(error), HTTP_BAD_REQUEST
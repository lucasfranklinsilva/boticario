from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify
import logging

from ..constants import HTTP_CREATED, HTTP_SUCCESS, HTTP_BAD_REQUEST
from ..services.Purchase_Status_Service import Purchase_Status_Service

logger = logging.getLogger()
purchase_status_bp = Blueprint('purchase_status', __name__)
purchase_status_service = Purchase_Status_Service()


@purchase_status_bp.route('/purchase_status/new', methods=['POST'])
def create():

    try:

        return purchase_status_service.new_purchase_status(request.json), HTTP_CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_status_bp.route('/purchase_status', methods=['GET'])
def get_all():

    try:

        return purchase_status_service.get_all_purchase_status(), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_status_bp.route('/purchase_status/<id_purchase_status>', methods=['GET'])
def get(id_purchase_status):

    try:

        return purchase_status_service.get_purchase_status(id_purchase_status), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_status_bp.route('/purchase_status/update/<id_purchase_status>', methods=['PUT'])
def update(id_purchase_status):

    try:

        return purchase_status_service.update_purchase_status(id_purchase_status, request.json), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@purchase_status_bp.route('/purchase_status/delete/<id_purchase_status>', methods=['DELETE'])
def delete(id_purchase_status):

    try:

        return purchase_status_service.delete_purchase_status(id_purchase_status), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


def error_hanlder(e):

    error = str(e.__cause__)

    logger.error(error)

    return jsonify(error), HTTP_BAD_REQUEST
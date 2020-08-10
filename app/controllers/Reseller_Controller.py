from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify
import logging

from ..constants import HTTP_CREATED, HTTP_SUCCESS, HTTP_BAD_REQUEST
from ..services.Login_Service import Login_Service as Auth
from ..services.Reseller_Service import Reseller_Service

logger = logging.getLogger()
reseller_bp = Blueprint('reseller', __name__)
reseller_service = Reseller_Service()

@reseller_bp.route('/reseller/new', methods=['POST'])
def create():

    try:

        return reseller_service.new_reseller(request.json), HTTP_CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)

@reseller_bp.route('/reseller', methods=['GET'])
def get_all():

    try:

        return reseller_service.get_all_resellers(), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@reseller_bp.route('/reseller/<reseller_cpf>', methods=['GET'])
def get(reseller_cpf):

    try:

        return reseller_service.get_reseller(reseller_cpf), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@reseller_bp.route('/reseller/update/<reseller_id>', methods=['PUT'])
def update(reseller_id):

    try:

        return reseller_service.update_reseller(reseller_id, request.json), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@reseller_bp.route('/reseller/delete/<reseller_id>', methods=['DELETE'])
def delete(reseller_id):

    try:

        return reseller_service.delete_reseller(reseller_id), HTTP_SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


def error_hanlder(e):

    error = str(e.__cause__)

    logger.error(error)

    return jsonify(error), HTTP_BAD_REQUEST

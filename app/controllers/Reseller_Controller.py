from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify

from .. import Constants
from ..services.Reseller_Service import Reseller_Service

reseller_bp = Blueprint('reseller', __name__)

real_estate_service = Reseller_Service()


@reseller_bp.route('/reseller/new', methods=['POST'])
def create():

    try:

        return real_estate_service.new_reseller(request.json), Constants.CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)


@reseller_bp.route('/reseller', methods=['GET'])
def get_all():

    try:

        return real_estate_service.get_all_resellers(), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@reseller_bp.route('/reseller/<reseller_id>', methods=['GET'])
def get(reseller_id):

    try:

        return real_estate_service.get_reseller(reseller_id), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@reseller_bp.route('/reseller/update/<reseller_id>', methods=['PUT'])
def update(reseller_id):

    try:

        return real_estate_service.update_reseller(reseller_id, request.json), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@reseller_bp.route('/reseller/delete/<reseller_id>', methods=['DELETE'])
def delete(reseller_id):

    try:

        return real_estate_service.delete_reseller(reseller_id), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


def error_hanlder(e):

    error = str(e.__cause__)

    return jsonify(error), Constants.BAD_REQUEST

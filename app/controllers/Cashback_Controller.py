from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify

from .. import Constants
from ..services.Cashback_Service import Cashback_Service


cashback_bp = Blueprint('cashback', __name__)

cash_back_service = Cashback_Service()


@cashback_bp.route('/cashback/new', methods=['POST'])
def create():

    try:

        return cash_back_service.new_cashback(request.json), Constants.CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)

@cashback_bp.route('/cashback', methods=['GET'])
def get_all():

    try:

        return cash_back_service.get_all_cashbacks(), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@cashback_bp.route('/cashback/<id_cashback>', methods=['GET'])
def get(id_cashback):

    try:

        return cash_back_service.get_cashback(id_cashback), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@cashback_bp.route('/cashback/update/<id_cashback>', methods=['PUT'])
def update(id_cashback):

    try:

        return cash_back_service.update_cashback(id_cashback, request.json), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


@cashback_bp.route('/cashback/delete/<id_cashback>', methods=['DELETE'])
def delete(id_cashback):

    try:

        return cash_back_service.delete_cashback(id_cashback), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)


def error_hanlder(e):

    error = str(e.__cause__)

    return jsonify(error), Constants.BAD_REQUEST
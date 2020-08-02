from flask import Blueprint, current_app, request
from sqlalchemy.exc import SQLAlchemyError
from flask_jsonpify import jsonify

from .. import Constants
from ..services.Purchase_Service import Purchase_Service

purchase_bp = Blueprint('purchase', __name__)

purchase_service = Purchase_Service()


@purchase_bp.route('/purchase/new', methods=['POST'])
def create():

    try:

        return purchase_service.new_purchase(request.json), Constants.CREATED

    except SQLAlchemyError as e:

        return error_hanlder(e)

@purchase_bp.route('/purchase', methods=['GET'])
def get_all():

    try:

        return purchase_service.get_all_purchases(), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@purchase_bp.route('/purchase/<id_purchase>', methods=['GET'])
def get(id_purchase):

    try:

        return purchase_service.get_purchase(id_purchase), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@purchase_bp.route('/purchase/update/<id_purchase>', methods=['PUT'])
def update(id_purchase):

    try:

        return purchase_service.update_purchase(id_purchase, request.json), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

@purchase_bp.route('/purchase/delete/<id_purchase>', methods=['DELETE'])
def delete(id_purchase):

    try:

        return purchase_service.delete_purchase(id_purchase), Constants.SUCCESS

    except SQLAlchemyError as e:

        return error_hanlder(e)

def error_hanlder(e):

    error = str(e.__cause__)

    return jsonify(error), Constants.BAD_REQUEST
from flask import Blueprint, current_app, request
from ..services.Purchase_Service import Purchase_Service

purchase_bp = Blueprint('purchase', __name__)

purchase_service = Purchase_Service()


@purchase_bp.route('/purchase/new', methods=['POST'])
def create():

    return purchase_service.new_purchase(request.json), 201


@purchase_bp.route('/purchase', methods=['GET'])
def get_all():

    return purchase_service.get_all_purchases(), 200


@purchase_bp.route('/purchase/<id_purchase>', methods=['GET'])
def get(id_purchase):

    return purchase_service.get_purchase(id_purchase), 200


@purchase_bp.route('/purchase/update/<id_purchase>', methods=['PUT'])
def update(id_purchase):

    return purchase_service.update_purchase(id_purchase, request.json), 200


@purchase_bp.route('/purchase/delete/<id_purchase>', methods=['DELETE'])
def delete(id_purchase):

    return purchase_service.delete_purchase(id_purchase), 200



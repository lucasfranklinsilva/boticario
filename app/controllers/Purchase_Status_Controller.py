from flask import Blueprint, request
from ..services.Purchase_Status_Service import Purchase_Status_Service

purchase_status_bp = Blueprint('purchase_status', __name__)

purchase_status_service = Purchase_Status_Service()


@purchase_status_bp.route('/purchase_status/new', methods=['POST'])
def create():

    return purchase_status_service.new_purchase_status(request.json), 201


@purchase_status_bp.route('/purchase_status', methods=['GET'])
def get_all():

    return purchase_status_service.get_all_purchase_status(), 200


@purchase_status_bp.route('/purchase_status/<id_purchase_status>', methods=['GET'])
def get(id_purchase_status):

    return purchase_status_service.get_purchase_status(id_purchase_status), 200


@purchase_status_bp.route('/purchase_status/update/<id_purchase_status>', methods=['PUT'])
def update(id_purchase_status):

    return purchase_status_service.update_purchase_status(id_purchase_status, request.json), 200


@purchase_status_bp.route('/purchase_status/delete/<id_purchase_status>', methods=['DELETE'])
def delete(id_purchase_status):

    return purchase_status_service.delete_purchase_status(id_purchase_status), 200


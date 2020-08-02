from flask import Blueprint, request
from ..services.Reseller_Service import Reseller_Service

reseller_bp = Blueprint('reseller', __name__)

real_estate_service = Reseller_Service()


@reseller_bp.route('/reseller/new', methods=['POST'])
def create():

    return real_estate_service.new_reseller(request.json), 201


@reseller_bp.route('/reseller', methods=['GET'])
def get_all():

    return real_estate_service.get_all_resellers(), 200


@reseller_bp.route('/reseller/<reseller_id>', methods=['GET'])
def get(reseller_id):

    return real_estate_service.get_reseller(reseller_id), 200


@reseller_bp.route('/reseller/update/<reseller_id>', methods=['PUT'])
def update(reseller_id):

    return real_estate_service.update_reseller(reseller_id, request.json), 200


@reseller_bp.route('/reseller/delete/<reseller_id>', methods=['DELETE'])
def delete(reseller_id):

    return real_estate_service.delete_reseller(reseller_id), 200

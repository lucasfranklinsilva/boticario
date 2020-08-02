from flask import Blueprint, request
from ..services.Cashback_Service import RealEstateTypeService

cashback_bp = Blueprint('cashback', __name__)

real_estate_type_service = RealEstateTypeService()


@cashback_bp.route('/cashback/new', methods=['POST'])
def create():

    return real_estate_type_service.new_cashback(request.json), 201


@cashback_bp.route('/cashback', methods=['GET'])
def get_all():

    return real_estate_type_service.get_all_cashbacks(), 200


@cashback_bp.route('/cashback/<id_cashback>', methods=['GET'])
def get(id_cashback):

    return real_estate_type_service.get_cashback(id_cashback), 200


@cashback_bp.route('/cashback/update/<id_cashback>', methods=['PUT'])
def update(id_cashback):

    return real_estate_type_service.update_cashback(id_cashback, request.json), 200


@cashback_bp.route('/cashback/delete/<id_cashback>', methods=['DELETE'])
def delete(id_cashback):

    return real_estate_type_service.delete_cashback(id_cashback), 200


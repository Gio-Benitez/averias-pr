from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

municipality_handler = Blueprint('municipality_handler', __name__)


@municipality_handler.route('/<int:mun_id>', methods=['GET'])
def get_municipality_by_id(mun_id):
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_municipality_dao()

    try:
        municipality = municipality_dao.get_municipality_by_id(mun_id)
        response = {
            'MunicipalityID': municipality[0],
            'MunicipalityName': municipality[1],
            'Population': municipality[2],
            'SizeArea': municipality[3]
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@municipality_handler.route('/all', methods=['GET'])
def get_all_municipalities():
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_municipality_dao()

    try:
        municipalities = municipality_dao.get_all_municipalities()
        response = []
        for municipality in municipalities:
            response.append({
                'MunicipalityID': municipality[0],
                'MunicipalityName': municipality[1],
                'Population': municipality[2],
                'SizeArea': municipality[3]
            })
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@municipality_handler.route('/name/<string:mun_name>', methods=['GET'])
def get_municipality_by_name(mun_name):
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_municipality_dao()

    try:
        # error handling with capitalize and strip
        municipality = municipality_dao.get_municipality_by_name(mun_name.capitalize().strip())

        response = {
            'MunicipalityID': municipality[0],
            'MunicipalityName': municipality[1],
            'Population': municipality[2],
            'SizeArea': municipality[3]
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


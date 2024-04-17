from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

municipality_handler = Blueprint('municipality_handler', __name__)


@municipality_handler.route('/g', methods=['POST'])
def get_municipalityby_id():
    data = request.get_json()
    mun_id = data.get('mun_id')
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

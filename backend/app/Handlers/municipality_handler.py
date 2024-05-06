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

@municipality_handler.route('/updateAggregates', methods=['PUT'])
def updateAggregates():
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_municipality_dao()
    data = request.get_json()
    mun_id = data['mun_id']
    num_reports = data['num_reports']
    most_common_category = data['most_common_category']
    resolved_reports = data['resolved_reports']
    try:
        municipality_dao.updateAggregates(mun_id, num_reports, most_common_category, resolved_reports)
        response = {
            'message': 'Aggregates updated successfully'
        }
        municipality_dao.close()
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        municipality_dao.close()
        return jsonify(error=error_message), 500

# Load Map Data 
@municipality_handler.route('/map', methods=['GET'])
def load_map():
    # Load necessary DAOs
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_municipality_dao()
    report_data_dao = dao_factory.get_report_data_dao()
    result = municipality_dao.getAggregates()
    pr_stats = municipality_dao.getAggregateNational()
    pr_cat = report_data_dao.getCommonCategoryNational()
    # Close DAO connection
    municipality_dao.close()
    report_data_dao.close()
    # Map output data
    output = {}
    for row in result:
        output[str(row[0])] = {
            'population': row[1],
            'num_reports': row[2],
            'most_common_category': row[3],
            'resolved_reports': row[4]
        }
    output['Puerto Rico'] = {
        'population': pr_stats[0],
        'num_reports': pr_stats[1],
        'most_common_category': pr_cat[0],
        'resolved_reports': pr_stats[2]
    }
    
    return jsonify(output), 200
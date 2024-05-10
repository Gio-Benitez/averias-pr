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
    # Get general aggregates
    result = municipality_dao.getAggregates()
    
    # Get aggregates by category
    cats = municipality_dao.getCategoryAggregates()
    cats_national = municipality_dao.getCategoryAggregatesNational()
    
    cat_dict = {}
    # Map municipal categories to dictionary
    for row in cats:
        if row[0] not in cat_dict:
            cat_dict[row[0]] = {}
        cat_dict[row[0]][row[1]] = {}
        cat_dict[row[0]][row[1]]['total'] = row[2]
        if row[3] is None:
            cat_dict[row[0]][row[1]]['resolved'] = 0
        else:
            cat_dict[row[0]][row[1]]['resolved'] = row[3]
            
    # Map national categories to dictionary
    for row in cats_national:
        if 'Puerto Rico' not in cat_dict:
            cat_dict['Puerto Rico'] = {}
        cat_dict['Puerto Rico'][row[0]] = {}
        cat_dict['Puerto Rico'][row[0]]['total'] = row[1]
        if row[2] is None:
            cat_dict['Puerto Rico'][row[0]]['resolved'] = 0
        else:
            cat_dict['Puerto Rico'][row[0]]['resolved'] = row[2]
    print(cat_dict)
    
    # Default Aggregates for Empty Categories
    default_cats = {
        'Carretera Dañada': 0,
        'Poste Caido': 0,
        'Deslizamiento': 0,
        'Peligro de Deslizamiento': 0,
        'Servicio de Agua': 0,
        'Servicio de Luz': 0
    }

    # Close DAO connection
    municipality_dao.close()
    report_data_dao.close()

    # Map output data to dictionary
    output = {}
    for row in result:
        output[str(row[0])] = {
            'population': row[1],
            'num_reports': row[2],
            'most_common_category': row[3],
            'resolved_reports': row[4],
            'categories': default_cats if str(row[0]) not in cat_dict else {
                'Carretera Dañada': cat_dict[str(row[0])].get('Carretera Dañada') if 'Carretera Dañada' in cat_dict[str(row[0])] else 0,
                'Poste Caido': cat_dict[str(row[0])].get('Poste Caido') if 'Poste Caido' in cat_dict[str(row[0])] else 0,
                'Deslizamiento': cat_dict[str(row[0])].get('Deslizamiento') if 'Deslizamiento' in cat_dict[str(row[0])] else 0,
                'Peligro de Deslizamiento': cat_dict[str(row[0])].get('Peligro de Deslizamiento') if 'Peligro de Deslizamiento' in cat_dict[str(row[0])] else 0,
                'Servicio de Agua': cat_dict[str(row[0])].get('Servicio de Agua') if 'Servicio de Agua' in cat_dict[str(row[0])] else 0,
                'Servicio de Luz': cat_dict[str(row[0])].get('Servicio de energía eléctrica') if 'Servicio de energía eléctrica' in cat_dict[str(row[0])] else 0
                }
        }

    #print(output)
    return jsonify(output), 200
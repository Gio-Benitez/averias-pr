from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection
from datetime import datetime

report_data_handler = Blueprint('report_data_handler', __name__)


@report_data_handler.route('/', methods=['POST'])
def create_report_data():
    data = request.get_json()
    user_id = data.get('userID') # Get current user here
    municipality = data.get('municipality') # Get mun id from municipality name
    category = data.get('category') # Get category id from category name
    location = data.get('location')
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d')
    status = "No"
    [geo_data_lat,geo_data_long] = location.get('coordinates')
    img_src = data.get('image')
    
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()
    municipality_dao = dao_factory.get_municipality_dao()
    category_dao = dao_factory.get_category_dao()

    try:
        # Fetch municipality and category id using names
        mun_id = municipality_dao.get_municipality_id_by_name(municipality)
        category_id = category_dao.get_category_id_by_name(category)

        report = report_data_dao.create_report_data(user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src, formatted_date, status)
        report_count = report_data_dao.get_report_count_by_user_id(user_id) # Update Report count in front end
        reports = report_data_dao.get_users_reports(user_id)
        response = {
            'message': 'Report Data Created',
            'report_data_id': report[0],
            'report_count': report_count[1],
            'user_reports': reports
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500

@report_data_handler.route('/reportcount', methods=['POST'])
def get_report_count_by_id():
    data = request.get_json()
    user_id = data.get('userID') # Get current user here
    municipality = data.get('municipality') # Get mun id from municipality name
    category = data.get('category') # Get category id from category name
    location = data.get('location')
    [geo_data_lat,geo_data_long] = location.get('coordinates')
    img_src = data.get('image')
    
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()
    municipality_dao = dao_factory.get_municipality_dao()
    category_dao = dao_factory.get_category_dao()

    try:
        # Fetch municipality and category id using names
        mun_id = municipality_dao.get_municipality_id_by_name(municipality)
        category_id = category_dao.get_category_id_by_name(category)

        report = report_data_dao.create_report_data(user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src)
        # test_response = {
        #     'message': 'Report Data Received',
        #     'userid': user_id,
        #     'municipality': mun_id,
        #     'category': category_id,
        #     'geo_data_lat': geo_data_lat,
        #     'geo_data_long': geo_data_long,
        #     'img_src': img_src
        # }

        response = {
            'message': 'Report Data Created',
            'report_data_id': report[0]
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@report_data_handler.route('/all', methods=['GET'])
def get_all_report_data():
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        report_data = report_data_dao.get_all_report_data()
        response = []
        for data in report_data:
            response.append({
                'data_id': data[0],
                'user_id': data[1],
                'mun_id': data[2],
                'category_id': data[3],
                'address_line_1': data[4],
                'address_line_2': data[5],
                'report_category': data[6],
                'city_name': data[7],
                'zipcode': data[8],
                'geo_data_lat': data[9],
                'geo_data_long': data[10],
                'img_src': data[11]
            })
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500



@report_data_handler.route('/get/<int:data_id>', methods=['GET'])
def get_report_data(data_id):
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        report_data = report_data_dao.get_report_data_by_id(data_id)
        response = {
            'data_id': report_data[0],
            'user_id': report_data[1],
            'mun_id': report_data[2],
            'category_id': report_data[3],
            'address_line_1': report_data[4],
            'address_line_2': report_data[5],
            'report_category': report_data[6],
            'city_name': report_data[7],
            'zipcode': report_data[8],
            'geo_data_lat': report_data[9],
            'geo_data_long': report_data[10],
            'img_src': report_data[11]
        }
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@report_data_handler.route('/update_report_data/<int:data_id>', methods=['PUT'])
def update_status(data_id):
    data = request.get_json()
    report_status = data.get('report_status')

    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        report_data_dao.update_report_data(data_id, report_status)
        response = {
            'message': 'Report Data Updated'
        }
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message),


# get all reports from a given target municipality
@report_data_handler.route('/get_reports_by_mun/<int:mun_id>', methods=['GET'])
def get_reports_by_mun(mun_id):
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        report_data = report_data_dao.get_reports_by_mun(mun_id)
        response = []
        for data in report_data:
            response.append({
                'data_id': data[0],
                'user_id': data[1],
                'mun_id': data[2],
                'category_id': data[3],
                'address_line_1': data[4],
                'address_line_2': data[5],
                'report_category': data[6],
                'city_name': data[7],
                'zipcode': data[8],
                'geo_data_lat': data[9],
                'geo_data_long': data[10],
                'img_src': data[11]
            })
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500

# get all reports from a given target category
@report_data_handler.route('/get_reports_by_cat/<int:category_id>', methods=['GET'])
def get_reports_by_cat(category_id):
    dao_factory = DAOFactory(get_connection())
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        report_data = report_data_dao.get_reports_by_cat(category_id)
        response = []
        for data in report_data:
            response.append({
                'data_id': data[0],
                'user_id': data[1],
                'mun_id': data[2],
                'category_id': data[3],
                'address_line_1': data[4],
                'address_line_2': data[5],
                'report_category': data[6],
                'city_name': data[7],
                'zipcode': data[8],
                'geo_data_lat': data[9],
                'geo_data_long': data[10],
                'img_src': data[11]
            })
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message),


# get population, count of all reports, most common report category and count reports resolved for all municipalities in the database

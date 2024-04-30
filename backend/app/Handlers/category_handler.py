from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

category_handler = Blueprint('category_handler', __name__)


@category_handler.route('/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_category_dao()

    try:
        category = municipality_dao.get_category_by_id(category_id)
        response = {
            'CategoryID': category[0],
            'CategoryName': category[1]
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@category_handler.route('/all', methods=['GET'])
def get_all_categories():
    dao_factory = DAOFactory(get_connection())
    municipality_dao = dao_factory.get_category_dao()

    try:
        categories = municipality_dao.get_all_categories()
        response = []
        for category in categories:
            response.append({
                'CategoryID': category[0],
                'CategoryName': category[1]
            })
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500

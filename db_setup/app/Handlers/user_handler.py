from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

user_handler = Blueprint('user_handler', __name__)


@user_handler.route('/', methods=['POST'])
def create_users():
    data = request.get_json()
    user_email = data.get('Email')
    user_pass_hash = data.get('PasswordHash')
    user_salt = data.get('Salt')
    user_fname = data.get('FirstName')
    user_lname = data.get('LastName')
    admin_id = data.get('AdminID', False)  # Default to False if AdminID is not provided

    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        # TODO may help to create a validator function to check if the email is valid
        if user_dao.get_user_by_email(user_email) is not None:
            return jsonify(error='Email already in use'), 400
        user_id = user_dao.create_user(user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id)
        response = {
            'message': 'User created successfully',
            'UserID': user_id
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


# @user_handler.route('/', methods=['GET'])
# def get_users():
#     dao_factory = DAOFactory(get_connection())
#     user_dao = dao_factory.get_user_dao()
#
#     try:
#         users = user_dao.get_users()
#         response = []
#         for user in users:
#             response.append({
#                 'UserID': user[0],
#                 'Email': user[1],
#                 'FirstName': user[2],
#                 'LastName': user[3],
#                 'AdminID': user[4]
#             })
#         return jsonify(response), 200
#
#     except Exception as e:
#         error_message = str(e)
#         return jsonify(error=error_message), 500


@user_handler.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        user = user_dao.get_user(user_id)
        response = {
            'UserID': user[0],
            'Email': user[1],
            'FirstName': user[2],
            'LastName': user[3],
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user_email = data.get('Email')
    user_pass_hash = data.get('PasswordHash')
    user_salt = data.get('Salt')
    user_fname = data.get('FirstName')
    user_lname = data.get('LastName')
    admin_id = data.get('AdminID', False)

    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    #
    try:
        if user_dao.get_user_by_email(user_email) is not None:
            return jsonify(error='Email already in use'), 400
        user_dao.update_user(user_id, user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id)
        response = {
            'message': 'User updated successfully'
        }
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        deleted_user = user_dao.delete_user(user_id)
        response = {

            'message': 'User deleted successfully'
        }
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/all', methods=['GET'])
def get_all_users():
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        users = user_dao.get_users()
        response = []
        for user in users:
            response.append({
                'UserID': user[0],
                'Email': user[1],
                'FirstName': user[2],
                'LastName': user[3],
                'AdminID': user[4]
            })
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/<int:user_id>/', methods=['GET'])
def get_user_by_id(user_id):
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        user = user_dao.get_user(user_id)
        response = {
            'UserID': user[0],
            'Email': user[1],
            'FirstName': user[2],
            'LastName': user[3]
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        print(e)
        return jsonify(error=error_message), 500


@user_handler.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_email = data.get('Email')
    user_pass_hash = data.get('PasswordHash')

    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        user = user_dao.get_user_by_email(user_email)
        if user is None:
            return jsonify(error='User not found'), 404
        if user[2] != str(user_pass_hash):
            return jsonify(error=f"Incorrect password"), 401
        response = {
            'UserID': user[0],
            # 'Email': user[1],
            # 'FirstName': user[3],
            # 'LastName': user[4],
            # 'AdminID': user[5]
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/<int:user_id>/reports', methods=['GET'])
def get_user_reports(user_id):
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        reports = user_dao.get_user_reports(user_id)
        response = []
        for report in reports:
            response.append({
                'ReportID': report[0],
                'ReportDate': report[1],
                'ReportEmail': report[2],
                'ReportStatus': report[3]
            })
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500

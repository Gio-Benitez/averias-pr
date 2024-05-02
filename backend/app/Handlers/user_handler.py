from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

user_handler = Blueprint('user_handler', __name__)


@user_handler.route('/', methods=['POST'])
def create_users():
    data = request.get_json()
    user_email = data.get('Email')
    user_pass = data.get('Password')
    user_pass_conf = data.get('PasswordConf')
    user_fname = data.get('FirstName')
    user_lname = data.get('LastName')
    admin_id = data.get('AdminID', False)  # Default to False if AdminID is not provided
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        # TODO may help to create a validator function to check if the email is valid
        if user_dao.get_user_by_email(user_email) is not None:
            return jsonify(error='Email already in use'), 400
        if user_pass_conf != user_pass: 
            return jsonify(error='Passwords do not match'), 400
        user_id = user_dao.create_user(user_email, user_pass, user_fname, user_lname, admin_id)
        response = {
            'message': 'User created successfully',
            'UserID': user_id,
            'access': 'true'
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500


@user_handler.route('/get/<int:user_id>', methods=['GET'])
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



@user_handler.route('/get_all_users', methods=['GET'])
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

                'Password': user[2],
                'FirstName': user[3],
                'LastName': user[4],
                'AdminID': user[5]
            })
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


@user_handler.route('/get_user/<int:user_id>/', methods=['GET'])
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
    user_pass = data.get('Password')    

    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()
    report_data_dao = dao_factory.get_report_data_dao()

    try:
        user = user_dao.get_user_by_email(user_email)
        if user is None:
            return jsonify(error='User not found'), 404
        if str(user[2]) != str(user_pass):
            return jsonify(error=f"Incorrect password"), 401
        report_count = report_data_dao.get_report_count_by_user_id(user[0]) # Update Report count in front end
        reports = report_data_dao.get_users_reports(user[0])
        if reports is None:
            reports = []
            
        response = {
            'UserID': user[0],
            'report_count': report_count[1],
            'user_reports': reports
        }
        return jsonify(response), 200

    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500



# @user_handler.route('/update_user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.get_json()
#     user_email = data.get('Email')
#     user_pass = data.get('Password')
#     user_fname = data.get('FirstName')
#     user_lname = data.get('LastName')
#     admin_id = data.get('AdminID', False)

#     dao_factory = DAOFactory(get_connection())
#     user_dao = dao_factory.get_user_dao()

#     try:
#         if user_dao.get_user_by_email(user_email) is not None:
#             return jsonify(error='Email already in use'), 400
#         user_dao.update_user(user_id, user_email, user_pass, user_fname, user_lname, admin_id)
#         response = {
#             'message': 'User updated successfully'
#         }
#         return jsonify(response), 200
#     except Exception as e:
#         error_message = str(e)
#         return jsonify(error=error_message), 500


# user route to update password
@user_handler.route('/update_password', methods=['POST'])
def update_password():
    data = request.get_json()
    user_email = data.get('Email')
    new_pass = data.get('Password')
    new_pass_conf = data.get('PasswordConf')

    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        if new_pass_conf != new_pass: 
            return jsonify(error='Passwords do not match'), 400
        user_id = user_dao.get_user_id_by_email(user_email)
        user_dao.update_user_password(user_id, new_pass)
        response = {
            'message': 'Password updated successfully',
            'UserID': user_id
        }
        return jsonify(response), 200
    except Exception as e:
        error_message = str(e)
        return jsonify(error=error_message), 500

# Get user by email to validate if email is already in use
@user_handler.route('/verify_user_email/', methods=['POST'])
def verify_user_email():
    if request.get_json() is None:
        return jsonify(error='No data provided'), 400
    
    data = request.get_json()
    dao_factory = DAOFactory(get_connection())
    user_dao = dao_factory.get_user_dao()

    try:
        user = user_dao.get_user_by_email(data.email)
        if user is None:
            return jsonify(error='User not found'), 404
        else:
            return jsonify(user), 200

    except Exception as e:
        error_message = str(e)
        print(e)
        return jsonify(error=error_message), 500
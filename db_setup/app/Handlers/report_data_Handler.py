from flask import Blueprint, request, jsonify
from DAO.dao_factory import DAOFactory
from config.dbconfig import get_connection

report_data_handler = Blueprint('report_data_handler', __name__)


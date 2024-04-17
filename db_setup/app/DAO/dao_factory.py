# add imported dao methods
from .userDAO import UserDAO
from .report_dataDAO import report_dataDAO
from .municipalityDOA import municipalityDAO

class DAOFactory:
    def __init__(self, conn):
        self.conn = conn

    def get_user_dao(self):
        return UserDAO(self.conn)

    def get_report_data_dao(self):
        return report_dataDAO(self.conn)

from DAO.dao import BaseDAO


class municipalityDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)


# CREATE TABLE if not exists report (
#     report_id SERIAL PRIMARY KEY,
#     data_id INT REFERENCES report_data(data_id),
#     report_date DATE NOT NULL,
#     report_email VARCHAR(255) NOT NULL,
#     report_status VARCHAR(20) NOT NULL,
#     CONSTRAINT fk_report_data FOREIGN KEY (report_id) REFERENCES report_data(data_id) ON DELETE CASCADE
# );


def get_all_municipalities(self):
    query = """SELECT * FROM municipality;"""
    cur = self.execute_query(query)
    return cur.fetchall()


def get_municipality_by_id(self, mun_id):
    query = """SELECT * FROM municipality WHERE mun_id = %s;"""
    cur = self.execute_query(query, (mun_id,))
    return cur.fetchone()


def get_municipality_by_name(self, mun_name):
    query = """SELECT * FROM municipality WHERE mun_name = %s;"""
    cur = self.execute_query(query, (mun_name,))
    return cur.fetchone()


def get_municipality_population(self, mun_ids):
    query = """SELECT mun_population FROM municipality WHERE mun_id = %s;"""
    cur = self.execute_query(query, (mun_ids,))
    return cur.fetchall()

def get_municipality_area(self, mun_ids):
    query = """SELECT mun_area FROM municipality WHERE mun_id = %s;"""
    cur = self.execute_query(query, (mun_ids,))
    return cur.fetchall()

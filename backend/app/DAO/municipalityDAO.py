from DAO.dao import BaseDAO


class municipalityDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def get_municipality_by_id(self, mun_id):
        query = """SELECT mun_id, mun_name, mun_population, mun_size_area FROM municipality WHERE mun_id = %s;"""
        cur = self.execute_query(query, (mun_id,))
        return cur.fetchone()

    def get_municipality_name_by_id(self, mun_id):
        query = """SELECT mun_name FROM municipality WHERE mun_id = %s;"""
        cur = self.execute_query(query, (mun_id,))
        return cur.fetchone()

    def get_all_municipalities(self):
        query = """SELECT mun_id, mun_name, mun_population, mun_size_area FROM municipality;"""
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_municipality_population(self, mun_ids):
        query = """SELECT mun_population FROM municipality WHERE mun_id = %s;"""
        cur = self.execute_query(query, (mun_ids,))
        return cur.fetchall()

    def get_municipality_area(self, mun_ids):
        query = """SELECT mun_area FROM municipality WHERE mun_id = %s;"""
        cur = self.execute_query(query, (mun_ids,))
        return cur.fetchall()

    def get_municipality_by_name(self, mun_name):
        query = """SELECT * FROM municipality WHERE mun_name = %s;"""
        cur = self.execute_query(query, (mun_name,))
        return cur.fetchone()

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
    
    def get_municipality_id_by_name(self, mun_name):
        query = """SELECT mun_id FROM municipality WHERE mun_name = %s;"""
        cur = self.execute_query(query, (mun_name,))
        return cur.fetchone()

    def updateAggregates(self, mun_id, num_reports, most_common_category, resolved_reports):
        params = (num_reports, most_common_category, resolved_reports, mun_id)
        query = """UPDATE municipality SET "num_reports" = %s, "most_common_category" = %s, "resolved_reports" = %s
                WHERE "mun_id" = %s;"""
        self.execute_query(query, params)
        self.commit()
    
    def getAggregates(self):
        query = """SELECT mun_name, mun_population, num_reports, most_common_category, resolved_reports FROM municipality;"""
        cur = self.execute_query(query)
        return cur.fetchall()
    
    def getAggregateNational(self):
        query = """SELECT  SUM(mun_population), SUM(num_reports), SUM(resolved_reports)  FROM municipality;"""
        cur = self.execute_query(query)
        return cur.fetchone()
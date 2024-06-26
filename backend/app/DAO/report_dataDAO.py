from DAO.dao import BaseDAO


class report_dataDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_report_data(self, user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src, report_date, report_status):
        query = """INSERT INTO report_data (user_id, mun_id, category_id, geo_data_lat, geo_data_long, image_src, report_date, report_status) 
        VALUES (%s, %s, %s, %s, %s, %s, %s::DATE, %s) returning data_id;"""
        params = (user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src, report_date, report_status)
        cur = self.execute_query(query, params)
        self.commit()
        return cur.fetchone()
    
    def get_users_reports(self, user_id):
        query = """SELECT rd.data_id, rd.user_id, m.mun_name, c.category_name, rd.geo_data_lat, rd.geo_data_long, rd.image_src, rd.report_status 
                FROM report_data rd
                JOIN municipality m ON rd.mun_id = m.mun_id
                JOIN category c ON rd.category_id = c.category_id
                WHERE rd.user_id = %s;"""
        cur = self.execute_query(query, (user_id,))
        return cur.fetchall()
    
    def get_all_report_data(self):
        query = """SELECT data_id, user_id, mun_id, category_id, address_line_1, address_line_2, 
                   report_category, city_name, zipcode, geo_data_lat, geo_data_long, image_src 
                   FROM report_data;"""
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_report_data_by_id(self, data_id):
        query = """SELECT data_id, user_id, mun_id, category_id, geo_data_lat, geo_data_long, image_src 
                   FROM report_data WHERE data_id = %s;"""
        cur = self.execute_query(query, (data_id, ))
        return cur.fetchone()

    def delete_report_data_by_id(self, data_id):
        query = """DELETE FROM report_data WHERE data_id = %s;"""
        self.execute_query(query, (data_id,))
        self.commit()

    def update_report_data(self, data_id, user_id, municipality_id, address_line_1, address_line_2, city, zipcode,
                           geo_data_lat,
                           geo_data_long, img_src):
        query = """UPDATE report_data SET user_id = %s, municipality_id = %s, address_line_1 = %s, address_line_2 = %s, 
        city = %s, zipcode = %s, geo_data_lat = %s, geo_data_long = %s, img_src = %s WHERE data_id = %s;"""

        params = (user_id, municipality_id, address_line_1, address_line_2, city, zipcode, geo_data_lat, geo_data_long,
                  img_src, data_id)
        self.execute_query(query, params)
        self.commit()

    def get_report_count_by_user_id(self, user_id):
        query = """SELECT user_id, COUNT(data_id) AS report_count 
                FROM report_data 
                WHERE user_id = %s 
                GROUP BY user_id;"""
        cur = self.execute_query(query, (user_id,))
        result = cur.fetchone()
        # Check if result is None
        if result is None:
            return (user_id, 0)  # Return user_id and count 0
        
        return result
    # Compute Aggregates
    # Total Reports for Municipio
    def getTotalReportsMuni(self, mun_id):
        query = """SELECT COUNT(data_id) FROM report_data WHERE mun_id = %s;"""
        cur = self.execute_query(query, (mun_id,))
        return cur.fetchone()
    
    # Most Common Report Category by Muni
    def getCommonCategory(self, mun_id):
        query = """SELECT category_name FROM report_data natural inner join category WHERE mun_id = %s GROUP BY category_name ORDER BY COUNT(category_id) DESC LIMIT 1;"""
        cur = self.execute_query(query, (mun_id,))
        return cur.fetchone()
    
    # Resolved Reports
    def getResolvedReportsMuni(self, mun_id):
        query = """SELECT COUNT(data_id) FROM report_data WHERE mun_id = %s AND report_status = 'Resolved';"""
        cur = self.execute_query(query, (mun_id,))
        return cur.fetchone()
    
    # Most Common Report Category National
    def getCommonCategoryNational(self):
        query = """SELECT category_name FROM report_data natural inner join category GROUP BY category_name ORDER BY COUNT(category_id) DESC LIMIT 1;"""
        cur = self.execute_query(query)
        return cur.fetchone()
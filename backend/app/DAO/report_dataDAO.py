from DAO.dao import BaseDAO


class report_dataDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_report_data(self, user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src):
        query = """INSERT INTO report_data (user_id, mun_id, category_id, geo_data_lat, geo_data_long, image_src) 
        VALUES (%s, %s, %s, %s, %s, %s) returning data_id;"""
        params = (user_id, mun_id, category_id, geo_data_lat, geo_data_long, img_src)
        cur = self.execute_query(query, params)
        self.commit()
        return cur.fetchone()

    def get_all_report_data(self):
        query = """SELECT data_id, user_id, mun_id, category_id, address_line_1, address_line_2, 
                   report_category, city_name, zipcode, geo_data_lat, geo_data_long, image_src 
                   FROM report_data;"""
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_report_data_by_id(self, data_id):
        query = """SELECT data_id, user_id, mun_id, category_id, address_line_1, address_line_2, 
                   report_category, city_name, zipcode, geo_data_lat, geo_data_long, image_src 
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
        return cur.fetchone()

from DAO.dao import BaseDAO


class report_dataDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_report_data(self, user_id, mun_id, category_id, address_line_1, address_line_2, report_category,
                           city_name, zipcode, geo_data_lat, geo_data_long, img_src):
        query = """INSERT INTO report_data (user_id, mun_id, category_id, address_line_1, address_line_2, 
        report_category, city_name, zipcode, geo_data_lat, geo_data_long, image_src) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning data_id;"""
        params = (user_id, mun_id, category_id, address_line_1, address_line_2, report_category,
                  city_name, zipcode, geo_data_lat, geo_data_long, img_src)
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
        cur = self.execute_query(query, (data_id,))
        return cur.fetchone()

    def delete_report_data_by_id(self, data_id):
        query = """DELETE FROM report_data WHERE data_id = %s;"""
        self.execute_query(query, (data_id,))
        self.commit()

    def update_report_data(self, data_id, user_id, municipality_id, address_line_1, address_line_2, city, zipcode,
                           geo_data_lat,
                           geo_data_long, img_src):
        query = """UPDATE report_data SET user_id = %s, mun_id = %s, address_line_1 = %s, address_line_2 = %s, 
        -- something is wrong here
        City_name = %s, zipcode = %s, geo_data_lat = %s, geo_data_long = %s, image_src = %s WHERE data_id = %s;"""

        params = (user_id, municipality_id, address_line_1, address_line_2, city, zipcode, geo_data_lat, geo_data_long,
                  img_src, data_id)
        self.execute_query(query, params)
        self.commit()

    # # get population, count of all reports, most common report category and count reports resolved for all
    # municipalities in the database
    def load_map_by_mun_id(self, mun_id):
        query = """SELECT mun_population, count(data_id) as report_count,
        (SELECT report_category, count(*) FROM report_data WHERE mun_id = %s GROUP BY report_category ORDER BY report_category
         DESC) as most_common_report_category, 
        count(data_id) as resolved_report_count FROM municipality LEFT JOIN report_data USING (mun_id) WHERE mun_id = %s GROUP BY mun_id;"""
        cur = self.execute_query(query, (mun_id, mun_id))
        return cur.fetchone()

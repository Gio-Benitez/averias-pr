from DAO.dao import BaseDAO


class CategoryDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def get_all_categories(self):
        query = """SELECT * FROM category;"""
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_category_by_id(self, category_id):
        query = """SELECT * FROM category WHERE category_id = %s;"""
        cur = self.execute_query(query, (category_id,))
        return cur.fetchone()

    def get_category_by_name(self, category_name):
        query = """SELECT * FROM category WHERE category_name = %s;"""
        cur = self.execute_query(query, (category_name,))
        return cur.fetchone()

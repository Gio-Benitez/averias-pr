import psycopg2 as ps
from DAO.dao import BaseDAO


class UserDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)

    def create_user(self, user_email, user_pass_hash, user_salt, user_fname=None, user_lname=None, admin_id=False):

        query = """INSERT INTO "user" (user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id)
                VALUES (%s, %s, %s, %s, %s, %s) returning user_id;
                """
        params = (user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id)
        cur = self.execute_query(query, params)
        self.commit()
        return cur.fetchone()
        # try:
        #     # Execute the query
        #     cur = self.execute_query(query, params)
        # # Error checking
        # except ps.errors.UniqueViolation as uv:
        #     return f'Email already in use, try to login.'
        #
        # self.commit()
        # return cur.fetchone()

    def get_users(self):
        query = """SELECT * FROM "user";"""
        cur = self.execute_query(query)
        self.commit()
        return cur.fetchall()

    # user_id SERIAL PRIMARY KEY,
    #     user_email VARCHAR(255) UNIQUE NOT NULL,
    #     user_pass_hash VARCHAR(255) NOT NULL,
    #     user_salt VARCHAR(255) NOT NULL,
    #     user_fname VARCHAR(100),
    #     user_lname VARCHAR(100),
    #     admin_id bool
    def get_user(self, user_id):
        query = """SELECT user_id, user_email, user_fname, user_lname FROM "user" WHERE "user_id" = %s;"""
        cur = self.execute_query(query, (user_id,))
        return cur.fetchone()

    def delete_user(self, user_id):
        query = """DELETE FROM "user" WHERE "user_id" = %s;"""
        self.execute_query(query, (user_id,))
        self.commit()

    def update_user(self, user_id, user_email, user_pass_hash, user_salt, user_fname=None, user_lname=None,
                    admin_id=False):
        query = """UPDATE "user" SET "user_email" = %s, "user_pass_hash" = %s, "user_salt" = %s, "user_fname" = %s, "user_lname" = 
        %s, "admin_id" = %s WHERE "user_id" = %s;"""
        params = (user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id, user_id)
        self.execute_query(query, params)
        self.commit()

    def get_user_by_email(self, user_email):
        query = """SELECT user_id, user_email, user_pass_hash FROM "user" WHERE "user_email" = %s;"""
        cur = self.execute_query(query, (user_email,))
        self.commit()
        return cur.fetchone()

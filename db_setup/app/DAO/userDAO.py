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

    def get_users(self):
        query = """SELECT * FROM "Users";"""
        cur = self.execute_query(query)
        return cur.fetchall()

    def get_user_by_id(self, user_id):
        query = """SELECT * FROM "Users" WHERE "UserID" = %s;"""
        cur = self.execute_query(query, (user_id,))
        return cur.fetchone()

    def delete_user_by_id(self, user_id):
        query = """DELETE FROM "Users" WHERE "UserID" = %s;"""
        self.execute_query(query, (user_id,))
        self.commit()

    def update_user(self, user_id, user_email, user_pass_hash, user_salt, user_fname=None, user_lname=None, admin_id=False):
        query = """UPDATE "Users" SET "Email" = %s, "PasswordHash" = %s, "Salt" = %s, "FirstName" = %s, "LastName" = 
        %s, "AdminID" = %s WHERE "UserID" = %s;"""
        params = (user_email, user_pass_hash, user_salt, user_fname, user_lname, admin_id, user_id)
        self.execute_query(query, params)
        self.commit()

    def get_user_by_email(self, user_email):
        query = """SELECT * FROM "Users" WHERE "Email" = %s;"""
        cur = self.execute_query(query, (user_email,))
        return cur.fetchone()





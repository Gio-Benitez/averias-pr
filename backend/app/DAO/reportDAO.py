from DAO.dao import BaseDAO


class reportDAO(BaseDAO):
    def __init__(self, conn):
        super().__init__(conn)


    def create_report(self, data_id, report_date, report_email, report_status):
        query = """INSERT INTO report (data_id, report_date, report_email, report_status) VALUES (%s, %s, %s, %s)"""
        params = (data_id, report_date, report_email, report_status)
        cur = self.execute_query(query, params)
        self.commit()
        return cur.fetchone()


    def get_all_reports(self):
        query = """SELECT data_id, report_date, report_email, report_status FROM report;"""
        cur = self.execute_query(query)
        return cur.fetchall()






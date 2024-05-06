class BaseDAO:
    def __init__(self, conn):
        self.conn = conn

    def execute_query(self, query, params=None):
        cur = self.conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        self.conn.commit()
        return cur

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()
    
    def close(self):
        self.conn.close()
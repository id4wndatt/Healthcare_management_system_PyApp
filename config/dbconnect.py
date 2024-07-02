import mysql.connector


class dbconfig:
    def __init__(self):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.dbname = 'hcms'
        self.con = None
        self.cur = None

    def connectdb(self):
        self.con = mysql.connector.connect(host=self.host, port=self.port, user=self.user, database=self.dbname)
        self.cur = self.con.cursor()

    def close_connect(self):
        if self.con:
            self.con.close()

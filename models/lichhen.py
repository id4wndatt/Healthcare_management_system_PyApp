from config import dbconnect


class Lichhen:
    def __init__(self, ngayhen, giohen, trangthai, khachhang):
        self.ngayhen = ngayhen
        self.giohen = giohen
        self.trangthai = trangthai
        self.khachhang = khachhang

    @staticmethod
    def get_all_app(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT * FROM hcms_lichhen")
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    def create_app(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_lichhen (lh_ngayhen, lh_giohen, lh_trangthai, lh_khachhang_id) VALUES (%s, "
                         "%s, %s, %s)", (self.ngayhen, self.giohen, self.trangthai, self.khachhang))
        conn.con.commit()
        conn.close_connect()

    def update_app(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("UPDATE hcms_lichhen SET lh_ngayhen = %s, lh_giohen = %s, lh_trangthai = %s, lh_khachhang_id "
                         "= %s WHERE id = %s", (self.ngayhen, self.giohen, self.trangthai, self.khachhang, id))
        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def delete_app(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_lichhen WHERE id = %s", (id,))
        conn.con.commit()
        conn.close_connect()

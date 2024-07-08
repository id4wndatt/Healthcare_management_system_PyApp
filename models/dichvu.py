from config import dbconnect


class Dichvu:
    def __init__(self, ten, dongia, mota, trangthai, danhmuc):
        self.ten = ten
        self.dongia = dongia
        self.mota = mota
        self.trangthai = trangthai
        self.danhmuc = danhmuc

    @staticmethod
    def get_dv_name(dv_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT dv_ten FROM hcms_dichvu WHERE id = %s", (dv_id,))
        rs = conn.cur.fetchone()
        conn.close_connect()
        return rs[0] if rs else None

    @staticmethod
    def get_all_services():
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT * FROM hcms_dichvu")
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    @staticmethod
    def get_dm_name(dm_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT dm_dv_ten FROM hcms_danhmuc_dichvu WHERE id = %s", (dm_id,))
        rs = conn.cur.fetchone()
        conn.close_connect()
        return rs[0] if rs else None

    def create_service(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_dichvu (dv_ten, dv_dongia, dv_mota, dv_trangthai, dv_danhmuc_id) VALUES (%s,"
                         "%s, %s, %s, %s)", (self.ten, self.dongia, self.mota, self.trangthai, self.danhmuc))
        conn.con.commit()
        conn.close_connect()

    def update_service(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("UPDATE hcms_dichvu SET dv_ten = %s, dv_dongia = %s, dv_mota = %s, dv_trangthai = %s, "
                         "dv_danhmuc_id = %s WHERE id = %s",
                         (self.ten, self.dongia, self.mota, self.trangthai, self.danhmuc, id))
        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def delete_service(id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_dichvu WHERE id = %s", (id,))
        conn.con.commit()
        conn.close_connect()

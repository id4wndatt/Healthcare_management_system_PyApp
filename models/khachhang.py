from user import User
from config import dbconnect


class Khachhang(User):
    def __init__(self, hoten, gioitinh, sdt, ngaysinh, diachi, trangthai):
        super().__init__(hoten, gioitinh, sdt, ngaysinh, diachi, trangthai)

    @staticmethod
    def get_all_user(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        query = "SELECT * FROM hcms_khachhang"
        conn.cur.execute(query)
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    def create_user(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_khachhang(kh_hoten, kh_gioitinh, kh_sdt, kh_ngaysinh, kh_diachi, "
                         "kh_trangthai) VALUES(%s, %s, %s, %s, %s)", (self.hoten, self.gioitinh, self.sdt,
                                                                      self.ngaysinh, self.diachi, self.trangthai))
        conn.con.commit()
        conn.close_connect()

    def update_user(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("UPDATE hcms_khachhang SET kh_hoten = %s, kh_gioitinh = %s, kh_sdt = %s, kh_ngaysinh = %s, "
                         "kh_diachi = %s, kh_trangthai = %s WHERE id = %s", (self.hoten, self.gioitinh, self.sdt,
                                                                             self.ngaysinh, self.diachi,
                                                                             self.trangthai, id))
        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def delete_user(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_khachhang WHERE id = %s", (id,))
        conn.con.commit()
        conn.close_connect()

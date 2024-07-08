
from config import dbconnect
from models.user import User


class Khachhang(User):
    def __init__(self, hoten, gioitinh, sdt, ngaysinh, diachi, trangthai, matkhau=None):
        super().__init__(hoten, gioitinh, sdt, ngaysinh, diachi, trangthai, matkhau)
        self.hoten = hoten
        self.gioitinh = gioitinh
        self.sdt = sdt
        self.ngaysinh = ngaysinh
        self.diachi = diachi
        self.trangthai = trangthai
        self.matkhau = matkhau

    @staticmethod
    def get_all_user():
        conn = dbconnect.dbconfig()
        conn.connectdb()

        query = "SELECT * FROM hcms_khachhang"
        conn.cur.execute(query)
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs
    @staticmethod
    def get_kh_name(kh_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT kh_hoten FROM hcms_khachhang WHERE id = %s", (kh_id,))
        rs = conn.cur.fetchone()
        conn.close_connect()
        return rs[0] if rs else None

    def create_user(self):
        conn = dbconnect.dbconfig()
        try:
            conn.connectdb()
            query = ("INSERT INTO hcms_khachhang(kh_hoten, kh_gioitinh, kh_sdt, kh_ngaysinh, kh_diachi, kh_trangthai) "
                     "VALUES(%s, %s, %s, %s, %s, %s)")
            conn.cur.execute(query, (self.hoten, self.gioitinh, self.sdt, self.ngaysinh, self.diachi, self.trangthai))
            conn.con.commit()
        except Exception as e:
            print(f"Error creating user: {e}")
        finally:
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
    def delete_user(id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_khachhang WHERE id = %s", (id,))
        conn.con.commit()
        conn.close_connect()

from config import dbconnect
from models.user import User


class Nhanvien(User):
    def __init__(self, hoten, gioitinh, sdt, ngaysinh, diachi, chucvu, trangthai, matkhau, quyen):
        super().__init__(hoten, gioitinh, sdt, ngaysinh, diachi, trangthai, matkhau)
        self.chucvu = chucvu
        self.quyen = quyen

    @staticmethod
    def get_all_emp():
        conn = dbconnect.dbconfig()
        conn.connectdb()

        query = "SELECT * FROM hcms_nhanvien"
        conn.cur.execute(query)
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    @staticmethod
    def get_nv_name(nv_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT nv_hoten FROM hcms_nhanvien WHERE id = %s", (nv_id,))
        rs = conn.cur.fetchone()
        conn.close_connect()
        return rs[0] if rs else None

    def create_emp(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_nhanvien (nv_hoten, nv_gioitinh, nv_sdt, nv_ngaysinh, nv_diachi, "
                         "nv_chucvu, nv_trangthai, nv_matkhau, nv_quyen) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         (self.hoten, self.gioitinh, self.sdt, self.ngaysinh, self.diachi, self.chucvu,
                          self.trangthai, self.matkhau, self.quyen))
        conn.con.commit()
        conn.close_connect()

    def update_user(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()
        conn.cur.execute("UPDATE hcms_nhanvien SET nv_hoten = %s, nv_gioitinh = %s, nv_sdt = %s, nv_ngaysinh = %s, "
                         "nv_diachi = %s, nv_chucvu = %s, nv_trangthai = %s, nv_matkhau = %s,  nv_quyen = %s WHERE id "
                         "= %s",
                         (self.hoten, self.gioitinh, self.sdt, self.ngaysinh, self.diachi, self.chucvu,
                          self.trangthai, self.matkhau, self.quyen, id))
        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def delete_user(id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_nhanvien WHERE id = %s", (id,))
        conn.con.commit()
        conn.close_connect()

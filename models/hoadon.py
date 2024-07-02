from config import dbconnect


class Hoadon:
    def __init__(self, tongtien, ngaygiotao, trangthai, mota, khachhang, nhanvien, soluong, dichvu, hoadon):
        self.tongtien = tongtien
        self.ngaygiotao = ngaygiotao
        self.trangthai = trangthai
        self.mota = mota
        self.khachhang = khachhang
        self.nhanvien = nhanvien
        self.soluong = soluong
        self.dichvu = dichvu
        self.hoadon = hoadon

    @staticmethod
    def get_all_bill(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT * FROM hcms_hoadon")
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    @staticmethod
    def get_all_bill_detail(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT * FROM hcms_hoadon_chitiet")
        oc = conn.cur.fetchall()
        conn.close_connect()
        return oc

    def create_bill(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_hoadon (hd_tongtien, hd_ngaygiotao, hd_trangthai, hd_mota, "
                         "hd_khachhang_id, hd_nhanvien_id) VALUES (%s, %s, %s, %s, %s, %s)", (self.tongtien,
                                                                                              self.ngaygiotao,
                                                                                              self.trangthai,
                                                                                              self.mota,
                                                                                              self.khachhang,
                                                                                              self.nhanvien))

        conn.cur.execute("INSERT INTO hcms_hoadon_chititet (hdct_soluong, hdct_dichvu_id, hdct_hoadon_id) VALUES (%s, "
                         "%s, %s)", (self.soluong, self.dichvu, self.hoadon))

        conn.con.commit()
        conn.close_connect()

    def update_bill(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("UPDATE hcms_hoadon SET hd_tongtien= %s, hd_ngaygiotao = %s, hd_trangthai = %s, hd_mota = "
                         "%s, hd_khachhang_id = %s, hd_nhanvien_id = %s WHERE id = %s", (self.tongtien,
                                                                                         self.ngaygiotao,
                                                                                         self.trangthai, self.mota,
                                                                                         self.khachhang,
                                                                                         self.nhanvien, id))

        conn.cur.execute("UPDATE hcms_hoadon_chitiet SET hdct_soluong = %s, hdct_dichvu_id = %s, hdct_hoadon = %s "
                         "WHERE id = %s", (self.soluong, self.dichvu, self.hoadon, id))
        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def delete_bill(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_hoadon WHERE id = %s", (id,))

        conn.cur.execute("DELETE FROM hcms_hoadon_chitiet WHERE id = %s", (id,))

        conn.con.commit()
        conn.close_connect()

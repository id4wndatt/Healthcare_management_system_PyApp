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
    def get_all_bill():
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT h.id, h.hd_khachhang_id, h.hd_tongtien, h.hd_ngaygiotao, h.hd_trangthai, h.hd_mota, "
                         "h.hd_nhanvien_id, hdc.id, hdc.hdct_soluong, hdc.hdct_dichvu_id, hdc.hdct_hoadon_id FROM "
                         "hcms_hoadon h LEFT JOIN hcms_hoadon_chitiet hdc ON h.id = hdc.hdct_hoadon_id")
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

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

        conn.con.commit()
        hd_id = conn.cur.lastrowid
        conn.close_connect()
        return hd_id

    def create_bill_detail(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("INSERT INTO hcms_hoadon_chitiet (hdct_soluong, hdct_dichvu_id, hdct_hoadon_id) VALUES (%s, "
                         "%s, %s)", (self.soluong, self.dichvu, self.hoadon))

        conn.con.commit()
        conn.close_connect()

    def update_bill(self, id, new_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute(
            "UPDATE hcms_hoadon SET id= %s, hd_tongtien= %s, hd_ngaygiotao = %s, hd_trangthai = %s, hd_mota = "
            "%s, hd_khachhang_id = %s, hd_nhanvien_id = %s WHERE id = %s", (new_id, self.tongtien,
                                                                            self.ngaygiotao,
                                                                            self.trangthai, self.mota,
                                                                            self.khachhang,
                                                                            self.nhanvien, id))

        conn.cur.execute("UPDATE hcms_hoadon_chitiet SET hdct_hoadon_id = %s WHERE hdct_hoadon_id = %s", (new_id, id))

        conn.con.commit()
        conn.close_connect()

    def update_hdct(self, id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("UPDATE hcms_hoadon_chitiet SET hdct_soluong = %s, hdct_dichvu_id = %s WHERE id = %s",
                         (self.soluong, self.dichvu, id))

        conn.con.commit()
        conn.close_connect()

    @staticmethod
    def exists(id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT * FROM hcms_hoadon WHERE id = %s", (id,))
        rs = conn.cur.fetchone()
        conn.close_connect()
        return rs is not None

    @staticmethod
    def get_latest_bill():
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT hcms_hoadon.id, hcms_hoadon.hd_khachhang_id, hcms_hoadon.hd_tongtien, "
                         "hcms_hoadon.hd_ngaygiotao, hcms_hoadon.hd_trangthai, hcms_hoadon.hd_mota, "
                         "hcms_hoadon.hd_nhanvien_id, hcms_hoadon_chitiet.id, hcms_hoadon_chitiet.hdct_soluong, "
                         "hcms_hoadon_chitiet.hdct_dichvu_id, hcms_hoadon_chitiet.hdct_hoadon_id FROM hcms_hoadon "
                         "LEFT JOIN hcms_hoadon_chitiet ON hcms_hoadon.id = hcms_hoadon_chitiet.hdct_hoadon_id ORDER "
                         "BY hcms_hoadon.id DESC LIMIT 1;")
        rs = conn.cur.fetchall()
        conn.close_connect()
        return rs

    @staticmethod
    def delete_bill(id):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("DELETE FROM hcms_hoadon_chitiet WHERE hdct_hoadon_id = %s", (id,))

        conn.cur.execute("DELETE FROM hcms_hoadon WHERE id = %s", (id,))

        conn.con.commit()
        conn.close_connect()

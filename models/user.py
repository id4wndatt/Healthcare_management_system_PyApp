from config import dbconnect


class User:
    def __init__(self, hoten, gioitinh, sdt, ngaysinh, diachi, trangthai, matkhau):
        self.hoten = hoten
        self.gioitinh = gioitinh
        self.sdt = sdt
        self.ngaysinh = ngaysinh
        self.diachi = diachi
        self.trangthai = trangthai
        self.matkhau = matkhau

    def log_user(self):
        db = dbconnect.dbconfig()
        db.connectdb()
        cur = db.cur

        cur.execute("SELECT * FROM hcms_nhanvien WHERE nv_sdt=%s AND nv_matkhau=%s", (self.sdt, self.matkhau))
        acc = cur.fetchone()

        if acc:
            if acc[9] == 1:  # Admin = 1
                db.close_connect()
                return 'admin'
            elif acc[9] == 0:  # Employee = 0
                db.close_connect()
                return 'employee'
            else:
                db.close_connect()
                return False
        else:
            db.close_connect()
            return False

    def update_nv_acc(self):
        db = dbconnect.dbconfig()
        db.connectdb()
        cur = db.cur
        cur.execute("UPDATE hcms_nhanvien SET nv_sdt = %s, nv_matkhau = %s WHERE nv_sdt = %s",
                    (self.sdt, self.matkhau, self.sdt))
        db.con.commit()
        db.close_connect()

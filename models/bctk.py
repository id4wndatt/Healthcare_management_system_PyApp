from config import dbconnect


class BaoCaoThongKe:
    def __init__(self, nam=2024):
        self.nam = nam

    def bao_cao_doanh_thu_nam(self):
        doanh_thu_nam = []
        for thang in range(1, 13):
            conn = dbconnect.dbconfig()
            conn.connectdb()

            conn.cur.execute(
                "SELECT SUM(hd.hd_tongtien) AS doanh_thu FROM hcms_hoadon hd WHERE MONTH(hd.hd_ngaygiotao) = "
                "%s AND YEAR(hd.hd_ngaygiotao) = %s", (thang, self.nam))

            rs = conn.cur.fetchone()
            conn.close_connect()
            doanh_thu_nam.append(rs[0] if rs else 0)

        return doanh_thu_nam

    def bao_cao_so_luong_lich_hen_quy(self):
        so_luong_lich_hen_quy = []
        for quy in range(1, 4):
            conn = dbconnect.dbconfig()
            conn.connectdb()

            conn.cur.execute(
                "SELECT COUNT(lh.id) AS so_luong_lich_hen FROM hcms_lichhen lh WHERE QUARTER(lh.lh_ngayhen) "
                "= %s AND YEAR(lh.lh_ngayhen) = %s;",
                (quy, self.nam))

            rs = conn.cur.fetchone()
            conn.close_connect()
            so_luong_lich_hen_quy.append(rs[0] if rs else 0)

        return so_luong_lich_hen_quy

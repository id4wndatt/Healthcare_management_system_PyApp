from datetime import datetime

from PyQt6.QtCore import QDate, QDateTime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

from config import dbconnect
from models.bctk import BaoCaoThongKe
from models.dichvu import Dichvu
from models.hoadon import Hoadon
from models.khachhang import Khachhang
from models.lichhen import Lichhen
from models.nhanvien import Nhanvien
from models.session import Session
from views.admin import Ui_admin_window
from log_handle import Login_MainWindow


class Admin_MainWindow(QMainWindow):
    def __init__(self):
        super(Admin_MainWindow, self).__init__()

        self.nam = 2024
        self.login_window = None
        self.ui = Ui_admin_window()
        self.ui.setupUi(self)

        current_user = Session.get_current_user()
        if current_user:
            print(f"Nhân viên có SĐT: {current_user.sdt}")
            self.ui.txt_sdt_tk.setText(current_user.sdt)

        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.btn_kh.clicked.connect(self.page_kh_toggle)
        self.ui.btn_nv.clicked.connect(self.page_nv_toggle)
        self.ui.btn_dv.clicked.connect(self.page_dv_toggle)
        self.ui.btn_lh.clicked.connect(self.page_lh_toggle)
        self.ui.btn_hd.clicked.connect(self.page_hd_toggle)
        self.ui.btn_bctk.clicked.connect(self.page_bctk_toggle)
        self.ui.btn_tk.clicked.connect(self.page_tk_toggle)

        self.load_kh_data()
        self.load_dv_data()
        self.load_dm_data()
        self.load_nv_data()

        self.show_kh_data()
        self.show_nv_data()
        self.show_dv_data()
        self.show_lh_data()
        self.show_hd_data()

        self.ui.tbl_kh.itemClicked.connect(self.call_kh_data)
        self.ui.tbl_nv.itemClicked.connect(self.call_nv_data)
        self.ui.tbl_dv.itemClicked.connect(self.call_dv_data)
        self.ui.tbl_lh.itemClicked.connect(self.call_lh_data)
        self.ui.tbl_hd.itemClicked.connect(self.call_hd_data)

        self.ui.btn_them_kh.clicked.connect(self.add_kh_ad)
        self.ui.btn_sua_kh.clicked.connect(self.update_kh_ad)
        self.ui.btn_xoa_kh.clicked.connect(self.del_kh_ad)
        self.ui.btn_them_nv.clicked.connect(self.add_nv_ad)
        self.ui.btn_sua_nv.clicked.connect(self.update_nv_ad)
        self.ui.btn_xoa_nv.clicked.connect(self.del_nv_ad)
        self.ui.btn_them_dv.clicked.connect(self.add_dv_ad)
        self.ui.btn_sua_dv.clicked.connect(self.update_dv_ad)
        self.ui.btn_xoa_dv.clicked.connect(self.del_dv_ad)
        self.ui.btn_sua_lh.clicked.connect(self.update_lh_ad)
        self.ui.btn_xoa_lh.clicked.connect(self.del_lh_ad)
        self.ui.btn_sua_hd.clicked.connect(self.update_hd_ad)
        self.ui.btn_xoa_hd.clicked.connect(self.del_hd_ad)
        self.ui.btn_xacnhan.clicked.connect(self.update_tk)

        self.ui.btn_bc.clicked.connect(self.show_bao_cao_doanh_thu)
        self.ui.btn_tke.clicked.connect(self.show_bao_cao_so_luong_lich_hen_quy)
        self.ui.btn_xuatpdf.clicked.connect(self.export_to_pdf)

        self.ui.btn_exit.clicked.connect(self.logout)

    def page_kh_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def page_nv_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def page_dv_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def page_lh_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def page_hd_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def page_bctk_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def page_tk_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    @staticmethod
    def get_kh_name(kh_id):
        conn = dbconnect.dbconfig()
        conn.connectdb()
        conn.cur.execute("SELECT kh_hoten FROM hcms_khachhang WHERE id = %s", (str(kh_id),))
        result = conn.cur.fetchone()
        conn.close_connect()
        return result[0] if result else ""

    def load_kh_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, kh_hoten FROM hcms_khachhang")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_kh_lh.clear()
        for kh in data:
            self.ui.cbb_kh_lh.addItem(kh[1], kh[0])

        self.ui.cbb_kh_hd.clear()
        for kh in data:
            self.ui.cbb_kh_hd.addItem(kh[1], kh[0])

        self.ui.cbb_kh_lh.clear()
        for kh in data:
            self.ui.cbb_kh_lh.addItem(kh[1], kh[0])

    def load_dv_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, dv_ten FROM hcms_dichvu")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_dv_hdct.clear()
        for dv in data:
            self.ui.cbb_dv_hdct.addItem(dv[1], dv[0])

    def load_nv_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, nv_hoten FROM hcms_nhanvien")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_nv_hd.clear()
        for nv in data:
            self.ui.cbb_nv_hd.addItem(nv[1], nv[0])

    def load_dm_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, dm_dv_ten FROM hcms_danhmuc_dichvu")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_dm_dv.clear()
        for dm in data:
            self.ui.cbb_dm_dv.addItem(dm[1], dm[0])

    def show_kh_data(self):
        kh_list = Khachhang.get_all_user()

        self.ui.tbl_kh.setRowCount(0)
        self.ui.tbl_kh.setColumnCount(7)

        self.ui.tbl_kh.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_kh.setHorizontalHeaderItem(1, QTableWidgetItem("Họ tên"))
        self.ui.tbl_kh.setHorizontalHeaderItem(2, QTableWidgetItem("Giới tính"))
        self.ui.tbl_kh.setHorizontalHeaderItem(3, QTableWidgetItem("SĐT"))
        self.ui.tbl_kh.setHorizontalHeaderItem(4, QTableWidgetItem("Ngày sinh"))
        self.ui.tbl_kh.setHorizontalHeaderItem(5, QTableWidgetItem("Địa chỉ"))
        self.ui.tbl_kh.setHorizontalHeaderItem(6, QTableWidgetItem("Trạng thái"))

        for row, kh in enumerate(kh_list):
            self.ui.tbl_kh.insertRow(row)
            id_kh = str(kh[0])
            self.ui.tbl_kh.setItem(row, 0, QTableWidgetItem(id_kh))

            hoten = kh[1]
            self.ui.tbl_kh.setItem(row, 1, QTableWidgetItem(hoten))

            gt = "Nam" if kh[2] == 1 else "Nữ"
            self.ui.tbl_kh.setItem(row, 2, QTableWidgetItem(gt))

            sdt = kh[3]
            self.ui.tbl_kh.setItem(row, 3, QTableWidgetItem(sdt))

            ns = kh[4].strftime("%d-%m-%Y")
            self.ui.tbl_kh.setItem(row, 4, QTableWidgetItem(ns))

            dc = kh[5]
            self.ui.tbl_kh.setItem(row, 5, QTableWidgetItem(dc))

            tt = "Hoạt động" if kh[6] == 1 else "Dừng hoạt động"
            self.ui.tbl_kh.setItem(row, 6, QTableWidgetItem(tt))

        for col in range(7):
            self.ui.tbl_kh.resizeColumnToContents(col)

    def show_nv_data(self):
        nv_list = Nhanvien.get_all_emp()

        self.ui.tbl_nv.setRowCount(0)
        self.ui.tbl_nv.setColumnCount(10)

        self.ui.tbl_nv.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_nv.setHorizontalHeaderItem(1, QTableWidgetItem("Họ tên"))
        self.ui.tbl_nv.setHorizontalHeaderItem(2, QTableWidgetItem("Giới tính"))
        self.ui.tbl_nv.setHorizontalHeaderItem(3, QTableWidgetItem("SĐT"))
        self.ui.tbl_nv.setHorizontalHeaderItem(4, QTableWidgetItem("Ngày sinh"))
        self.ui.tbl_nv.setHorizontalHeaderItem(5, QTableWidgetItem("Địa chỉ"))
        self.ui.tbl_nv.setHorizontalHeaderItem(6, QTableWidgetItem("Chức vụ"))
        self.ui.tbl_nv.setHorizontalHeaderItem(7, QTableWidgetItem("Trạng thái"))
        self.ui.tbl_nv.setHorizontalHeaderItem(8, QTableWidgetItem("Mật khẩu"))
        self.ui.tbl_nv.setHorizontalHeaderItem(9, QTableWidgetItem("Quyền"))

        for row, nv in enumerate(nv_list):
            self.ui.tbl_nv.insertRow(row)
            id_nv = str(nv[0])
            self.ui.tbl_nv.setItem(row, 0, QTableWidgetItem(id_nv))

            hoten = nv[1]
            self.ui.tbl_nv.setItem(row, 1, QTableWidgetItem(hoten))

            gt = "Nam" if nv[2] == 1 else "Nữ"
            self.ui.tbl_nv.setItem(row, 2, QTableWidgetItem(gt))

            sdt = nv[3]
            self.ui.tbl_nv.setItem(row, 3, QTableWidgetItem(sdt))

            ns = nv[4]
            if ns is not None:
                ns = ns.strftime("%d-%m-%Y")
            else:
                ns = ""
            self.ui.tbl_nv.setItem(row, 4, QTableWidgetItem(ns))

            dc = nv[5]
            self.ui.tbl_nv.setItem(row, 5, QTableWidgetItem(dc))

            cv = "Quản lý" if nv[6] == 1 else "Nhân viên"
            self.ui.tbl_nv.setItem(row, 6, QTableWidgetItem(cv))

            tt = "Hoạt động" if nv[7] == 1 else "Dừng hoạt động"
            self.ui.tbl_nv.setItem(row, 7, QTableWidgetItem(tt))

            mk = nv[8]
            self.ui.tbl_nv.setItem(row, 8, QTableWidgetItem(mk))

            q = "Quản lý" if nv[9] == 1 else "Nhân viên"
            self.ui.tbl_nv.setItem(row, 9, QTableWidgetItem(q))

            for col in range(10):
                self.ui.tbl_nv.resizeColumnToContents(col)

    def show_dv_data(self):
        dv_list = Dichvu.get_all_services()

        self.ui.tbl_dv.setRowCount(0)
        self.ui.tbl_dv.setColumnCount(6)

        self.ui.tbl_dv.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_dv.setHorizontalHeaderItem(1, QTableWidgetItem("Tên dịch vụ"))
        self.ui.tbl_dv.setHorizontalHeaderItem(2, QTableWidgetItem("Đơn giá"))
        self.ui.tbl_dv.setHorizontalHeaderItem(3, QTableWidgetItem("Mô tả"))
        self.ui.tbl_dv.setHorizontalHeaderItem(4, QTableWidgetItem("Trạng thái"))
        self.ui.tbl_dv.setHorizontalHeaderItem(5, QTableWidgetItem("Danh mục"))

        for row, dv in enumerate(dv_list):
            self.ui.tbl_dv.insertRow(row)
            id_dv = str(dv[0])
            self.ui.tbl_dv.setItem(row, 0, QTableWidgetItem(id_dv))

            ten = dv[1]
            self.ui.tbl_dv.setItem(row, 1, QTableWidgetItem(ten))

            dg = str(dv[2])
            self.ui.tbl_dv.setItem(row, 2, QTableWidgetItem(dg))

            mt = dv[3]
            self.ui.tbl_dv.setItem(row, 3, QTableWidgetItem(mt))

            tt = "Hoạt động" if dv[4] == 1 else "Dừng hoạt động"
            self.ui.tbl_dv.setItem(row, 4, QTableWidgetItem(tt))

            dm_id = dv[5]
            dm_ten = Dichvu.get_dm_name(dm_id)
            self.ui.tbl_dv.setItem(row, 5, QTableWidgetItem(dm_ten))

            for col in range(6):
                self.ui.tbl_dv.resizeColumnToContents(col)

        self.load_dm_data()

    def show_lh_data(self):
        lh_list = Lichhen.get_all_app()

        self.ui.tbl_lh.setRowCount(0)
        self.ui.tbl_lh.setColumnCount(4)

        self.ui.tbl_lh.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_lh.setHorizontalHeaderItem(1, QTableWidgetItem("Ngày hẹn"))
        self.ui.tbl_lh.setHorizontalHeaderItem(2, QTableWidgetItem("Trạng thái"))
        self.ui.tbl_lh.setHorizontalHeaderItem(3, QTableWidgetItem("Khách hàng"))

        for row, lh in enumerate(lh_list):
            self.ui.tbl_lh.insertRow(row)
            id_lh = str(lh[0])
            self.ui.tbl_lh.setItem(row, 0, QTableWidgetItem(id_lh))

            ngay_hen = lh[1].strftime("%d-%m-%Y %H:%M:%S")
            self.ui.tbl_lh.setItem(row, 1, QTableWidgetItem(ngay_hen))

            trang_thai = "Xác nhận" if lh[2] == 1 else "Chờ xác nhận"
            self.ui.tbl_lh.setItem(row, 2, QTableWidgetItem(trang_thai))

            kh_lh_id = lh[3]
            kh_lh_ten = Khachhang.get_kh_name(kh_lh_id)
            self.ui.tbl_lh.setItem(row, 3, QTableWidgetItem(kh_lh_ten))

        for col in range(4):
            self.ui.tbl_lh.resizeColumnToContents(col)

    def show_hd_data(self):
        hd_list = Hoadon.get_all_bill()

        self.ui.tbl_hd.setRowCount(0)
        self.ui.tbl_hd.setColumnCount(11)

        self.ui.tbl_hd.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_hd.setHorizontalHeaderItem(1, QTableWidgetItem("Khách hàng"))
        self.ui.tbl_hd.setHorizontalHeaderItem(2, QTableWidgetItem("Tổng tiền"))
        self.ui.tbl_hd.setHorizontalHeaderItem(3, QTableWidgetItem("Ngày giờ tạo"))
        self.ui.tbl_hd.setHorizontalHeaderItem(4, QTableWidgetItem("Trạng thái"))
        self.ui.tbl_hd.setHorizontalHeaderItem(5, QTableWidgetItem("Mô tả"))
        self.ui.tbl_hd.setHorizontalHeaderItem(6, QTableWidgetItem("Nhân viên"))
        self.ui.tbl_hd.setHorizontalHeaderItem(7, QTableWidgetItem("ID Chi tiết hóa đơn"))
        self.ui.tbl_hd.setHorizontalHeaderItem(8, QTableWidgetItem("Số lượng"))
        self.ui.tbl_hd.setHorizontalHeaderItem(9, QTableWidgetItem("Dịch vụ"))
        self.ui.tbl_hd.setHorizontalHeaderItem(10, QTableWidgetItem("Hóa đơn"))

        for row, hd in enumerate(hd_list):
            self.ui.tbl_hd.insertRow(row)
            id_hd = str(hd[0])
            self.ui.tbl_hd.setItem(row, 0, QTableWidgetItem(id_hd))

            kh_id = hd[1]
            kh_name = Khachhang.get_kh_name(kh_id)
            self.ui.tbl_hd.setItem(row, 1, QTableWidgetItem(kh_name))

            ttien = str(hd[2])
            self.ui.tbl_hd.setItem(row, 2, QTableWidgetItem(ttien))

            if isinstance(hd[3], (int, float)):
                ngaytao = datetime.fromtimestamp(hd[3]).strftime("%d-%m-%Y %H:%M:%S")
            else:
                ngaytao = hd[3].strftime("%d-%m-%Y %H:%M:%S")
            self.ui.tbl_hd.setItem(row, 3, QTableWidgetItem(ngaytao))

            tt = "Xác nhận" if hd[4] == 1 else "Chờ xác nhận"
            self.ui.tbl_hd.setItem(row, 4, QTableWidgetItem(tt))

            mt = hd[5]
            self.ui.tbl_hd.setItem(row, 5, QTableWidgetItem(mt))

            nv_id = hd[6]
            nv_ten = Nhanvien.get_nv_name(nv_id)
            self.ui.tbl_hd.setItem(row, 6, QTableWidgetItem(nv_ten))

            id_hdct = str(hd[7])
            self.ui.tbl_hd.setItem(row, 7, QTableWidgetItem(id_hdct))

            sl = str(hd[8])
            self.ui.tbl_hd.setItem(row, 8, QTableWidgetItem(sl))

            dv_id = hd[9]
            dv_ten = Dichvu.get_dv_name(dv_id)
            self.ui.tbl_hd.setItem(row, 9, QTableWidgetItem(dv_ten))

            hd_id = str(hd[10])
            self.ui.tbl_hd.setItem(row, 10, QTableWidgetItem(hd_id))

            for col in range(11):
                self.ui.tbl_hd.resizeColumnToContents(col)

    def export_to_pdf(self):
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf);;All Files(*)")

            if file_path:
                pdf_doc = SimpleDocTemplate(file_path, pagesize=letter)
                n = self.ui.tbl_bctk.columnCount()
                m = self.ui.tbl_bctk.rowCount()

                headers = [self.ui.tbl_bctk.horizontalHeaderItem(col).text() for col in range(n)]

                data = [headers]

                for row in range(m):
                    row_data = [
                        self.ui.tbl_bctk.item(row, col).text() if self.ui.tbl_bctk.item(row, col) is not None else ""
                        for col in range(n)]
                    data.append(row_data)

                pdf_table = Table(data)

                pdfmetrics.registerFont(TTFont('Roboto-Black', 'font/Roboto-Black.ttf'))

                style = TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Roboto-Black'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Roboto-Black'),
                    ('FONTSIZE', (0, 0), (-1, -1), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ])

                pdf_table.setStyle(style)

                pdf_doc.build([pdf_table])
                print(f"PDF saved to {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def show_bao_cao_doanh_thu(self):
        try:
            bctk = BaoCaoThongKe(self.nam)
            doanh_thu_nam = bctk.bao_cao_doanh_thu_nam()
            print("Doanh thu nam:", doanh_thu_nam)

            self.ui.tbl_bctk.setRowCount(12)
            self.ui.tbl_bctk.setColumnCount(2)

            self.ui.tbl_bctk.setHorizontalHeaderItem(0, QTableWidgetItem("Tháng"))
            self.ui.tbl_bctk.setHorizontalHeaderItem(1, QTableWidgetItem("Doanh thu"))

            for row, dt in enumerate(doanh_thu_nam):
                self.ui.tbl_bctk.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                self.ui.tbl_bctk.setItem(row, 1, QTableWidgetItem(str(dt)))

            for col in range(2):
                self.ui.tbl_bctk.resizeColumnToContents(col)
        except Exception as e:
            print("Error loading doanh thu nam:", e)

    def show_bao_cao_so_luong_lich_hen_quy(self):
        try:
            bctk = BaoCaoThongKe(self.nam)
            so_luong_lich_hen_quy = bctk.bao_cao_so_luong_lich_hen_quy()
            print("So luong lich hen quy:", so_luong_lich_hen_quy)

            self.ui.tbl_bctk.setRowCount(3)
            self.ui.tbl_bctk.setColumnCount(2)

            self.ui.tbl_bctk.setHorizontalHeaderItem(0, QTableWidgetItem("Quý"))
            self.ui.tbl_bctk.setHorizontalHeaderItem(1, QTableWidgetItem("Số lượng lịch hẹn"))

            for row, sl in enumerate(so_luong_lich_hen_quy):
                self.ui.tbl_bctk.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                self.ui.tbl_bctk.setItem(row, 1, QTableWidgetItem(str(sl)))

            for col in range(2):
                self.ui.tbl_bctk.resizeColumnToContents(col)
        except Exception as e:
            print("Error loading so luong lich hen quy:", e)

    def reset_kh(self):
        self.ui.txt_hoten_kh.clear()
        self.ui.cbb_gioitinh_kh.setCurrentIndex(0)
        self.ui.date_ns_kh.setDate(QDate.currentDate())
        self.ui.txt_sdt_kh.clear()
        self.ui.txt_diachi_kh.clear()
        self.ui.cbb_trangthai_kh.setCurrentIndex(0)

    def reset_nv(self):
        self.ui.txt_hoten_nv.clear()
        self.ui.cbb_gioitinh_nv.setCurrentIndex(0)
        self.ui.date_ns_nv.setDate(QDate.currentDate())
        self.ui.txt_sdt_nv.clear()
        self.ui.txt_diachi_nv.clear()
        self.ui.cbb_trangthai_nv.setCurrentIndex(0)
        self.ui.cbb_chucvu.setCurrentIndex(0)
        self.ui.cbb_quyen.setCurrentIndex(0)
        self.ui.txt_matkhau.clear()

    def reset_dv(self):
        self.ui.txt_tendv.clear()
        self.ui.txt_dongia.clear()
        self.ui.cbb_dm_dv.setCurrentIndex(0)
        self.ui.txt_mota_dv.clear()
        self.ui.cbb_trangthai_dv.setCurrentIndex(0)

    def reset_lh(self):
        self.ui.cbb_kh_lh.setCurrentIndex(0)
        self.ui.date_lh.setDate(QDate.currentDate())
        self.ui.cbb_trangthai_lh.setCurrentIndex(0)

    def reset_hd(self):
        self.ui.cbb_kh_hd.setCurrentIndex(0)
        self.ui.txt_tongtien_hd.clear()
        self.ui.date_hd.setDate(QDate.currentDate())
        self.ui.cbb_dv_hdct.setCurrentIndex(0)
        self.ui.txt_soluong_hdct.clear()
        self.ui.txt_mota_hd.clear()

    def add_kh_ad(self):
        print("Gọi hàm 'add_kh_nv'")
        hoten = self.ui.txt_hoten_kh.text()
        print("hoten:", hoten)
        gioitinh = self.ui.cbb_gioitinh_kh.currentIndex()
        print("gioitinh:", gioitinh)

        if gioitinh == 0:  # "Nam" với index == 0
            gt = 1
        elif gioitinh == 1:  # "Nữ" với index == 1
            gt = 0

        print("gt:", gt)

        ngaysinh = self.ui.date_ns_kh.dateTime().toString("yyyy-MM-dd")
        print("ngaysinh:", ngaysinh)
        sdt = self.ui.txt_sdt_kh.text()
        print("sdt:", sdt)
        dchi = self.ui.txt_diachi_kh.text()
        print("dchi:", dchi)
        trangthai = self.ui.cbb_trangthai_kh.currentIndex()
        print("trangthai:", trangthai)

        if trangthai == 0:  # "Xác nhận" với index == 0
            tthai = 1
        elif trangthai == 1:  # "Chờ xác nhận" với index == 1
            tthai = 0

        print("tthai:", tthai)

        try:
            kh = Khachhang(hoten, gt, sdt, ngaysinh, dchi, tthai)
            print("Tạo khách hàng:", kh)
            kh.create_user()
            print("Gọi hàm 'create_user'")
            self.show_kh_data()
            self.load_kh_data()
            print("Gọi hàm 'show_kh_data'")
        except Exception as e:
            print(f"Error creating user: {e}")

    def call_kh_data(self):
        current_row_index = self.ui.tbl_kh.currentRow()
        if current_row_index != -1:
            hoten = self.ui.tbl_kh.item(current_row_index, 1).text()
            gioitinh = self.ui.tbl_kh.item(current_row_index, 2).text()
            ngaysinh = self.ui.tbl_kh.item(current_row_index, 4).text()
            sdt = self.ui.tbl_kh.item(current_row_index, 3).text()
            dchi = self.ui.tbl_kh.item(current_row_index, 5).text()
            trangthai = self.ui.tbl_kh.item(current_row_index, 6).text()

            self.ui.txt_hoten_kh.setText(hoten)
            self.ui.txt_sdt_kh.setText(sdt)
            self.ui.txt_diachi_kh.setText(dchi)

            if gioitinh == "Nam":
                self.ui.cbb_gioitinh_kh.setCurrentIndex(0)
            else:
                self.ui.cbb_gioitinh_kh.setCurrentIndex(1)

            if trangthai == "Hoạt động":
                self.ui.cbb_trangthai_kh.setCurrentIndex(0)
            else:
                self.ui.cbb_trangthai_kh.setCurrentIndex(1)

            date = QDateTime.fromString(ngaysinh, "dd-MM-yyyy")
            self.ui.date_ns_kh.setDateTime(date)

    def update_kh_ad(self):
        print("Gọi hàm 'update_kh_ad'")
        try:
            current_row_index = self.ui.tbl_kh.currentRow()
            item = self.ui.tbl_kh.item(current_row_index, 0)
            if item is not None:
                kh_id = item.text()
                hoten = self.ui.txt_hoten_kh.text()
                gioitinh = self.ui.cbb_gioitinh_kh.currentIndex()
                ngaysinh = self.ui.date_ns_kh.dateTime().toString("yyyy-MM-dd")
                sdt = self.ui.txt_sdt_kh.text()
                dchi = self.ui.txt_diachi_kh.text()
                trangthai = self.ui.cbb_trangthai_kh.currentIndex()

                if gioitinh == 0:  # "Nam" với index == 0
                    gt = 1
                elif gioitinh == 1:  # "Nữ" với index == 1
                    gt = 0

                if trangthai == 0:  # "Hoạt động" với index == 0
                    tthai = 1
                elif trangthai == 1:  # "Dừng hoạt động" với index == 1
                    tthai = 0

                # Hiển thị message box xác nhận
                reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn cập nhật thông tin này?',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    kh = Khachhang(hoten, gt, sdt, ngaysinh, dchi, tthai)
                    kh.update_user(kh_id)
                    self.show_kh_data()
                    self.load_kh_data()
                    QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
                    self.reset_kh()
                else:
                    print("Đã hủy cập nhật thông tin")
            else:
                QMessageBox.warning(self, "Warning", "Ô hiện tại không có dữ liệu")

        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", "Có lỗi xảy ra khi cập nhật thông tin")

    def del_kh_ad(self):
        print("Gọi 'del_kh_ad'")
        current_row_index = self.ui.tbl_kh.currentRow()
        if current_row_index != -1:
            kh_id = self.ui.tbl_kh.item(current_row_index, 0).text()
            print(f"Xóa khách hàng với id là: {kh_id}")

            try:
                msg_box = QMessageBox(self)
                msg_box.setText("Bạn có chắc chắn muốn xóa khách hàng này?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg_box.setDefaultButton(QMessageBox.StandardButton.No)
                result = msg_box.exec()

                if result == QMessageBox.StandardButton.Yes:
                    print("Đã xác nhận xóa")
                    Khachhang.delete_user(kh_id)
                    print(f"Đã xóa khách hàng tại id là: {kh_id}")
                    self.show_kh_data()
                    self.load_kh_data()
                    self.reset_kh()
                else:
                    print("Đã hủy xóa khách hàng")
            except Exception as e:
                print(f"Lỗi tại: {e}")

    def add_nv_ad(self):
        print("Gọi hàm 'add_nv_ad'")
        hoten = self.ui.txt_hoten_nv.text()
        print("hoten:", hoten)
        gioitinh = self.ui.cbb_gioitinh_nv.currentIndex()
        print("gioitinh:", gioitinh)

        if gioitinh == 0:  # "Nam" với index == 0
            gt = 1
        elif gioitinh == 1:  # "Nữ" với index == 1
            gt = 0

        print("gt:", gt)

        ngaysinh = self.ui.date_ns_nv.date().toString("yyyy-MM-dd")
        print("ngaysinh:", ngaysinh)
        sdt = self.ui.txt_sdt_nv.text()
        print("sdt:", sdt)
        dchi = self.ui.txt_diachi_nv.text()
        print("dchi:", dchi)
        cvu = self.ui.cbb_chucvu.currentIndex()
        print("cvu:", cvu)

        if cvu == 0:  # "Quản lý" với index == 0
            cv = 1
        elif cvu == 1:  # "Nhân viên" với index == 1
            cv = 0

        print("cvu:", cv)
        quyen = self.ui.cbb_quyen.currentIndex()
        print("quyen:", quyen)

        if quyen == 0:  # "Quản lý" với index == 0
            q = 0
        elif quyen == 1:  # "Nhân viên" với index == 1
            q = 1

        print("quyen:", q)
        trangthai = self.ui.cbb_trangthai_nv.currentIndex()
        print("trangthai:", trangthai)

        if trangthai == 0:  # "Xác nhận" với index == 0
            tthai = 1
        elif trangthai == 1:  # "Chờ xác nhận" với index == 1
            tthai = 0

        print("tthai:", tthai)

        mkhau = self.ui.txt_matkhau.text()
        print("mkhau:", mkhau)

        nv = Nhanvien(hoten, gt, sdt, ngaysinh, dchi, cv, tthai, mkhau, q)
        print("Tạo nhân viên:", nv)
        nv.create_emp()
        print("Gọi hàm 'create_emp'")
        self.show_nv_data()
        self.load_nv_data()
        print("Gọi hàm 'show_nv_data'")

    def call_nv_data(self):
        current_row_index = self.ui.tbl_nv.currentRow()
        if current_row_index != -1:
            hoten = self.ui.tbl_nv.item(current_row_index, 1).text()
            gioitinh = self.ui.tbl_nv.item(current_row_index, 2).text()
            ngaysinh = self.ui.tbl_nv.item(current_row_index, 4).text()
            sdt = self.ui.tbl_nv.item(current_row_index, 3).text()
            dchi = self.ui.tbl_nv.item(current_row_index, 5).text()
            cvu = self.ui.tbl_nv.item(current_row_index, 6).text()
            trangthai = self.ui.tbl_nv.item(current_row_index, 7).text()
            mk = self.ui.tbl_nv.item(current_row_index, 8).text()
            q = self.ui.tbl_nv.item(current_row_index, 9).text()

            self.ui.txt_hoten_nv.setText(hoten)
            self.ui.txt_sdt_nv.setText(sdt)
            self.ui.txt_diachi_nv.setText(dchi)
            self.ui.txt_matkhau.setText(mk)

            if gioitinh == "Nam":
                self.ui.cbb_gioitinh_kh.setCurrentIndex(0)
            else:
                self.ui.cbb_gioitinh_kh.setCurrentIndex(1)

            if trangthai == "Hoạt động":
                self.ui.cbb_trangthai_kh.setCurrentIndex(0)
            else:
                self.ui.cbb_trangthai_kh.setCurrentIndex(1)

            date = QDateTime.fromString(ngaysinh, "dd-MM-yyyy")
            self.ui.date_ns_nv.setDateTime(date)

            if cvu == "Nhân viên":
                self.ui.cbb_chucvu.setCurrentIndex(0)
            else:
                self.ui.cbb_chucvu.setCurrentIndex(1)

            if q == "Nhân viên":
                self.ui.cbb_quyen.setCurrentIndex(0)
            else:
                self.ui.cbb_quyen.setCurrentIndex(1)

    def update_nv_ad(self):
        print("Gọi hàm 'update_nv_ad'")
        try:
            current_row_index = self.ui.tbl_nv.currentRow()
            item = self.ui.tbl_nv.item(current_row_index, 0)
            if item is not None:
                nv_id = item.text()
                hoten = self.ui.txt_hoten_nv.text()
                gioitinh = self.ui.cbb_gioitinh_nv.currentIndex()
                ngaysinh = self.ui.date_ns_nv.dateTime().toString("yyyy-MM-dd")
                sdt = self.ui.txt_sdt_nv.text()
                dchi = self.ui.txt_diachi_nv.text()
                cvu = self.ui.cbb_chucvu.currentIndex()
                trangthai = self.ui.cbb_trangthai_nv.currentIndex()
                quyen = self.ui.cbb_quyen.currentIndex()
                mk = self.ui.txt_matkhau.text()

                if gioitinh == 0:  # "Nam" với index == 0
                    gt = 1
                elif gioitinh == 1:  # "Nữ" với index == 1
                    gt = 0

                if cvu == 0:  # "Nhân viên" với index == 0
                    chucvu = 0
                elif cvu == 1:  # "Quản lý" với index == 1
                    chucvu = 1

                if trangthai == 0:  # "Hoạt động" với index == 0
                    tthai = 1
                elif trangthai == 1:  # "Dừng hoạt động" với index == 1
                    tthai = 0

                if quyen == 0:  # "Nhân viên" với index == 0
                    q = 0
                elif quyen == 1:  # "Quản lý" với index == 1
                    q = 1

                # Hiển thị message box xác nhận
                reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn cập nhật thông tin này?',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    nv = Nhanvien(hoten, gt, sdt, ngaysinh, dchi, chucvu, tthai, mk, q)
                    nv.update_user(nv_id)
                    self.show_nv_data()
                    self.load_nv_data()
                    QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
                    self.reset_nv()
                else:
                    print("Đã hủy cập nhật thông tin")
            else:
                QMessageBox.warning(self, "Warning", "Ô hiện tại không có dữ liệu")

        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", "Có lỗi xảy ra khi cập nhật thông tin")

    def del_nv_ad(self):
        print("Gọi 'del_nv_ad'")
        current_row_index = self.ui.tbl_nv.currentRow()
        if current_row_index != -1:
            nv_id = self.ui.tbl_nv.item(current_row_index, 0).text()
            print(f"Xóa nhân viên với id là: {nv_id}")

            try:
                msg_box = QMessageBox(self)
                msg_box.setText("Bạn có chắc chắn muốn xóa nhân viên này?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg_box.setDefaultButton(QMessageBox.StandardButton.No)
                result = msg_box.exec()

                if result == QMessageBox.StandardButton.Yes:
                    print("Đã xác nhận xóa")
                    Nhanvien.delete_user(nv_id)
                    print(f"Đã xóa nhân viên tại id là: {nv_id}")
                    self.show_nv_data()
                    self.load_nv_data()
                    self.reset_nv()
                else:
                    print("Đã hủy xóa nhân viên")
            except Exception as e:
                print(f"Lỗi tại: {e}")

    def add_dv_ad(self):
        print("Gọi hàm 'add_dv_ad'")
        tendv = self.ui.txt_tendv.text()
        print("tendv:", tendv)
        dgia = self.ui.txt_dongia.text()
        print("dgia:", dgia)
        dm_id = self.ui.cbb_dm_dv.currentData()
        print("dm_id:", dm_id)
        motadv = self.ui.txt_mota_dv.text()
        print("motadv:", motadv)
        trangthai = self.ui.cbb_trangthai_dv.currentIndex()
        print("trangthai:", trangthai)

        if trangthai == 0:  # "Hoạt động" với index == 0
            tthai = 1
        elif trangthai == 1:  # "Dừng hoạt động" với index == 1
            tthai = 0

        print("tthai:", tthai)

        dv = Dichvu(tendv, dgia, motadv, tthai, dm_id)
        print("Tạo dịch vụ:", dv)
        dv.create_service()
        print("Gọi hàm 'create_service'")
        self.show_dv_data()
        self.load_dv_data()
        print("Gọi hàm 'show_dv_data'")

    def call_dv_data(self):
        current_row_index = self.ui.tbl_dv.currentRow()
        if current_row_index != -1:
            tendv = self.ui.tbl_dv.item(current_row_index, 1).text()
            dgia = self.ui.tbl_dv.item(current_row_index, 2).text()
            mota = self.ui.tbl_dv.item(current_row_index, 3).text()
            trangthai = self.ui.tbl_dv.item(current_row_index, 4).text()

            self.ui.txt_tendv.setText(tendv)
            self.ui.txt_dongia.setText(dgia)
            self.ui.txt_mota_dv.setText(mota)

            if trangthai == "Hoạt động":
                self.ui.cbb_trangthai_dv.setCurrentIndex(0)
            else:
                self.ui.cbb_trangthai_dv.setCurrentIndex(1)

    def update_dv_ad(self):
        print("Gọi hàm 'update_dv_ad'")
        try:
            current_row_index = self.ui.tbl_dv.currentRow()
            item = self.ui.tbl_dv.item(current_row_index, 0)
            if item is not None:
                dv_id = item.text()
                ten = self.ui.txt_tendv.text()
                dgia = self.ui.txt_dongia.text()
                dm_id = self.ui.cbb_dm_dv.itemData(self.ui.cbb_dm_dv.currentIndex())
                mota = self.ui.txt_mota_dv.text()
                trangthai = self.ui.cbb_trangthai_dv.currentIndex()

                if trangthai == 0:  # "Hoạt động" với index == 0
                    tthai = 1
                elif trangthai == 1:  # "Dừng hoạt động" với index == 1
                    tthai = 0

                # Hiển thị message box xác nhận
                reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn cập nhật thông tin này?',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    dv = Dichvu(ten, dgia, mota, tthai, dm_id)
                    dv.update_service(dv_id)
                    self.show_dv_data()
                    QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
                    self.reset_dv()
                    self.load_dv_data()
                else:
                    print("Đã hủy cập nhật thông tin")
            else:
                QMessageBox.warning(self, "Warning", "Ô hiện tại không có dữ liệu")

        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", "Có lỗi xảy ra khi cập nhật thông tin")

    def del_dv_ad(self):
        print("Gọi 'del_dv_ad'")
        current_row_index = self.ui.tbl_dv.currentRow()
        if current_row_index != -1:
            dv_id = self.ui.tbl_dv.item(current_row_index, 0).text()
            print(f"Xóa dịch vụ với id là: {dv_id}")

            try:
                msg_box = QMessageBox(self)
                msg_box.setText("Bạn có chắc chắn muốn xóa dịch vụ này?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg_box.setDefaultButton(QMessageBox.StandardButton.No)
                result = msg_box.exec()

                if result == QMessageBox.StandardButton.Yes:
                    print("Đã xác nhận xóa")
                    Dichvu.delete_service(dv_id)
                    print(f"Đã xóa dịch vụ tại id là: {dv_id}")
                    self.show_dv_data()
                    self.load_dv_data()
                    self.reset_dv()
                else:
                    print("Đã hủy xóa dịch vụ")
            except Exception as e:
                print(f"Lỗi tại: {e}")

    def call_lh_data(self):
        current_row_index = self.ui.tbl_lh.currentRow()
        if current_row_index != -1:
            ngayhen = self.ui.tbl_lh.item(current_row_index, 1).text()
            trangthai = self.ui.tbl_lh.item(current_row_index, 2).text()

            date = QDateTime.fromString(ngayhen, "dd-MM-yyyy hh:mm:ss")
            self.ui.date_lh.setDateTime(date)

            if trangthai == "Xác nhận":
                self.ui.cbb_trangthai_lh.setCurrentIndex(0)
            else:
                self.ui.cbb_trangthai_lh.setCurrentIndex(1)

    def update_lh_ad(self):
        print("Gọi hàm 'update_lh_ad'")
        try:
            current_row_index = self.ui.tbl_lh.currentRow()
            item = self.ui.tbl_lh.item(current_row_index, 0)
            if item is not None:
                lh_id = item.text()
                ngayhen = self.ui.date_lh.dateTime().toString("yyyy-MM-dd hh:mm:ss")
                trangthai = self.ui.cbb_trangthai_lh.currentIndex()
                kh_id = self.ui.cbb_kh_lh.itemData(self.ui.cbb_kh_lh.currentIndex())

                if trangthai == 0:  # "Xác nhận" với index == 0
                    tthai = 1
                elif trangthai == 1:  # "Chờ xác nhận" với index == 1
                    tthai = 0

                # Hiển thị message box xác nhận
                reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn cập nhật thông tin này?',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    lh = Lichhen(ngayhen, tthai, kh_id)
                    lh.update_app(lh_id)
                    self.show_lh_data()
                    QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
                    self.reset_lh()
                else:
                    print("Đã hủy cập nhật thông tin")
            else:
                QMessageBox.warning(self, "Warning", "Ô hiện tại không có dữ liệu")

        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", "Có lỗi xảy ra khi cập nhật thông tin")

    def del_lh_ad(self):
        print("Gọi 'del_lh_ad'")
        current_row_index = self.ui.tbl_lh.currentRow()
        if current_row_index != -1:
            lh_id = self.ui.tbl_lh.item(current_row_index, 0).text()
            print(f"Xóa lịch hẹn với id là: {lh_id}")

            try:
                msg_box = QMessageBox(self)
                msg_box.setText("Bạn có chắc chắn muốn xóa lịch hẹn này?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg_box.setDefaultButton(QMessageBox.StandardButton.No)
                result = msg_box.exec()

                if result == QMessageBox.StandardButton.Yes:
                    print("Đã xác nhận xóa")
                    Lichhen.delete_app(lh_id)
                    print(f"Đã xóa lịch hẹn tại id là: {lh_id}")
                    self.show_lh_data()
                else:
                    print("Đã hủy xóa lịch hẹn")
            except Exception as e:
                print(f"Lỗi tại: {e}")

    def call_hd_data(self):
        current_row_index = self.ui.tbl_hd.currentRow()
        if current_row_index != -1:
            ttien = self.ui.tbl_hd.item(current_row_index, 2).text()
            ngaytao = self.ui.tbl_hd.item(current_row_index, 3).text()
            mota = self.ui.tbl_hd.item(current_row_index, 5).text()
            sl = self.ui.tbl_hd.item(current_row_index, 8).text()
            trangthai = self.ui.tbl_hd.item(current_row_index, 4).text()

            self.ui.txt_tongtien_hd.setText(ttien)
            self.ui.txt_soluong_hdct.setText(sl)
            self.ui.txt_mota_hd.setText(mota)

            if trangthai == "Xác nhận":
                self.ui.cbb_trangthai_hd.setCurrentIndex(0)
            else:
                self.ui.cbb_trangthai_hd.setCurrentIndex(1)

            date = QDateTime.fromString(ngaytao, "dd-MM-yyyy hh:mm:ss")
            self.ui.date_hd.setDateTime(date)

    def del_hd_ad(self):
        print("Gọi 'del_hd_ad'")
        current_row_index = self.ui.tbl_hd.currentRow()
        if current_row_index != -1:
            hd_id = self.ui.tbl_hd.item(current_row_index, 0).text()
            print(f"Xóa hóa đơn với id là: {hd_id}")

            try:
                msg_box = QMessageBox(self)
                msg_box.setText("Bạn có chắc chắn muốn xóa hóa đơn này?")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                msg_box.setDefaultButton(QMessageBox.StandardButton.No)
                result = msg_box.exec()

                if result == QMessageBox.StandardButton.Yes:
                    print("Đã xác nhận xóa")
                    Hoadon.delete_bill(hd_id)
                    print(f"Đã xóa hóa đơn tại id là: {hd_id}")
                    self.show_hd_data()
                else:
                    print("Đã hủy xóa hóa đơn")
            except Exception as e:
                print(f"Lỗi tại: {e}")

    def update_hd_ad(self):
        print("Gọi hàm 'update_hd_ad'")
        try:
            current_row_index = self.ui.tbl_hd.currentRow()
            item = self.ui.tbl_hd.item(current_row_index, 0)
            if item is not None:
                hd_id = item.text()
                kh_id = self.ui.cbb_kh_hd.itemData(self.ui.cbb_kh_hd.currentIndex())
                nv_id = self.ui.cbb_nv_hd.itemData(self.ui.cbb_nv_hd.currentIndex())
                ttien = self.ui.txt_tongtien_hd.text()
                ngaytao = self.ui.date_hd.dateTime().toString("yyyy-MM-dd hh:mm:ss")
                dv_id = self.ui.cbb_dv_hdct.itemData(self.ui.cbb_dv_hdct.currentIndex())
                sl = self.ui.txt_soluong_hdct.text()
                mota = self.ui.txt_mota_hd.text()
                trangthai = self.ui.cbb_trangthai_hd.currentIndex()

                tthai = 1 if trangthai == 0 else 0

                reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn cập nhật thông tin này?',
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                             QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    hd = Hoadon(ttien, ngaytao, tthai, mota, kh_id, nv_id, None, None, None)
                    if hd.exists(hd_id):
                        hd.update_bill(hd_id, hd_id)

                        hdct_id = self.ui.tbl_hd.item(current_row_index, 7).text()
                        hdct = Hoadon(None, None, None, None, None, None, sl, dv_id, hdct_id)
                        hdct.update_hdct(hdct_id)

                        self.show_hd_data()
                        QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
                        self.reset_hd()
                    else:
                        QMessageBox.warning(self, "Warning", "Hóa đơn không tồn tại")
            else:
                QMessageBox.warning(self, "Warning", "Ô hiện tại không có dữ liệu")

        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", "Có lỗi xảy ra khi cập nhật thông tin")

    def update_tk(self):
        print("Gọi hàm 'update_tk_nv'")
        try:
            sdt = self.ui.txt_sdt_tk.text()
            matkhau = self.ui.txt_matkhau_tk.text()
            user = Session.get_current_user()

            if user:
                user.sdt = sdt
                user.matkhau = matkhau

                user.update_nv_acc()
                self.show_nv_data()
                self.ui.txt_matkhau_tk.clear()
                QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
            else:
                raise Exception("Không tìm thấy thông tin người dùng")
        except Exception as e:
            print(f"Error updating user: {e}")
            QMessageBox.critical(self, "Error", str(e))

    def logout(self):
        Session.logout()
        self.close()
        self.login_window = Login_MainWindow()
        self.login_window.show()

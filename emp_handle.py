from datetime import datetime

from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow, QFileDialog
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from config import dbconnect
from models.dichvu import Dichvu
from models.hoadon import Hoadon
from models.khachhang import Khachhang
from models.lichhen import Lichhen
from models.nhanvien import Nhanvien
from models.session import Session
from log_handle import Login_MainWindow
from views.nhanvien import Ui_nhanvien_window


class Emp_MainWindow(QMainWindow):
    def __init__(self):
        super(Emp_MainWindow, self).__init__()

        self.login_window = None
        self.ui = Ui_nhanvien_window()
        self.ui.setupUi(self)

        current_user = Session.get_current_user()
        current_user_id = Session.get_current_user_id()
        if current_user and current_user_id:
            print(f"Đăng nhập với: {current_user.sdt} , id: {current_user_id}")
            self.ui.txt_sdt_tk_nv.setText(current_user.sdt)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btn_lh.clicked.connect(self.page_lh_toggle)
        self.ui.btn_hd.clicked.connect(self.page_hd_toggle)
        self.ui.btn_tk.clicked.connect(self.page_tk_toggle)

        self.load_kh_data()
        self.load_dv_data()
        self.show_data_lh()

        self.ui.btn_them_lh.clicked.connect(self.add_lh_nv)
        self.ui.btn_xuat_hd.clicked.connect(self.add_hd_nv)
        self.ui.btn_xacnhan_tk.clicked.connect(self.update_tk_nv)

        self.ui.btn_huy_hd.clicked.connect(self.export_to_pdf)

        self.ui.btn_exit.clicked.connect(self.logout)

    def page_lh_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def page_hd_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def page_tk_toggle(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def show_data_lh(self):
        lichhen_list = Lichhen.get_all_app()
        self.ui.tb_lh.setRowCount(0)
        self.ui.tb_lh.setColumnCount(3)

        self.ui.tb_lh.setHorizontalHeaderItem(0, QTableWidgetItem("Ngày hẹn"))
        self.ui.tb_lh.setHorizontalHeaderItem(1, QTableWidgetItem("Trạng thái"))
        self.ui.tb_lh.setHorizontalHeaderItem(2, QTableWidgetItem("Khách hàng"))

        for row, lichhen in enumerate(lichhen_list):
            self.ui.tb_lh.insertRow(row)

            ngay_hen = lichhen[1].strftime("%d-%m-%Y %H:%M:%S")
            self.ui.tb_lh.setItem(row, 0, QTableWidgetItem(ngay_hen))

            trang_thai = "Xác nhận" if lichhen[2] == 1 else "Chờ xác nhận"
            self.ui.tb_lh.setItem(row, 1, QTableWidgetItem(trang_thai))

            kh_id = lichhen[3]
            kh_ten = Khachhang.get_kh_name(kh_id)
            self.ui.tb_lh.setItem(row, 2, QTableWidgetItem(kh_ten))

        for col in range(4):
            self.ui.tb_lh.resizeColumnToContents(col)

    def load_kh_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, kh_hoten FROM hcms_khachhang")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_kh_lh.clear()
        for kh in data:
            self.ui.cbb_kh_lh.addItem(kh[1], kh[0])

        self.ui.cbb_kh_hdct.clear()
        for kh in data:
            self.ui.cbb_kh_hdct.addItem(kh[1], kh[0])

    def load_dv_data(self):
        conn = dbconnect.dbconfig()
        conn.connectdb()

        conn.cur.execute("SELECT id, dv_ten FROM hcms_dichvu")
        data = conn.cur.fetchall()
        conn.close_connect()

        self.ui.cbb_dv_hdct.clear()
        for dv in data:
            self.ui.cbb_dv_hdct.addItem(dv[1], dv[0])

    def add_lh_nv(self):
        print("Gọi hàm 'add_lh_nv'")
        ngayhen = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        print("ngayhen:", ngayhen)
        kh_id = self.ui.cbb_kh_lh.currentData()
        print("kh_id:", kh_id)
        trangthai = self.ui.cbb_trangthai_lh.currentIndex()
        print("trangthai:", trangthai)

        if trangthai == 0:  # "Chờ xác nhận" với index == 0
            tthai = 0

        print("tthai:", tthai)

        lh = Lichhen(ngayhen, tthai, kh_id)
        print("Tạo lịch hẹn:", lh)
        lh.create_app()
        print("Gọi hàm 'create_app'")
        self.show_data_lh()
        self.load_kh_data()
        self.load_dv_data()
        print("Gọi hàm 'show_data_lh'")

    def show_hd_data(self):
        hd_list = Hoadon.get_latest_bill()

        self.ui.tbl_hd_nv.setRowCount(0)
        self.ui.tbl_hd_nv.setColumnCount(11)

        self.ui.tbl_hd_nv.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(1, QTableWidgetItem("Khách hàng"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(2, QTableWidgetItem("Tổng tiền"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(3, QTableWidgetItem("Ngày giờ tạo"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(4, QTableWidgetItem("Trạng thái"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(5, QTableWidgetItem("Mô tả"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(6, QTableWidgetItem("Nhân viên"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(7, QTableWidgetItem("ID Chi tiết hóa đơn"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(8, QTableWidgetItem("Số lượng"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(9, QTableWidgetItem("Dịch vụ"))
        self.ui.tbl_hd_nv.setHorizontalHeaderItem(10, QTableWidgetItem("Hóa đơn"))

        for row, hd in enumerate(hd_list):
            self.ui.tbl_hd_nv.insertRow(row)
            id_hd = str(hd[0])
            self.ui.tbl_hd_nv.setItem(row, 0, QTableWidgetItem(id_hd))

            kh_id = hd[1]
            kh_name = Khachhang.get_kh_name(kh_id)
            self.ui.tbl_hd_nv.setItem(row, 1, QTableWidgetItem(kh_name))

            ttien = str(hd[2])
            self.ui.tbl_hd_nv.setItem(row, 2, QTableWidgetItem(ttien))

            if isinstance(hd[3], (int, float)):
                ngaytao = datetime.fromtimestamp(hd[3]).strftime("%d-%m-%Y %H:%M:%S")
            else:
                ngaytao = hd[3].strftime("%d-%m-%Y %H:%M:%S")
            self.ui.tbl_hd_nv.setItem(row, 3, QTableWidgetItem(ngaytao))

            tt = "Xác nhận" if hd[4] == 1 else "Chờ xác nhận"
            self.ui.tbl_hd_nv.setItem(row, 4, QTableWidgetItem(tt))

            mt = hd[5]
            self.ui.tbl_hd_nv.setItem(row, 5, QTableWidgetItem(mt))

            nv_id = hd[6]
            nv_ten = Nhanvien.get_nv_name(nv_id)
            self.ui.tbl_hd_nv.setItem(row, 6, QTableWidgetItem(nv_ten))

            id_hdct = str(hd[7])
            self.ui.tbl_hd_nv.setItem(row, 7, QTableWidgetItem(id_hdct))

            sl = str(hd[8])
            self.ui.tbl_hd_nv.setItem(row, 8, QTableWidgetItem(sl))

            dv_id = hd[9]
            dv_ten = Dichvu.get_dv_name(dv_id)
            self.ui.tbl_hd_nv.setItem(row, 9, QTableWidgetItem(dv_ten))

            hd_id = str(hd[10])
            self.ui.tbl_hd_nv.setItem(row, 10, QTableWidgetItem(hd_id))

            for col in range(11):
                self.ui.tbl_hd_nv.resizeColumnToContents(col)

    def add_hd_nv(self):
        try:
            print("Gọi hàm 'add_hd_nv'")
            kh_id = self.ui.cbb_kh_hdct.currentData()
            print("kh_id:", kh_id)
            dv_id = self.ui.cbb_dv_hdct.currentData()
            print("dv_id:", dv_id)
            sl = self.ui.txt_soluong_hdct.text()
            print("sl:", sl)
            ttien = self.ui.txt_tongtien_hd.text()
            print("ttien:", ttien)
            ngaytao = self.ui.date_hd.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            print("ngaytao:", ngaytao)
            mota = self.ui.txt_mota_hd.text()
            print("mota:", mota)
            trangthai = self.ui.cbb_trangthai_lh.currentIndex()
            print("trangthai:", trangthai)

            if trangthai == 0:  # "Xác nhận" với index == 0
                tthai = 1
            elif trangthai == 1:  # "Chờ xác nhận" với index == 1
                tthai = 0

            print("tthai:", tthai)

            # Lấy ID của nhân viên đang đăng nhập từ Session
            nhanvien_id = Session.get_current_user_id()

            # Tạo đối tượng Hoadon
            hoadon_obj = Hoadon(
                tongtien=ttien,
                ngaygiotao=ngaytao,
                trangthai=tthai,
                mota=mota,
                khachhang=kh_id,
                nhanvien=nhanvien_id,
                soluong=sl,
                dichvu=dv_id,
                hoadon=None  # Sẽ được gán sau khi tạo hóa đơn
            )

            # Tạo hóa đơn
            hd_id = hoadon_obj.create_bill()

            # Tạo chi tiết hóa đơn
            hoadon_obj.hoadon = hd_id  # Gán ID hóa đơn mới tạo vào chi tiết hóa đơn
            hoadon_obj.create_bill_detail()
            self.show_hd_data()

            QMessageBox.information(self, "Thông báo", "Thêm hóa đơn thành công.")

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi thêm hóa đơn: {str(e)}")
            print(f"Lỗi khi thêm hóa đơn: {str(e)}")

    def export_to_pdf(self):
        try:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "Save PDF File", "", "PDF Files (*.pdf);;All Files(*)")

            if file_path:
                pdf_doc = SimpleDocTemplate(file_path, pagesize=letter)
                n = self.ui.tbl_hd_nv.columnCount()
                m = self.ui.tbl_hd_nv.rowCount()

                headers = [self.ui.tbl_hd_nv.horizontalHeaderItem(col).text() for col in range(n)]

                data = [headers]

                for row in range(m):
                    row_data = [
                        self.ui.tbl_hd_nv.item(row, col).text() if self.ui.tbl_hd_nv.item(row,
                                                                                        col) is not None else ""
                        for col in range(n)]
                    data.append(row_data)

                pdf_table = Table(data)

                pdfmetrics.registerFont(TTFont('Roboto-Black', 'font/Roboto-Black.ttf'))

                style = TableStyle([
                    ('FONTNAME', (0, 0), (-1, 0), 'Roboto-Black'),
                    ('FONTNAME', (0, 1), (-1, -1), 'Roboto-Black'),
                    ('FONTSIZE', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ])

                pdf_table.setStyle(style)

                pdf_doc.build([pdf_table])
                print(f"PDF saved to {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_tk_nv(self):
        print("Gọi hàm 'update_tk_nv'")
        sdt = self.ui.txt_sdt_tk_nv.text()
        matkhau = self.ui.txt_matkhau_nv.text()
        user = Session.get_current_user()

        if user:
            user.sdt = sdt
            user.matkhau = matkhau

            user.update_nv_acc()
            self.ui.txt_matkhau_nv.clear()
            QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
        else:
            QMessageBox.critical(self, "Error", "Không tìm thấy thông tin người dùng")

    def logout(self):
        Session.logout()
        self.close()
        self.login_window = Login_MainWindow()
        self.login_window.show()

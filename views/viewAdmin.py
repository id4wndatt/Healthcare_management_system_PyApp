from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDialog
from ui_Admin import Ui_MainWindown

class viewAdmin(QMainWindow, Ui_MainWindown):
    def  __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindownTitle("Admin")

        self.icon_name_widget.setHidden(True)

        self.btnThongTinKhachHang_1.clicked.connect(self.swich_to_page_ThongTinKhachHang())
        self.btnThongTinKhachHang_2.clicked.connect(self.swich_to_page_ThongTinKhachHang())

        self.btnDanhSachLichHen_1.clicked.connect(self.swich_to_page_DanhSachLichHen())
        self.btnDanhSachLichHen_2.clicked.connect(self.swich_to_page_DanhSachLichHen())

        self.btnDanhSachHoaDon_1.clicked.connect(self.swich_to_page_DanhSachHoaDon())
        self.btnDanhSachHoaDon_2.clicked.connect(self.swich_to_page_DanhSachHoaDon())

        self.btnDanhSachDichVu_2.clicked.connect(self.swich_to_page_DanHSachDichVu())
        self.bbtnDanhSachDichVu_2.clicked.connect(self.swich_to_page_DanHSachDichVu())


        self.btnBaoCaoThongKe_1.clicked.connect(self.swich_to_page_BaoCaoThongKe())
        self.btnBaoCaoThongKe_2.clicked.connect(self.swich_to_page_BaoCaoThongKe())

    def swich_to_page_ThongTinKhachHang(self):
        self.stackedWidget.setCurrentInDex(0)

    def swich_to_page_DanhSachLichHen(self):
        self.stackedWidget.setCurrentInDex(1)

    def swich_to_page_DanhSachHoaDon(self):
        self.stackedWidget.setCurrentInDex(2)

    def swich_to_page_DanHSachDichVu(self):
        self.stackedWidget.setCurrentInDex(3)

    def swich_to_page_BaoCaoThongKe(self):
        self.stackedWidget.setCurrentInDex(4)








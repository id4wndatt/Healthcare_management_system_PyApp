from PyQt6.QtWidgets import QMainWindow, QMessageBox

from models.session import Session
from models.user import User
from views.login import Ui_Login


class Login_MainWindow(QMainWindow):
    def __init__(self):
        super(Login_MainWindow, self).__init__()

        self.quanly_window = None
        self.emp_window = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.bntSignIn.clicked.connect(self.login)

    def login(self):
        try:
            sdt = self.ui.txtEmail.text()
            matkhau = self.ui.txtPassword.text()

            print("Đăng nhập với:", sdt, matkhau)

            user = User(None, None, sdt, None, None, None, matkhau)
            role = user.log_user()

            print("Quyền:", role)

            if role == 'admin' or role == 'employee':
                Session.login(user)
                if role == 'admin':
                    from admin_hanndle import Admin_MainWindow
                    self.quanly_window = Admin_MainWindow()
                else:
                    from emp_handle import Emp_MainWindow
                    self.emp_window = Emp_MainWindow()
                self.quanly_window.show() if role == 'admin' else self.emp_window.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error", "Sai số điện thoại hoặc mật khẩu")
        except Exception as e:
            print(f"Lỗi khi đăng nhập: {e}")
            QMessageBox.critical(self, "Error", str(e))
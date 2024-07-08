# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(442, 338)
        font = QtGui.QFont()
        font.setItalic(False)
        Login.setFont(font)
        Login.setStyleSheet("background-color: #FFFFFF;\n"
"display: inline-block;\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbDichvu_2 = QtWidgets.QLabel(parent=self.widget)
        self.lbDichvu_2.setMinimumSize(QtCore.QSize(0, 60))
        self.lbDichvu_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbDichvu_2.setFont(font)
        self.lbDichvu_2.setObjectName("lbDichvu_2")
        self.verticalLayout_3.addWidget(self.lbDichvu_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbEmail = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbEmail.setFont(font)
        self.lbEmail.setObjectName("lbEmail")
        self.verticalLayout.addWidget(self.lbEmail)
        self.txtEmail = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setKerning(True)
        self.txtEmail.setFont(font)
        self.txtEmail.setStyleSheet("    border-radius: 10px; \n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px; \n"
"    background-color: white; \n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3);")
        self.txtEmail.setObjectName("txtEmail")
        self.verticalLayout.addWidget(self.txtEmail)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbPassword = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setKerning(True)
        self.lbPassword.setFont(font)
        self.lbPassword.setObjectName("lbPassword")
        self.verticalLayout_2.addWidget(self.lbPassword)
        self.txtPassword = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setStyleSheet("    border-radius: 10px; /* Bo góc 10px */\n"
"    border: 1px solid #cccccc; /* Đường viền */\n"
"    padding: 5px; /* Khoảng cách bên trong */\n"
"    background-color: white; /* Nền trắng */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3);")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtPassword.setPlaceholderText("")
        self.txtPassword.setObjectName("txtPassword")
        self.verticalLayout_2.addWidget(self.txtPassword)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.bntSignIn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setItalic(False)
        self.bntSignIn.setFont(font)
        self.bntSignIn.setStyleSheet("    border-radius: 10px; /* Bo góc 10px */\n"
"    border: 1px solid #cccccc; /* Đường viền */\n"
"    padding: 5px; /* Khoảng cách bên trong */\n"
"    background-color: white; /* Nền trắng */\n"
"    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3);\n"
"    background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.bntSignIn.setObjectName("bntSignIn")
        self.verticalLayout_3.addWidget(self.bntSignIn)
        self.horizontalLayout.addWidget(self.widget)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.lbDichvu_2.setText(_translate("Login", "HCMS"))
        self.lbEmail.setText(_translate("Login", "SĐT"))
        self.lbPassword.setText(_translate("Login", "MẬT KHẨU"))
        self.bntSignIn.setText(_translate("Login", "ĐĂNG NHẬP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
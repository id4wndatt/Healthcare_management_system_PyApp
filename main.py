import sys

from PyQt6.QtWidgets import QApplication
from log_handle import Login_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = Login_MainWindow()
    login_window.show()

    sys.exit(app.exec())

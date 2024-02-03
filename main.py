from PySide6.QtWidgets import QApplication,QMainWindow
from ui.mainwindow_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    

if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    main_window = MainWindow()

    # window = LoginWindow(main_window)
    # window.show()
    main_window.show()

    sys.exit(app.exec())
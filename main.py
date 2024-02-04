from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
from ui.mainwindow_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.history_btn.clicked.connect(self.history_btn_clicked)
        self.ui.temperature_btn.clicked.connect(self.temperature_btn_clicked)
         # 连接所有按钮的点击事件到同一个槽函数
        for button in self.findChildren(QPushButton):
            button.clicked.connect(self.onButtonClicked)
    def temperature_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)        
    def history_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def onButtonClicked(self):
        # 获取发送信号的按钮对象
        sender_button = self.sender()

        # 获取按钮的名称
        button_name = sender_button.objectName()

        print(f"Clicked button with name: {button_name}")
   
if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    main_window = MainWindow()

    
    main_window.show()

    sys.exit(app.exec())
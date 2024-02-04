from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QWidget
from ui.mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import Qt,QTimer
from temperature_reader import TemperatureReader
from sql_class import temperature_db
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 创建TemperatureReader和TemperatureDB实例
        self.temperature_reader = TemperatureReader()
        self.temperature_db = temperature_db()

        # 创建 QTimer，并连接 timeout 信号到更新函数
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_temperature)

        # 设置定时器间隔为5秒
        self.timer_interval = 5000  # 毫秒
        self.timer.start(self.timer_interval)
        
        self.ui.history_btn.clicked.connect(self.history_btn_clicked)
        self.ui.temperature_btn.clicked.connect(self.temperature_btn_clicked)

        # 创建temperature_db类的实例
        self.db_instance = temperature_db()

        # 将所有按钮的点击事件连接到同一个槽函数
        for button in self.findChildren(QPushButton):
            button.clicked.connect(self.onButtonClicked)

        

    def temperature_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def history_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def onButtonClicked(self):
        # 获取发送信号的按钮对象
        sender_button = self.sender()

        # 获取按钮的名称和checked状态
        button_name = sender_button.objectName()
        is_checked = sender_button.isChecked()

        print(f"按钮 {button_name} 的checked状态: {is_checked}")

        # 在temperature_db实例上调用实例方法
        recv = self.db_instance.on_button_clicked(button_name)
        print(recv)

        # 根据获取的值设置QLabel的背景颜色
        self.set_label_background_color(recv, is_checked)

    def set_label_background_color(self, value, is_checked):
        # 遍历窗口的所有子部件
        for widget in self.findChildren(QWidget):
            # 仅处理QLabel部件
            if isinstance(widget, QLabel):
                # 检查QLabel的objectName是否与value相匹配
                if widget.objectName() == value:
                    # 根据按钮的checked状态设置背景颜色
                    text_color = "green" if is_checked else "black"
                    widget.setStyleSheet(f"color: {text_color};")

    def read_temperature(self):
        if self.temperature_reader.connect():
            # 读取温度
            temperatures = self.temperature_reader.read_temperature()

if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec())       

        
           

        

   


 
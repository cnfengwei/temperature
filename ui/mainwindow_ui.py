# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 808)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.daohang = QFrame(self.centralwidget)
        self.daohang.setObjectName(u"daohang")
        self.daohang.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.daohang.setFrameShape(QFrame.StyledPanel)
        self.daohang.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.daohang)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_5 = QPushButton(self.daohang)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.line = QFrame(self.daohang)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(29)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.daohang)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.daohang)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.daohang)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_4 = QPushButton(self.daohang)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pushButton_4)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.daohang, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1_main = QWidget()
        self.page1_main.setObjectName(u"page1_main")
        self.verticalLayout_2 = QVBoxLayout(self.page1_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.fdn1in_btn = QPushButton(self.page1_main)
        self.fdn1in_btn.setObjectName(u"fdn1in_btn")
        self.fdn1in_btn.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Suruma"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.fdn1in_btn.setFont(font)
        self.fdn1in_btn.setMouseTracking(False)
        self.fdn1in_btn.setTabletTracking(False)
        self.fdn1in_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.fdn1in_btn.setAutoRepeatDelay(301)
        self.fdn1in_btn.setAutoDefault(False)
        self.fdn1in_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.fdn1in_btn)

        self.fdn1intm = QLabel(self.page1_main)
        self.fdn1intm.setObjectName(u"fdn1intm")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fdn1intm.sizePolicy().hasHeightForWidth())
        self.fdn1intm.setSizePolicy(sizePolicy2)
        self.fdn1intm.setMinimumSize(QSize(100, 30))
        self.fdn1intm.setFont(font)
        self.fdn1intm.setAutoFillBackground(True)
        self.fdn1intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1intm.setFrameShape(QFrame.Panel)
        self.fdn1intm.setFrameShadow(QFrame.Sunken)
        self.fdn1intm.setTextFormat(Qt.AutoText)
        self.fdn1intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.fdn1intm)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.fdn1in_btn_2 = QPushButton(self.page1_main)
        self.fdn1in_btn_2.setObjectName(u"fdn1in_btn_2")
        self.fdn1in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn1in_btn_2.setFont(font)

        self.horizontalLayout_19.addWidget(self.fdn1in_btn_2)

        self.fdn1intm_2 = QLabel(self.page1_main)
        self.fdn1intm_2.setObjectName(u"fdn1intm_2")
        sizePolicy2.setHeightForWidth(self.fdn1intm_2.sizePolicy().hasHeightForWidth())
        self.fdn1intm_2.setSizePolicy(sizePolicy2)
        self.fdn1intm_2.setMinimumSize(QSize(100, 30))
        self.fdn1intm_2.setFont(font)
        self.fdn1intm_2.setAutoFillBackground(True)
        self.fdn1intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1intm_2.setFrameShape(QFrame.Panel)
        self.fdn1intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn1intm_2.setTextFormat(Qt.AutoText)
        self.fdn1intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.fdn1intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_19, 0, 1, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(6)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.fdn1in_btn_3 = QPushButton(self.page1_main)
        self.fdn1in_btn_3.setObjectName(u"fdn1in_btn_3")
        self.fdn1in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn1in_btn_3.setFont(font)

        self.horizontalLayout_31.addWidget(self.fdn1in_btn_3)

        self.fdn1intm_3 = QLabel(self.page1_main)
        self.fdn1intm_3.setObjectName(u"fdn1intm_3")
        sizePolicy2.setHeightForWidth(self.fdn1intm_3.sizePolicy().hasHeightForWidth())
        self.fdn1intm_3.setSizePolicy(sizePolicy2)
        self.fdn1intm_3.setMinimumSize(QSize(100, 30))
        self.fdn1intm_3.setFont(font)
        self.fdn1intm_3.setAutoFillBackground(True)
        self.fdn1intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1intm_3.setFrameShape(QFrame.Panel)
        self.fdn1intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn1intm_3.setTextFormat(Qt.AutoText)
        self.fdn1intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.fdn1intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_31, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.fdn1out_brn = QPushButton(self.page1_main)
        self.fdn1out_brn.setObjectName(u"fdn1out_brn")
        self.fdn1out_brn.setMinimumSize(QSize(0, 30))
        self.fdn1out_brn.setFont(font)

        self.horizontalLayout_2.addWidget(self.fdn1out_brn)

        self.fdn1outtm = QLabel(self.page1_main)
        self.fdn1outtm.setObjectName(u"fdn1outtm")
        sizePolicy2.setHeightForWidth(self.fdn1outtm.sizePolicy().hasHeightForWidth())
        self.fdn1outtm.setSizePolicy(sizePolicy2)
        self.fdn1outtm.setMinimumSize(QSize(100, 30))
        self.fdn1outtm.setFont(font)
        self.fdn1outtm.setAutoFillBackground(False)
        self.fdn1outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1outtm.setFrameShape(QFrame.Panel)
        self.fdn1outtm.setFrameShadow(QFrame.Sunken)
        self.fdn1outtm.setTextFormat(Qt.AutoText)
        self.fdn1outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.fdn1outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.fdn1out_brn_2 = QPushButton(self.page1_main)
        self.fdn1out_brn_2.setObjectName(u"fdn1out_brn_2")
        self.fdn1out_brn_2.setMinimumSize(QSize(0, 30))
        self.fdn1out_brn_2.setFont(font)

        self.horizontalLayout_13.addWidget(self.fdn1out_brn_2)

        self.fdn1outtm_2 = QLabel(self.page1_main)
        self.fdn1outtm_2.setObjectName(u"fdn1outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn1outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn1outtm_2.setSizePolicy(sizePolicy2)
        self.fdn1outtm_2.setMinimumSize(QSize(100, 30))
        self.fdn1outtm_2.setFont(font)
        self.fdn1outtm_2.setAutoFillBackground(False)
        self.fdn1outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1outtm_2.setFrameShape(QFrame.Panel)
        self.fdn1outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn1outtm_2.setTextFormat(Qt.AutoText)
        self.fdn1outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.fdn1outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 1, 1, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.fdn1out_brn_3 = QPushButton(self.page1_main)
        self.fdn1out_brn_3.setObjectName(u"fdn1out_brn_3")
        self.fdn1out_brn_3.setMinimumSize(QSize(0, 30))
        self.fdn1out_brn_3.setFont(font)

        self.horizontalLayout_25.addWidget(self.fdn1out_brn_3)

        self.fdn1outtm_3 = QLabel(self.page1_main)
        self.fdn1outtm_3.setObjectName(u"fdn1outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn1outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn1outtm_3.setSizePolicy(sizePolicy2)
        self.fdn1outtm_3.setMinimumSize(QSize(100, 30))
        self.fdn1outtm_3.setFont(font)
        self.fdn1outtm_3.setAutoFillBackground(False)
        self.fdn1outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn1outtm_3.setFrameShape(QFrame.Panel)
        self.fdn1outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn1outtm_3.setTextFormat(Qt.AutoText)
        self.fdn1outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.fdn1outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_25, 1, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.fdn2in_btn = QPushButton(self.page1_main)
        self.fdn2in_btn.setObjectName(u"fdn2in_btn")
        self.fdn2in_btn.setMinimumSize(QSize(0, 30))
        self.fdn2in_btn.setFont(font)

        self.horizontalLayout_3.addWidget(self.fdn2in_btn)

        self.fdn2intm = QLabel(self.page1_main)
        self.fdn2intm.setObjectName(u"fdn2intm")
        sizePolicy2.setHeightForWidth(self.fdn2intm.sizePolicy().hasHeightForWidth())
        self.fdn2intm.setSizePolicy(sizePolicy2)
        self.fdn2intm.setMinimumSize(QSize(100, 30))
        self.fdn2intm.setFont(font)
        self.fdn2intm.setAutoFillBackground(False)
        self.fdn2intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2intm.setFrameShape(QFrame.Panel)
        self.fdn2intm.setFrameShadow(QFrame.Sunken)
        self.fdn2intm.setTextFormat(Qt.AutoText)
        self.fdn2intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.fdn2intm)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.fdn2in_btn_2 = QPushButton(self.page1_main)
        self.fdn2in_btn_2.setObjectName(u"fdn2in_btn_2")
        self.fdn2in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn2in_btn_2.setFont(font)

        self.horizontalLayout_22.addWidget(self.fdn2in_btn_2)

        self.fdn2intm_2 = QLabel(self.page1_main)
        self.fdn2intm_2.setObjectName(u"fdn2intm_2")
        sizePolicy2.setHeightForWidth(self.fdn2intm_2.sizePolicy().hasHeightForWidth())
        self.fdn2intm_2.setSizePolicy(sizePolicy2)
        self.fdn2intm_2.setMinimumSize(QSize(100, 30))
        self.fdn2intm_2.setFont(font)
        self.fdn2intm_2.setAutoFillBackground(False)
        self.fdn2intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2intm_2.setFrameShape(QFrame.Panel)
        self.fdn2intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn2intm_2.setTextFormat(Qt.AutoText)
        self.fdn2intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.fdn2intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_22, 2, 1, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(5, 5, 5, 5)
        self.fdn2in_btn_3 = QPushButton(self.page1_main)
        self.fdn2in_btn_3.setObjectName(u"fdn2in_btn_3")
        self.fdn2in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn2in_btn_3.setFont(font)

        self.horizontalLayout_34.addWidget(self.fdn2in_btn_3)

        self.fdn2intm_3 = QLabel(self.page1_main)
        self.fdn2intm_3.setObjectName(u"fdn2intm_3")
        sizePolicy2.setHeightForWidth(self.fdn2intm_3.sizePolicy().hasHeightForWidth())
        self.fdn2intm_3.setSizePolicy(sizePolicy2)
        self.fdn2intm_3.setMinimumSize(QSize(100, 30))
        self.fdn2intm_3.setFont(font)
        self.fdn2intm_3.setAutoFillBackground(False)
        self.fdn2intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2intm_3.setFrameShape(QFrame.Panel)
        self.fdn2intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn2intm_3.setTextFormat(Qt.AutoText)
        self.fdn2intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.fdn2intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_34, 2, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.fdn2out_btn = QPushButton(self.page1_main)
        self.fdn2out_btn.setObjectName(u"fdn2out_btn")
        self.fdn2out_btn.setMinimumSize(QSize(0, 30))
        self.fdn2out_btn.setFont(font)

        self.horizontalLayout_4.addWidget(self.fdn2out_btn)

        self.fdn2outtm = QLabel(self.page1_main)
        self.fdn2outtm.setObjectName(u"fdn2outtm")
        sizePolicy2.setHeightForWidth(self.fdn2outtm.sizePolicy().hasHeightForWidth())
        self.fdn2outtm.setSizePolicy(sizePolicy2)
        self.fdn2outtm.setMinimumSize(QSize(0, 30))
        self.fdn2outtm.setFont(font)
        self.fdn2outtm.setAutoFillBackground(False)
        self.fdn2outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2outtm.setFrameShape(QFrame.Panel)
        self.fdn2outtm.setFrameShadow(QFrame.Sunken)
        self.fdn2outtm.setTextFormat(Qt.AutoText)
        self.fdn2outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.fdn2outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.fdn2out_btn_2 = QPushButton(self.page1_main)
        self.fdn2out_btn_2.setObjectName(u"fdn2out_btn_2")
        self.fdn2out_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn2out_btn_2.setFont(font)

        self.horizontalLayout_23.addWidget(self.fdn2out_btn_2)

        self.fdn2outtm_2 = QLabel(self.page1_main)
        self.fdn2outtm_2.setObjectName(u"fdn2outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn2outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn2outtm_2.setSizePolicy(sizePolicy2)
        self.fdn2outtm_2.setMinimumSize(QSize(0, 30))
        self.fdn2outtm_2.setFont(font)
        self.fdn2outtm_2.setAutoFillBackground(False)
        self.fdn2outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2outtm_2.setFrameShape(QFrame.Panel)
        self.fdn2outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn2outtm_2.setTextFormat(Qt.AutoText)
        self.fdn2outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.fdn2outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_23, 3, 1, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(5, 5, 5, 5)
        self.fdn2out_btn_3 = QPushButton(self.page1_main)
        self.fdn2out_btn_3.setObjectName(u"fdn2out_btn_3")
        self.fdn2out_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn2out_btn_3.setFont(font)

        self.horizontalLayout_35.addWidget(self.fdn2out_btn_3)

        self.fdn2outtm_3 = QLabel(self.page1_main)
        self.fdn2outtm_3.setObjectName(u"fdn2outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn2outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn2outtm_3.setSizePolicy(sizePolicy2)
        self.fdn2outtm_3.setMinimumSize(QSize(0, 30))
        self.fdn2outtm_3.setFont(font)
        self.fdn2outtm_3.setAutoFillBackground(False)
        self.fdn2outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn2outtm_3.setFrameShape(QFrame.Panel)
        self.fdn2outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn2outtm_3.setTextFormat(Qt.AutoText)
        self.fdn2outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.fdn2outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_35, 3, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.fdn3in_btn = QPushButton(self.page1_main)
        self.fdn3in_btn.setObjectName(u"fdn3in_btn")
        self.fdn3in_btn.setMinimumSize(QSize(0, 30))
        self.fdn3in_btn.setFont(font)

        self.horizontalLayout_5.addWidget(self.fdn3in_btn)

        self.fdn3intm = QLabel(self.page1_main)
        self.fdn3intm.setObjectName(u"fdn3intm")
        sizePolicy2.setHeightForWidth(self.fdn3intm.sizePolicy().hasHeightForWidth())
        self.fdn3intm.setSizePolicy(sizePolicy2)
        self.fdn3intm.setMinimumSize(QSize(100, 30))
        self.fdn3intm.setFont(font)
        self.fdn3intm.setAutoFillBackground(False)
        self.fdn3intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3intm.setFrameShape(QFrame.Panel)
        self.fdn3intm.setFrameShadow(QFrame.Sunken)
        self.fdn3intm.setTextFormat(Qt.AutoText)
        self.fdn3intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.fdn3intm)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.fdn3in_btn_2 = QPushButton(self.page1_main)
        self.fdn3in_btn_2.setObjectName(u"fdn3in_btn_2")
        self.fdn3in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn3in_btn_2.setFont(font)

        self.horizontalLayout_15.addWidget(self.fdn3in_btn_2)

        self.fdn3intm_2 = QLabel(self.page1_main)
        self.fdn3intm_2.setObjectName(u"fdn3intm_2")
        sizePolicy2.setHeightForWidth(self.fdn3intm_2.sizePolicy().hasHeightForWidth())
        self.fdn3intm_2.setSizePolicy(sizePolicy2)
        self.fdn3intm_2.setMinimumSize(QSize(100, 30))
        self.fdn3intm_2.setFont(font)
        self.fdn3intm_2.setAutoFillBackground(False)
        self.fdn3intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3intm_2.setFrameShape(QFrame.Panel)
        self.fdn3intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn3intm_2.setTextFormat(Qt.AutoText)
        self.fdn3intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.fdn3intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 4, 1, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.fdn3in_btn_3 = QPushButton(self.page1_main)
        self.fdn3in_btn_3.setObjectName(u"fdn3in_btn_3")
        self.fdn3in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn3in_btn_3.setFont(font)

        self.horizontalLayout_27.addWidget(self.fdn3in_btn_3)

        self.fdn3intm_3 = QLabel(self.page1_main)
        self.fdn3intm_3.setObjectName(u"fdn3intm_3")
        sizePolicy2.setHeightForWidth(self.fdn3intm_3.sizePolicy().hasHeightForWidth())
        self.fdn3intm_3.setSizePolicy(sizePolicy2)
        self.fdn3intm_3.setMinimumSize(QSize(100, 30))
        self.fdn3intm_3.setFont(font)
        self.fdn3intm_3.setAutoFillBackground(False)
        self.fdn3intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3intm_3.setFrameShape(QFrame.Panel)
        self.fdn3intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn3intm_3.setTextFormat(Qt.AutoText)
        self.fdn3intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.fdn3intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_27, 4, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.fdn3out_btn = QPushButton(self.page1_main)
        self.fdn3out_btn.setObjectName(u"fdn3out_btn")
        self.fdn3out_btn.setMinimumSize(QSize(0, 30))
        self.fdn3out_btn.setFont(font)

        self.horizontalLayout_6.addWidget(self.fdn3out_btn)

        self.fdn3outtm = QLabel(self.page1_main)
        self.fdn3outtm.setObjectName(u"fdn3outtm")
        sizePolicy2.setHeightForWidth(self.fdn3outtm.sizePolicy().hasHeightForWidth())
        self.fdn3outtm.setSizePolicy(sizePolicy2)
        self.fdn3outtm.setMinimumSize(QSize(100, 30))
        self.fdn3outtm.setFont(font)
        self.fdn3outtm.setAutoFillBackground(False)
        self.fdn3outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3outtm.setFrameShape(QFrame.Panel)
        self.fdn3outtm.setFrameShadow(QFrame.Sunken)
        self.fdn3outtm.setTextFormat(Qt.AutoText)
        self.fdn3outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.fdn3outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.fdn3out_btn_2 = QPushButton(self.page1_main)
        self.fdn3out_btn_2.setObjectName(u"fdn3out_btn_2")
        self.fdn3out_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn3out_btn_2.setFont(font)

        self.horizontalLayout_14.addWidget(self.fdn3out_btn_2)

        self.fdn3outtm_2 = QLabel(self.page1_main)
        self.fdn3outtm_2.setObjectName(u"fdn3outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn3outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn3outtm_2.setSizePolicy(sizePolicy2)
        self.fdn3outtm_2.setMinimumSize(QSize(100, 30))
        self.fdn3outtm_2.setFont(font)
        self.fdn3outtm_2.setAutoFillBackground(False)
        self.fdn3outtm_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fdn3outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3outtm_2.setFrameShape(QFrame.Panel)
        self.fdn3outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn3outtm_2.setTextFormat(Qt.AutoText)
        self.fdn3outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.fdn3outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 5, 1, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.fdn3out_btn_3 = QPushButton(self.page1_main)
        self.fdn3out_btn_3.setObjectName(u"fdn3out_btn_3")
        self.fdn3out_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn3out_btn_3.setFont(font)

        self.horizontalLayout_26.addWidget(self.fdn3out_btn_3)

        self.fdn3outtm_3 = QLabel(self.page1_main)
        self.fdn3outtm_3.setObjectName(u"fdn3outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn3outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn3outtm_3.setSizePolicy(sizePolicy2)
        self.fdn3outtm_3.setMinimumSize(QSize(100, 30))
        self.fdn3outtm_3.setFont(font)
        self.fdn3outtm_3.setAutoFillBackground(False)
        self.fdn3outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn3outtm_3.setFrameShape(QFrame.Panel)
        self.fdn3outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn3outtm_3.setTextFormat(Qt.AutoText)
        self.fdn3outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.fdn3outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_26, 5, 2, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.fdn4in_btn = QPushButton(self.page1_main)
        self.fdn4in_btn.setObjectName(u"fdn4in_btn")
        self.fdn4in_btn.setMinimumSize(QSize(0, 30))
        self.fdn4in_btn.setFont(font)

        self.horizontalLayout_7.addWidget(self.fdn4in_btn)

        self.fdn4intm = QLabel(self.page1_main)
        self.fdn4intm.setObjectName(u"fdn4intm")
        sizePolicy2.setHeightForWidth(self.fdn4intm.sizePolicy().hasHeightForWidth())
        self.fdn4intm.setSizePolicy(sizePolicy2)
        self.fdn4intm.setMinimumSize(QSize(100, 30))
        self.fdn4intm.setFont(font)
        self.fdn4intm.setAutoFillBackground(False)
        self.fdn4intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4intm.setFrameShape(QFrame.Panel)
        self.fdn4intm.setFrameShadow(QFrame.Sunken)
        self.fdn4intm.setTextFormat(Qt.AutoText)
        self.fdn4intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.fdn4intm)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.fdn4in_btn_2 = QPushButton(self.page1_main)
        self.fdn4in_btn_2.setObjectName(u"fdn4in_btn_2")
        self.fdn4in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn4in_btn_2.setFont(font)

        self.horizontalLayout_21.addWidget(self.fdn4in_btn_2)

        self.fdn4intm_2 = QLabel(self.page1_main)
        self.fdn4intm_2.setObjectName(u"fdn4intm_2")
        sizePolicy2.setHeightForWidth(self.fdn4intm_2.sizePolicy().hasHeightForWidth())
        self.fdn4intm_2.setSizePolicy(sizePolicy2)
        self.fdn4intm_2.setMinimumSize(QSize(100, 30))
        self.fdn4intm_2.setFont(font)
        self.fdn4intm_2.setAutoFillBackground(False)
        self.fdn4intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4intm_2.setFrameShape(QFrame.Panel)
        self.fdn4intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn4intm_2.setTextFormat(Qt.AutoText)
        self.fdn4intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.fdn4intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_21, 6, 1, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.fdn4in_btn_3 = QPushButton(self.page1_main)
        self.fdn4in_btn_3.setObjectName(u"fdn4in_btn_3")
        self.fdn4in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn4in_btn_3.setFont(font)

        self.horizontalLayout_33.addWidget(self.fdn4in_btn_3)

        self.fdn4intm_3 = QLabel(self.page1_main)
        self.fdn4intm_3.setObjectName(u"fdn4intm_3")
        sizePolicy2.setHeightForWidth(self.fdn4intm_3.sizePolicy().hasHeightForWidth())
        self.fdn4intm_3.setSizePolicy(sizePolicy2)
        self.fdn4intm_3.setMinimumSize(QSize(100, 30))
        self.fdn4intm_3.setFont(font)
        self.fdn4intm_3.setAutoFillBackground(False)
        self.fdn4intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4intm_3.setFrameShape(QFrame.Panel)
        self.fdn4intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn4intm_3.setTextFormat(Qt.AutoText)
        self.fdn4intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.fdn4intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_33, 6, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.fdn4out_btn = QPushButton(self.page1_main)
        self.fdn4out_btn.setObjectName(u"fdn4out_btn")
        self.fdn4out_btn.setMinimumSize(QSize(0, 30))
        self.fdn4out_btn.setFont(font)

        self.horizontalLayout_8.addWidget(self.fdn4out_btn)

        self.fdn4outtm = QLabel(self.page1_main)
        self.fdn4outtm.setObjectName(u"fdn4outtm")
        sizePolicy2.setHeightForWidth(self.fdn4outtm.sizePolicy().hasHeightForWidth())
        self.fdn4outtm.setSizePolicy(sizePolicy2)
        self.fdn4outtm.setMinimumSize(QSize(100, 30))
        self.fdn4outtm.setFont(font)
        self.fdn4outtm.setAutoFillBackground(False)
        self.fdn4outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4outtm.setFrameShape(QFrame.Panel)
        self.fdn4outtm.setFrameShadow(QFrame.Sunken)
        self.fdn4outtm.setTextFormat(Qt.AutoText)
        self.fdn4outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.fdn4outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.fdn4out_btn_2 = QPushButton(self.page1_main)
        self.fdn4out_btn_2.setObjectName(u"fdn4out_btn_2")
        self.fdn4out_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn4out_btn_2.setFont(font)

        self.horizontalLayout_18.addWidget(self.fdn4out_btn_2)

        self.fdn4outtm_2 = QLabel(self.page1_main)
        self.fdn4outtm_2.setObjectName(u"fdn4outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn4outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn4outtm_2.setSizePolicy(sizePolicy2)
        self.fdn4outtm_2.setMinimumSize(QSize(100, 30))
        self.fdn4outtm_2.setFont(font)
        self.fdn4outtm_2.setAutoFillBackground(False)
        self.fdn4outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4outtm_2.setFrameShape(QFrame.Panel)
        self.fdn4outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn4outtm_2.setTextFormat(Qt.AutoText)
        self.fdn4outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.fdn4outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_18, 7, 1, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.fdn4out_btn_3 = QPushButton(self.page1_main)
        self.fdn4out_btn_3.setObjectName(u"fdn4out_btn_3")
        self.fdn4out_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn4out_btn_3.setFont(font)

        self.horizontalLayout_30.addWidget(self.fdn4out_btn_3)

        self.fdn4outtm_3 = QLabel(self.page1_main)
        self.fdn4outtm_3.setObjectName(u"fdn4outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn4outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn4outtm_3.setSizePolicy(sizePolicy2)
        self.fdn4outtm_3.setMinimumSize(QSize(100, 30))
        self.fdn4outtm_3.setFont(font)
        self.fdn4outtm_3.setAutoFillBackground(False)
        self.fdn4outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn4outtm_3.setFrameShape(QFrame.Panel)
        self.fdn4outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn4outtm_3.setTextFormat(Qt.AutoText)
        self.fdn4outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.fdn4outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_30, 7, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.fdn5in_btn = QPushButton(self.page1_main)
        self.fdn5in_btn.setObjectName(u"fdn5in_btn")
        self.fdn5in_btn.setMinimumSize(QSize(0, 30))
        self.fdn5in_btn.setFont(font)

        self.horizontalLayout_9.addWidget(self.fdn5in_btn)

        self.fdn5intm = QLabel(self.page1_main)
        self.fdn5intm.setObjectName(u"fdn5intm")
        sizePolicy2.setHeightForWidth(self.fdn5intm.sizePolicy().hasHeightForWidth())
        self.fdn5intm.setSizePolicy(sizePolicy2)
        self.fdn5intm.setMinimumSize(QSize(100, 30))
        self.fdn5intm.setFont(font)
        self.fdn5intm.setAutoFillBackground(False)
        self.fdn5intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5intm.setFrameShape(QFrame.Panel)
        self.fdn5intm.setFrameShadow(QFrame.Sunken)
        self.fdn5intm.setTextFormat(Qt.AutoText)
        self.fdn5intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.fdn5intm)


        self.gridLayout_2.addLayout(self.horizontalLayout_9, 8, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.fdn5in_btn_2 = QPushButton(self.page1_main)
        self.fdn5in_btn_2.setObjectName(u"fdn5in_btn_2")
        self.fdn5in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn5in_btn_2.setFont(font)

        self.horizontalLayout_20.addWidget(self.fdn5in_btn_2)

        self.fdn5intm_2 = QLabel(self.page1_main)
        self.fdn5intm_2.setObjectName(u"fdn5intm_2")
        sizePolicy2.setHeightForWidth(self.fdn5intm_2.sizePolicy().hasHeightForWidth())
        self.fdn5intm_2.setSizePolicy(sizePolicy2)
        self.fdn5intm_2.setMinimumSize(QSize(100, 30))
        self.fdn5intm_2.setFont(font)
        self.fdn5intm_2.setAutoFillBackground(False)
        self.fdn5intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5intm_2.setFrameShape(QFrame.Panel)
        self.fdn5intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn5intm_2.setTextFormat(Qt.AutoText)
        self.fdn5intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.fdn5intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_20, 8, 1, 1, 1)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.fdn5in_btn_3 = QPushButton(self.page1_main)
        self.fdn5in_btn_3.setObjectName(u"fdn5in_btn_3")
        self.fdn5in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn5in_btn_3.setFont(font)

        self.horizontalLayout_32.addWidget(self.fdn5in_btn_3)

        self.fdn5intm_3 = QLabel(self.page1_main)
        self.fdn5intm_3.setObjectName(u"fdn5intm_3")
        sizePolicy2.setHeightForWidth(self.fdn5intm_3.sizePolicy().hasHeightForWidth())
        self.fdn5intm_3.setSizePolicy(sizePolicy2)
        self.fdn5intm_3.setMinimumSize(QSize(100, 30))
        self.fdn5intm_3.setFont(font)
        self.fdn5intm_3.setAutoFillBackground(False)
        self.fdn5intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5intm_3.setFrameShape(QFrame.Panel)
        self.fdn5intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn5intm_3.setTextFormat(Qt.AutoText)
        self.fdn5intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.fdn5intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_32, 8, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.fdn5out_btn = QPushButton(self.page1_main)
        self.fdn5out_btn.setObjectName(u"fdn5out_btn")
        self.fdn5out_btn.setMinimumSize(QSize(0, 30))
        self.fdn5out_btn.setFont(font)

        self.horizontalLayout_10.addWidget(self.fdn5out_btn)

        self.fdn5outtm = QLabel(self.page1_main)
        self.fdn5outtm.setObjectName(u"fdn5outtm")
        sizePolicy2.setHeightForWidth(self.fdn5outtm.sizePolicy().hasHeightForWidth())
        self.fdn5outtm.setSizePolicy(sizePolicy2)
        self.fdn5outtm.setMinimumSize(QSize(100, 30))
        self.fdn5outtm.setFont(font)
        self.fdn5outtm.setAutoFillBackground(False)
        self.fdn5outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5outtm.setFrameShape(QFrame.Panel)
        self.fdn5outtm.setFrameShadow(QFrame.Sunken)
        self.fdn5outtm.setTextFormat(Qt.AutoText)
        self.fdn5outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.fdn5outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 9, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.fdn5out_btn_2 = QPushButton(self.page1_main)
        self.fdn5out_btn_2.setObjectName(u"fdn5out_btn_2")
        self.fdn5out_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn5out_btn_2.setFont(font)

        self.horizontalLayout_24.addWidget(self.fdn5out_btn_2)

        self.fdn5outtm_2 = QLabel(self.page1_main)
        self.fdn5outtm_2.setObjectName(u"fdn5outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn5outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn5outtm_2.setSizePolicy(sizePolicy2)
        self.fdn5outtm_2.setMinimumSize(QSize(100, 30))
        self.fdn5outtm_2.setFont(font)
        self.fdn5outtm_2.setAutoFillBackground(False)
        self.fdn5outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5outtm_2.setFrameShape(QFrame.Panel)
        self.fdn5outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn5outtm_2.setTextFormat(Qt.AutoText)
        self.fdn5outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.fdn5outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_24, 9, 1, 1, 1)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(5, 5, 5, 5)
        self.fdn5out_btn_3 = QPushButton(self.page1_main)
        self.fdn5out_btn_3.setObjectName(u"fdn5out_btn_3")
        self.fdn5out_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn5out_btn_3.setFont(font)

        self.horizontalLayout_36.addWidget(self.fdn5out_btn_3)

        self.fdn5outtm_3 = QLabel(self.page1_main)
        self.fdn5outtm_3.setObjectName(u"fdn5outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn5outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn5outtm_3.setSizePolicy(sizePolicy2)
        self.fdn5outtm_3.setMinimumSize(QSize(100, 30))
        self.fdn5outtm_3.setFont(font)
        self.fdn5outtm_3.setAutoFillBackground(False)
        self.fdn5outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn5outtm_3.setFrameShape(QFrame.Panel)
        self.fdn5outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn5outtm_3.setTextFormat(Qt.AutoText)
        self.fdn5outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.fdn5outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_36, 9, 2, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.fdn6in_btn = QPushButton(self.page1_main)
        self.fdn6in_btn.setObjectName(u"fdn6in_btn")
        self.fdn6in_btn.setMinimumSize(QSize(0, 30))
        self.fdn6in_btn.setFont(font)

        self.horizontalLayout_11.addWidget(self.fdn6in_btn)

        self.fdn6intm = QLabel(self.page1_main)
        self.fdn6intm.setObjectName(u"fdn6intm")
        sizePolicy2.setHeightForWidth(self.fdn6intm.sizePolicy().hasHeightForWidth())
        self.fdn6intm.setSizePolicy(sizePolicy2)
        self.fdn6intm.setMinimumSize(QSize(100, 30))
        self.fdn6intm.setFont(font)
        self.fdn6intm.setAutoFillBackground(False)
        self.fdn6intm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6intm.setFrameShape(QFrame.Panel)
        self.fdn6intm.setFrameShadow(QFrame.Sunken)
        self.fdn6intm.setTextFormat(Qt.AutoText)
        self.fdn6intm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.fdn6intm)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 10, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.fdn6in_btn_2 = QPushButton(self.page1_main)
        self.fdn6in_btn_2.setObjectName(u"fdn6in_btn_2")
        self.fdn6in_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn6in_btn_2.setFont(font)

        self.horizontalLayout_16.addWidget(self.fdn6in_btn_2)

        self.fdn6intm_2 = QLabel(self.page1_main)
        self.fdn6intm_2.setObjectName(u"fdn6intm_2")
        sizePolicy2.setHeightForWidth(self.fdn6intm_2.sizePolicy().hasHeightForWidth())
        self.fdn6intm_2.setSizePolicy(sizePolicy2)
        self.fdn6intm_2.setMinimumSize(QSize(100, 30))
        self.fdn6intm_2.setFont(font)
        self.fdn6intm_2.setAutoFillBackground(False)
        self.fdn6intm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6intm_2.setFrameShape(QFrame.Panel)
        self.fdn6intm_2.setFrameShadow(QFrame.Sunken)
        self.fdn6intm_2.setTextFormat(Qt.AutoText)
        self.fdn6intm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.fdn6intm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 10, 1, 1, 1)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.fdn6in_btn_3 = QPushButton(self.page1_main)
        self.fdn6in_btn_3.setObjectName(u"fdn6in_btn_3")
        self.fdn6in_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn6in_btn_3.setFont(font)

        self.horizontalLayout_28.addWidget(self.fdn6in_btn_3)

        self.fdn6intm_3 = QLabel(self.page1_main)
        self.fdn6intm_3.setObjectName(u"fdn6intm_3")
        sizePolicy2.setHeightForWidth(self.fdn6intm_3.sizePolicy().hasHeightForWidth())
        self.fdn6intm_3.setSizePolicy(sizePolicy2)
        self.fdn6intm_3.setMinimumSize(QSize(100, 30))
        self.fdn6intm_3.setFont(font)
        self.fdn6intm_3.setAutoFillBackground(False)
        self.fdn6intm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6intm_3.setFrameShape(QFrame.Panel)
        self.fdn6intm_3.setFrameShadow(QFrame.Sunken)
        self.fdn6intm_3.setTextFormat(Qt.AutoText)
        self.fdn6intm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.fdn6intm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_28, 10, 2, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.fdn6out_btn = QPushButton(self.page1_main)
        self.fdn6out_btn.setObjectName(u"fdn6out_btn")
        self.fdn6out_btn.setMinimumSize(QSize(0, 30))
        self.fdn6out_btn.setFont(font)

        self.horizontalLayout_12.addWidget(self.fdn6out_btn)

        self.fdn6outtm = QLabel(self.page1_main)
        self.fdn6outtm.setObjectName(u"fdn6outtm")
        sizePolicy2.setHeightForWidth(self.fdn6outtm.sizePolicy().hasHeightForWidth())
        self.fdn6outtm.setSizePolicy(sizePolicy2)
        self.fdn6outtm.setMinimumSize(QSize(100, 30))
        self.fdn6outtm.setFont(font)
        self.fdn6outtm.setAutoFillBackground(False)
        self.fdn6outtm.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6outtm.setFrameShape(QFrame.Panel)
        self.fdn6outtm.setFrameShadow(QFrame.Sunken)
        self.fdn6outtm.setTextFormat(Qt.AutoText)
        self.fdn6outtm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.fdn6outtm)


        self.gridLayout_2.addLayout(self.horizontalLayout_12, 11, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.fdn6out_btn_2 = QPushButton(self.page1_main)
        self.fdn6out_btn_2.setObjectName(u"fdn6out_btn_2")
        self.fdn6out_btn_2.setMinimumSize(QSize(0, 30))
        self.fdn6out_btn_2.setFont(font)

        self.horizontalLayout_17.addWidget(self.fdn6out_btn_2)

        self.fdn6outtm_2 = QLabel(self.page1_main)
        self.fdn6outtm_2.setObjectName(u"fdn6outtm_2")
        sizePolicy2.setHeightForWidth(self.fdn6outtm_2.sizePolicy().hasHeightForWidth())
        self.fdn6outtm_2.setSizePolicy(sizePolicy2)
        self.fdn6outtm_2.setMinimumSize(QSize(100, 30))
        self.fdn6outtm_2.setFont(font)
        self.fdn6outtm_2.setAutoFillBackground(False)
        self.fdn6outtm_2.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6outtm_2.setFrameShape(QFrame.Panel)
        self.fdn6outtm_2.setFrameShadow(QFrame.Sunken)
        self.fdn6outtm_2.setTextFormat(Qt.AutoText)
        self.fdn6outtm_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.fdn6outtm_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_17, 11, 1, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.fdn6out_btn_3 = QPushButton(self.page1_main)
        self.fdn6out_btn_3.setObjectName(u"fdn6out_btn_3")
        self.fdn6out_btn_3.setMinimumSize(QSize(0, 30))
        self.fdn6out_btn_3.setFont(font)

        self.horizontalLayout_29.addWidget(self.fdn6out_btn_3)

        self.fdn6outtm_3 = QLabel(self.page1_main)
        self.fdn6outtm_3.setObjectName(u"fdn6outtm_3")
        sizePolicy2.setHeightForWidth(self.fdn6outtm_3.sizePolicy().hasHeightForWidth())
        self.fdn6outtm_3.setSizePolicy(sizePolicy2)
        self.fdn6outtm_3.setMinimumSize(QSize(100, 30))
        self.fdn6outtm_3.setFont(font)
        self.fdn6outtm_3.setAutoFillBackground(False)
        self.fdn6outtm_3.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.fdn6outtm_3.setFrameShape(QFrame.Panel)
        self.fdn6outtm_3.setFrameShadow(QFrame.Sunken)
        self.fdn6outtm_3.setTextFormat(Qt.AutoText)
        self.fdn6outtm_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.fdn6outtm_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_29, 11, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.page1_main)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.fdn1in_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a\u680f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6\u76d1\u63a7", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6\u67e5\u8be2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6\u66f2\u7ebf", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(tooltip)
        self.fdn1in_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.fdn1in_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.fdn1in_btn.setText(QCoreApplication.translate("MainWindow", u"1#\u51b7\u4e95\u8fdb\u6db2", None))
#if QT_CONFIG(shortcut)
        self.fdn1in_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.fdn1intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn1in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn1intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn1in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn1intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn1out_brn.setText(QCoreApplication.translate("MainWindow", u"1#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn1outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn1out_brn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn1outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn1out_brn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn1outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2in_btn.setText(QCoreApplication.translate("MainWindow", u"2#\u51b7\u4e95\u8fdb\u6db2", None))
        self.fdn2intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn2intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn2intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2out_btn.setText(QCoreApplication.translate("MainWindow", u"2#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn2outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2out_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn2outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn2out_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn2outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn3in_btn.setText(QCoreApplication.translate("MainWindow", u"3#\u51b7\u4e95\u8fdb\u6db2", None))
        self.fdn3intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn3in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn3intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn3in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn3intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn3out_btn.setText(QCoreApplication.translate("MainWindow", u"3#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn3outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn3out_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn3outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
#if QT_CONFIG(tooltip)
        self.fdn3out_btn_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fdn3out_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn3outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4in_btn.setText(QCoreApplication.translate("MainWindow", u"4#\u51b7\u4e95\u8fdb\u6db2", None))
        self.fdn4intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn4intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn4intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4out_btn.setText(QCoreApplication.translate("MainWindow", u"4#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn4outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4out_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn4outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn4out_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn4outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5in_btn.setText(QCoreApplication.translate("MainWindow", u"5#\u51b7\u4e95\u8fdb\u6db2", None))
        self.fdn5intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn5intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn5intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5out_btn.setText(QCoreApplication.translate("MainWindow", u"5#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn5outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5out_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn5outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn5out_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn5outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6in_btn.setText(QCoreApplication.translate("MainWindow", u"6#\u51b7\u4e95\u8fdb\u6db2", None))
        self.fdn6intm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6in_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn6intm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6in_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn6intm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6out_btn.setText(QCoreApplication.translate("MainWindow", u"6#\u51b7\u4e95\u56de\u6c14", None))
        self.fdn6outtm.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6out_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn6outtm_2.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.fdn6out_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u5907\u7528", None))
        self.fdn6outtm_3.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
    # retranslateUi


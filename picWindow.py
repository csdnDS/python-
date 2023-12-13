# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QSizePolicy, QVBoxLayout,
                               QWidget)


class PicWindow(QMainWindow):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label")
        self.horizontalLayout.addWidget(self.label_1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label_1.setPixmap(QPixmap("barChart.png"))
        self.label_2.setPixmap(QPixmap("fanChart.png"))
        self.label_3.setPixmap(QPixmap("wordcloud.png"))
        self.label_4.setPixmap(QPixmap("polyLine.png"))
        self.label_1.setScaledContents(True)
        self.label_2.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_4.setScaledContents(True)
        self.label_1.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))
        self.label_2.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))
        self.label_3.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))
        self.label_4.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        QMetaObject.connectSlotsByName(MainWindow)

class MyPicWindow(QMainWindow):
    def __init__(self):
        super(MyPicWindow, self).__init__()
        self.ui = PicWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])  # 创建应用程序实例
    MainWindow = QMainWindow()  # 创建主窗口实例
    ui = PicWindow()  # 创建UI实例
    ui.setupUi(MainWindow)  # 设置UI

    MainWindow.show()  # 显示主窗口
    sys.exit(app.exec_())  # 运行应用程序事件循环

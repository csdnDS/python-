# -*- coding=utf-8 -*-
import os
import sys

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QLabel

from dataCrawl import WeiboCommentsCrawler
from generateBarChart import BarChartGenerator
from generateFanChart import fanChartGenerator
from generatePolylineChart import polylineChartGenerator
from generateWordCloudChart import wordCloudGenerator
from picWindow import MyPicWindow

input_text = None  # 定义接收传入url的变量


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("CentralWidget")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName("Label")
        self.label.setGeometry(QRect(10, 160, 781, 51))
        self.lineEdit = QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("LineEdit")
        self.lineEdit.setGeometry(QRect(200, 250, 390, 30))
        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setObjectName("PushButton")
        self.pushButton.setGeometry(QRect(630, 250, 102, 32))
        self.resultLabel = QLabel(self.centralWidget)
        self.resultLabel.setGeometry(QRect(200, 300, 400, 100))
        self.resultLabel.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "请输入微博评论链接", None))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""QLabel{
                                        font: bold 24px \"Microsoft YaHei UI\";}""")
        self.lineEdit.setStyleSheet("""QLineEdit{
                                            border-radius:5px;}""")
        self.pushButton.setStyleSheet("""QPushButton{
                                            border-radius:5px;
                                            background-color:white;
                                            font:bold;}
                                        QPushButton:pressed{
                                            background-color: #f0f0f0;}""")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "生成", None))
        QMetaObject.connectSlotsByName(MainWindow)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_url)
        self.ui.pushButton.clicked.connect(self.crawl_data_and_generate_chart)

    def get_url(self):
        global input_text
        input_text = self.ui.lineEdit.text()

    def crawl_data_and_generate_chart(self):
        self.ui.resultLabel.setText("正在生成中，请稍候...")
        self.ui.resultLabel.setStyleSheet("QLabel{font: bold 16px \"Microsoft YaHei UI\";}")
        self.repaint()
        crawler = WeiboCommentsCrawler(start_url=input_text)
        crawler.crawl_weibo_comments()
        wordChart = wordCloudGenerator("weibocomments.csv")
        wordChart.generate_word_cloud_chart()
        barChart = BarChartGenerator("weibocomments.csv")
        barChart.generate_bar_chart()
        polylineChart = polylineChartGenerator("weibocomments.csv")
        polylineChart.generate_poly_line_chart()
        fanChart = fanChartGenerator("weibocomments.csv")
        fanChart.generate_fan_chart()
        if self.check_image('fanChart.png'):
            self.ui.resultLabel.setText("生成成功！")
            window = MyPicWindow()
            window.show()

    def check_image(self, image_path):
        return os.path.exists(image_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedLayout
from p_MenuBar.m_MenuBar import c_MenuBar
from p_Main import *

class c_MainWindow(QMainWindow):
    """Mainwindow of the Application"""
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 250, 1000, 640)
        self.setWindowTitle('타자연습')

        self.stackedlayout = QStackedLayout()
        self.setLayout(self.stackedlayout)

        self.menuBar = c_MenuBar()
        self.setMenuBar(self.menuBar)

        self.centerframe = m_CenterFrame.c_CenterFrame(self)

        self.stackedlayout.addWidget(self.centerframe)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = c_MainWindow()
    sys.exit(app.exec_())
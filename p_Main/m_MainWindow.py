import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedLayout

from p_Main.m_CenterFrame import c_CenterFrame as CenterFrame
from p_MenuBar.m_MenuBar import c_MenuBar as MenuBar
from p_AcidRain.m_AcidRainFrame import c_AcidRainFrame  as AcidRainFrame

class c_MainWindow(QMainWindow):
    """Mainwindow of the Application"""
    stackedlayout = QStackedLayout()
    centerframe = None
    acidrainframe = None

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(400, 250, 1000, 640)
        self.setMinimumSize(1000, 640)
        self.setWindowTitle('타자연습')

        self.setLayout(c_MainWindow.stackedlayout)


        self.menuBar = MenuBar()
        self.setMenuBar(self.menuBar)

        c_MainWindow.centerframe = CenterFrame(self)
        c_MainWindow.acidrainframe = AcidRainFrame(self)

        self.setCentralWidget(self.acidrainframe)

        c_MainWindow.stackedlayout.addWidget(c_MainWindow.centerframe)
        c_MainWindow.stackedlayout.addWidget(c_MainWindow.acidrainframe)

        self.show()


    def changeLayout(self, index):
        self.stackedlayout.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = c_MainWindow()
    sys.exit(app.exec_())
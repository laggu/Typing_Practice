from PyQt5.QtWidgets import QFrame, QStackedLayout
from . import centralize
from p_Main.m_MenuFrame import c_MenuFrame

class c_CenterFrame(QFrame):
    """The frame at the center of the MainWindow"""
    def __init__(self, mainframe):
        super(c_CenterFrame, self).__init__(mainframe)
        self.mainframe = mainframe

        self.initUI()

    def initUI(self):
        self.stackedlayout = QStackedLayout()
        self.setLayout(self.stackedlayout)

        self.stackedlayout.addWidget(c_MenuFrame())

        self.setFrameStyle(6)
        self.resize(600,400)
        centralize(self)
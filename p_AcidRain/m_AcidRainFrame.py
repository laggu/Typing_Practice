from PyQt5.QtWidgets import QFrame, QVBoxLayout
from p_AcidRain import *

class c_AcidRainFrame(QFrame):
    level = 1
    score = 0

    def __init__(self, mainwindow):
        super(c_AcidRainFrame, self).__init__(mainwindow)
        self.mainframe = mainwindow

        self.initUI()

    def initUI(self):
        self.resize(self.mainframe.width(), self.mainframe.height()-30)
        self.move(0,25)

        self.setFrameStyle(6)
        vboxlayout = QVBoxLayout()

        self.gameframe = m_GameFrame.c_GameFrame(self)
        self.typingframe = m_TypingFrame.c_TypingFrame(self)

        vboxlayout.addWidget(self.gameframe)
        vboxlayout.addWidget(self.typingframe)
        self.setLayout(vboxlayout)
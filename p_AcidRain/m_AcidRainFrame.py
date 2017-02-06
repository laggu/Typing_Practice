from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLineEdit
from p_AcidRain import *

class c_AcidRainFrame(QFrame):
    level = 1

    def __init__(self, mainwindow):
        super(c_AcidRainFrame, self).__init__(mainwindow)
        self.mainframe = mainwindow

        self.initUI()

    def initUI(self):
        self.resize(self.mainframe.width(), self.mainframe.height()-30)
        self.move(0,25)

        self.setFrameStyle(6)
        vboxlayout = QVBoxLayout()

        gameframe = m_GameFrame.c_GameFrame(self)
        typingframe = m_TypingFrame.c_TypingFrame()

        vboxlayout.addWidget(gameframe)
        vboxlayout.addWidget(typingframe)
        self.setLayout(vboxlayout)
from PyQt5.QtWidgets import QFrame
from .m_Rain import c_Rain as Rain


class c_GameFrame(QFrame):
    """The frame where the words will be droped"""
    raindrop = []
    def __init__(self, arFrame):
        super(c_GameFrame, self).__init__(arFrame)
        self.arframe = arFrame

        self.initUI()

    def initUI(self):
        self.setFrameStyle(1)

        self.setMinimumWidth(self.arframe.height())
        self.setMinimumHeight(self.arframe.height())

        self.raindrop.append(Rain('rk', self))

from PyQt5.QtWidgets import QFrame, QGridLayout, QLineEdit

class c_TypingFrame(QFrame):
    """The frame where the words will be droped"""

    def __init__(self):
        super(c_TypingFrame, self).__init__()

        self.initUI()

    def initUI(self):
        gridlayout = QGridLayout()
        self.lineedit = QLineEdit()
        self.lineedit.setMaximumWidth(150)

        gridlayout.addWidget(self.lineedit, 0, 1)
        self.setLayout(gridlayout)
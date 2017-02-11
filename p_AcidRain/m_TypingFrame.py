from PyQt5.QtWidgets import QFrame, QGridLayout, QLineEdit, QLabel, QPushButton

class c_TypingFrame(QFrame):
    """The frame where the words will be droped"""

    def __init__(self, arframe):
        super(c_TypingFrame, self).__init__(arframe)
        self.arframe = arframe

        self.initUI()

    def initUI(self):
        self.gridlayout = QGridLayout()

        self.explanation = QPushButton('시작')
        self.explanation.setMaximumSize(50, 20)
        self.explanation.clicked.connect(self.arframe.gameframe.start)

        self.lineedit = QLineEdit()
        self.lineedit.setMaximumWidth(150)

        self.scorelabel = QLabel('                                                 점수 : 0')

        self.gridlayout.addWidget(self.explanation, 0, 0)
        self.gridlayout.addWidget(None,0,1)
        self.gridlayout.addWidget(self.lineedit, 0, 2)
        self.gridlayout.addWidget(self.scorelabel, 0, 3)

        self.setLayout(self.gridlayout)
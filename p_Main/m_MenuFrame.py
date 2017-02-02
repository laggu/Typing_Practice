from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, qApp

class c_MenuFrame(QFrame):

    def __init__(self):
        super(c_MenuFrame, self).__init__()

        self.initUI()

    def initUI(self):
        self.vboxlayout = QVBoxLayout()

        btn_LP = QPushButton("짧은글연습")
        self.vboxlayout.addWidget(btn_LP)

        btn_PP = QPushButton('긴글연습')
        self.vboxlayout.addWidget(btn_PP)

        btn_AR = QPushButton('산성비')
        self.vboxlayout.addWidget(btn_AR)

        btn_Record = QPushButton('기록')
        self.vboxlayout.addWidget(btn_Record)

        btn_Quit = QPushButton('종료 [Ctrl+Q]')
        btn_Quit.clicked.connect(qApp.quit)
        self.vboxlayout.addWidget(btn_Quit)

        self.setLayout(self.vboxlayout)


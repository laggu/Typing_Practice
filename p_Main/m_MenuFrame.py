from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, qApp



class c_MenuFrame(QFrame):

    def __init__(self, centerframe):
        super(c_MenuFrame, self).__init__(centerframe)
        self.centerframe = centerframe

        self.initUI()

    def initUI(self):
        self.vboxlayout = QVBoxLayout()

        btn_LP = QPushButton("짧은글연습")
        btn_LP.number = 1
        self.vboxlayout.addWidget(btn_LP)

        btn_PP = QPushButton('긴글연습')
        btn_PP.number = 2
        self.vboxlayout.addWidget(btn_PP)

        btn_AR = QPushButton('산성비')
        btn_AR.number = 1
        btn_AR.clicked.connect(self.btnClicked)
        self.vboxlayout.addWidget(btn_AR)

        btn_Record = QPushButton('기록')
        btn_Record.number = 4
        self.vboxlayout.addWidget(btn_Record)

        btn_Quit = QPushButton('종료 [Ctrl+Q]')
        btn_Quit.clicked.connect(qApp.quit)
        self.vboxlayout.addWidget(btn_Quit)

        self.setLayout(self.vboxlayout)

    def btnClicked(self):
        btn = self.sender()
        self.centerframe.mainwindow.changeLayout(btn.number)



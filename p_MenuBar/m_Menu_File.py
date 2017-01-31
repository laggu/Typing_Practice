from PyQt5.QtWidgets import QMenu, QAction, qApp
from PyQt5.QtGui import QIcon

class c_FileMenu(QMenu):

    def __init__(self):
        super(c_FileMenu, self).__init__(title='File')

        self.initUI()

    def initUI(self):
        self.exitAction()


    def exitAction(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        #exitAction.setStatusTip('Exit application')
        #exitAction.setWhatsThis('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.addAction(exitAction)
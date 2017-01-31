from PyQt5.QtWidgets import QMenuBar
from p_MenuBar import *

class c_MenuBar(QMenuBar):
    """Menu cutomizing"""
    def __init__(self):
        super(c_MenuBar, self).__init__()


        self.initUI()

    def initUI(self):
        self.filemenu = m_Menu_File.c_FileMenu()
        self.addMenu(self.filemenu)

        self.show()
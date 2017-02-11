import time, random
from threading import Thread

from PyQt5.QtWidgets import QFrame
from .m_Rain import c_Rain as Rain

class c_GameFrame(QFrame):
    """The frame where the words will be droped"""
    words = []
    raindrop = []

    def __init__(self, arFrame):
        QFrame.__init__(self, arFrame)

        self.arframe = arFrame

        self.initUI()
        self.loadWords()


    def initUI(self):
        self.setFrameStyle(1)

        self.setMinimumWidth(self.arframe.height())
        self.setMinimumHeight(self.arframe.height()*.90)

    def loadWords(self):
        f = open('../static/text/word.txt', encoding='utf-8')

        lines = f.readlines()

        for line in lines:
            c_GameFrame.words.extend(line.split(' '))

        f.close()

        random.shuffle(c_GameFrame.words)

    def start(self):
        it = 0
        t = time.time()
        while True:
            if (time.time() - t) > 1 - (self.arframe.level*0.1):
                word = Rain(c_GameFrame.words[it], self)
                self.raindrop.append(word)
                t = time.time()
                it += 1
            self.repaint()
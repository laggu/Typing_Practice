from PyQt5.QtWidgets import QLabel
from threading import Thread
import random, time



class c_Rain(QLabel, Thread):

    def __init__(self, word, parent):
        QLabel.__init__(self, word, parent)
        Thread.__init__(self)

        self.setText(word)
        self.parent = parent

        from p_AcidRain.m_AcidRainFrame import c_AcidRainFrame
        #self.speed = 1 - random.random()*0.2*c_AcidRainFrame.level
        self.speed = 0.1

        self.x = parent.width()*random.random()
        self.y = 10

        self.move(self.x, self.y)
        self.start()

    def run(self):

        while self.y < self.parent.height():
            self.y += 10
            self.move(self.x, self.y)
            time.sleep(self.speed)
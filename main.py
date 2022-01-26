import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import easy
import hard
import medium

MainForm = uic.loadUiType(os.path.join(os.getcwd(), "Main.ui"))[0]


class MainWindow(QMainWindow, MainForm):
    def __init__(self,):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.easywind = easy.EasyWindow()
        self.mediumwind = medium.MediumWindow()
        self.hardwind = hard.HardWindow()
        self.StartButton.clicked.connect(self.Play)

    def Play(self):
        if self.Rb_easymode.isChecked() == True:
            self.easywind.show()
        if self.Rb_mediummode.isChecked() == True:
            self.mediumwind.show()
        if self.Rb_hardmode.isChecked() == True:
            self.hardwind.show()


app = QApplication(sys.argv)
app.setStyle("Fusoin")
w = MainWindow()
w.show()
app.exec_()
sys.exit()

import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from random import randint

"""1:R 2:B 3:G 4:Y 5:Pu 6:Pi 7:W 8:Lb"""
Redstyle = "background-color: rgb(255, 0, 0); border-radius:15px;"
Bluestyle = "background-color: rgb(0, 0, 255); border-radius:15px;"
Greenstyle = "background-color: rgb(0, 170, 0); border-radius:15px;"
Yellowstyle = "background-color: rgb(255, 255, 0); border-radius:15px;"
Purplestyle = "background-color: rgb(139, 0, 104); border-radius:15px;"
Pinkstyle = "background-color: rgb(255, 90, 90); border-radius:15px;"
Whitestyle = "background-color: rgb(255, 255, 255); border-radius:15px;"
Lightbluestyle = "background-color: rgb(0, 255, 238); border-radius:15px;"

Cstyle = "background-color: rgb(97, 97, 97); border-radius:25px;"
Gstyle = "background-color : rgb(97, 97, 97); border-radius:15px;"
Hstyle = "background-color: rgb(97, 97, 97);"

EasyForm = uic.loadUiType(os.path.join(os.getcwd(), "Easy.ui"))[0]


class EasyWindow(QMainWindow, EasyForm):
    def __init__(self,):
        super(EasyWindow, self).__init__()
        self.WIN = False
        self.LOSS = False
        self.RandArr = [randint(1, 8) for i in range(4)]
        self.currentRow = [0, 0, 0, 0]
        self.row = 1
        self.column = 1
        self.setupUi(self)
        self.ExitButton.clicked.connect(self.quit_press)
        self.ResetgameButton.clicked.connect(self.first_reset_msg)
        self.ResetrowButton.clicked.connect(self.row_reset)
        self.CheckButton.clicked.connect(self.check)
        self.RedButton.clicked.connect(self.R_pressed)
        self.BlueButton.clicked.connect(self.B_pressed)
        self.GreenButton.clicked.connect(self.G_pressed)
        self.YellowButton.clicked.connect(self.Y_pressed)
        self.PurpleButton.clicked.connect(self.Pu_pressed)
        self.PinkButton.clicked.connect(self.Pi_pressed)
        self.WhiteButton.clicked.connect(self.W_pressed)
        self.LightblueButton.clicked.connect(self.Lb_pressed)

    def R_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Redstyle)
            self.currentRow[self.column-1] = 1
            if self.column < 4:
                self.column += 1

    def B_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Bluestyle)
            self.currentRow[self.column-1] = 2
            if self.column < 4:
                self.column += 1

    def G_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Greenstyle)
            self.currentRow[self.column-1] = 3
            if self.column < 4:
                self.column += 1

    def Y_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Yellowstyle)
            self.currentRow[self.column-1] = 4
            if self.column < 4:
                self.column += 1

    def Pu_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Purplestyle)
            self.currentRow[self.column-1] = 5
            if self.column < 4:
                self.column += 1

    def Pi_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Pinkstyle)
            self.currentRow[self.column-1] = 6
            if self.column < 4:
                self.column += 1

    def W_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Whitestyle)
            self.currentRow[self.column-1] = 7
            if self.column < 4:
                self.column += 1

    def Lb_pressed(self):
        if self.WIN == False and self.LOSS == False:
            self.frameG.children()[
                self.row-1].children()[self.column-1].setStyleSheet(Lightbluestyle)
            self.currentRow[self.column-1] = 8
            if self.column < 4:
                self.column += 1

    def game_reset(self):
        self.row = 1
        self.column = 1
        self.currentRow = [0, 0, 0, 0]
        self.RandArr = [randint(1, 8) for i in range(4)]

        self.Color1.setStyleSheet(Cstyle)
        self.Color2.setStyleSheet(Cstyle)
        self.Color3.setStyleSheet(Cstyle)
        self.Color4.setStyleSheet(Cstyle)

        for x in self.frameG.children():
            for y in x.children():
                y.setStyleSheet(Gstyle)

        for x in self.frameH.children():
            for y in x.children():
                y.setStyleSheet(Hstyle)
        self.WIN = False
        self.LOSS = False

    def row_reset(self):
        if self.WIN == False and self.LOSS == False:
            for i in range(4):
                self.frameG.children()[
                    self.row-1].children()[i].setStyleSheet(Gstyle)
            self.column = 1
            self.currentRow = [0, 0, 0, 0]

    def check(self):
        if self.WIN == False and self.LOSS == False and self.currentRow[3] != 0:
            red_hint = 0

            RAcopy = self.RandArr.copy()

            for i, j, k in zip(self.RandArr, self.currentRow, range(4)):
                if i == j:
                    red_hint += 1
                    self.frameH.children()[
                        self.row-1].children()[k].setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.currentRow[k] = -1
                    RAcopy[k] = -1

            for j, k in zip(self.currentRow, range(4)):
                if (j in RAcopy) == True and j != -1:
                    self.frameH.children()[
                        self.row-1].children()[k].setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.currentRow[k] = -1
                    RAcopy[RAcopy.index(j)] = -1

            if red_hint == 4 or self.row == 10:
                for i in range(4):
                    if self.RandArr[i] == 1:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(255, 0, 0); border-radius:25px;")
                    if self.RandArr[i] == 2:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(0, 0, 255); border-radius:25px;")
                    if self.RandArr[i] == 3:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(0, 170, 0); border-radius:25px;")
                    if self.RandArr[i] == 4:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(255, 255, 0); border-radius:25px;")
                    if self.RandArr[i] == 5:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(139, 0, 104); border-radius:25px;")
                    if self.RandArr[i] == 6:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(255, 90, 90); border-radius:25px;")
                    if self.RandArr[i] == 7:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(255, 255, 255); border-radius:25px;")
                    if self.RandArr[i] == 8:
                        self.frameC.children()[i].setStyleSheet(
                            "background-color: rgb(0, 255, 238); border-radius:25px;")
                msgbx = QMessageBox()
                msgbx.setIcon(QMessageBox.Information)
                msgbx.setStyleSheet("font: 11pt ""MS Shell Dlg 2"";")
                if red_hint == 4:
                    self.WIN = True
                    msgbx.setWindowTitle("Win Message")
                    msgbx.setText(
                        "Congratulations You Won!")
                elif self.row == 10:
                    msgbx.setWindowTitle("Lose Message")
                    msgbx.setText(
                        "Oops You Lost!")
                    self.LOSS = True
                msgbx.setInformativeText(
                    "Click on Reset Game to start a new game")
                msgbx.exec_()
            else:
                self.column = 1
                self.currentRow = [0, 0, 0, 0]
                self.row += 1

    def quit_press(self):
        msgbx = QMessageBox()
        msgbx.setWindowTitle("Exit Message")
        msgbx.setText(
            "Are you sure you want to quit?")
        msgbx.setIcon(QMessageBox.Question)
        msgbx.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msgbx.setDefaultButton(QMessageBox.No)
        msgbx.setStyleSheet("font: 11pt ""MS Shell Dlg 2"";")
        msgbx.buttonClicked.connect(self.exit_popup)
        msgbx.exec_()

    def exit_popup(self, clk):
        if clk.text() == "&Yes":
            self.close()

    def first_reset_msg(self):
        if self.WIN == True or self.LOSS == True:
            self.game_reset()
        else:
            msgbx = QMessageBox()
            msgbx.setWindowTitle("Reset Message")
            msgbx.setText(
                "Are you sure you want to rest the game?")
            msgbx.setIcon(QMessageBox.Question)
            msgbx.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
            msgbx.setDefaultButton(QMessageBox.No)
            msgbx.setStyleSheet("font: 11pt ""MS Shell Dlg 2"";")
            msgbx.buttonClicked.connect(self.exit_popup_reset)
            msgbx.exec_()

    def exit_popup_reset(self, clk):
        if clk.text() == "&Yes":
            self.game_reset()

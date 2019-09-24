import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QRadioButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QRect, QSize
import random
import sys

class game(QWidget):
    def __init__(self):
        super().__init__()

        self.x = 100
        self.y = 200
        self.width = 340
        self.height = 360

        self.change_y = 40
        self.change_x = 10

        self.Button1 = QPushButton(self)
        self.Button1.setGeometry(40+self.change_x, 60+self.change_y, 80, 80)
        self.Button1.clicked.connect(self.Button_1)
        self.Button2 = QPushButton(self)
        self.Button2.setGeometry(120+self.change_x, 60+self.change_y, 80, 80)
        self.Button2.clicked.connect(self.Button_2)
        self.Button3 = QPushButton(self)
        self.Button3.setGeometry(200+self.change_x, 60+self.change_y, 80, 80)
        self.Button3.clicked.connect(self.Button_3)

        self.Button4 = QPushButton(self)
        self.Button4.setGeometry(40+self.change_x, 140+self.change_y, 80, 80)
        self.Button4.clicked.connect(self.Button_4)
        self.Button5 = QPushButton(self)
        self.Button5.setGeometry(120+self.change_x, 140+self.change_y, 80, 80)
        self.Button5.clicked.connect(self.Button_5)
        self.Button6 = QPushButton(self)
        self.Button6.setGeometry(200+self.change_x, 140+self.change_y, 80, 80)
        self.Button6.clicked.connect(self.Button_6)

        self.Button7 = QPushButton(self)
        self.Button7.setGeometry(40+self.change_x, 220+self.change_y, 80, 80)
        self.Button7.clicked.connect(self.Button_7)
        self.Button8 = QPushButton(self)
        self.Button8.setGeometry(120+self.change_x, 220+self.change_y, 80, 80)
        self.Button8.clicked.connect(self.Button_8)
        self.Button9 = QPushButton(self)
        self.Button9.setGeometry(200+self.change_x, 220+self.change_y, 80, 80)
        self.Button9.clicked.connect(self.Button_9)

        self.player_ch = ""
        self.bot_choice = ""
        self.O_Button = QPushButton(self)
        self.O_Button.setGeometry(260, 10, 40, 40)
        self.O_Button.setIcon(QIcon(os.path.join("Images/O_image.png")))
        self.O_Button.setIconSize(QSize(40, 40))
        self.O_Button.clicked.connect(self.choose_O)

        self.X_Button = QPushButton(self)
        self.X_Button.setGeometry(300, 10, 40, 40)
        self.X_Button.setIcon(QIcon(os.path.join("Images/X_image.png")))
        self.X_Button.setIconSize(QSize(40, 40))
        self.X_Button.clicked.connect(self.choose_X)

        self.label1 = QLabel(self)

        self.label2 = QLabel(self)

        self.p1 = ""
        self.p2 = ""
        self.p3 = ""
        self.p4 = ""
        self.p5 = ""
        self.p6 = ""
        self.p7 = ""
        self.p8 = ""
        self.p9 = ""

        self.b1 = ""
        self.b2 = ""
        self.b3 = ""
        self.b4 = ""
        self.b5 = ""
        self.b6 = ""
        self.b7 = ""
        self.b8 = ""
        self.b9 = ""

        self.ch = ["ch1", "ch2", "ch3",
                   "ch4", "ch5", "ch6",
                   "ch7", "ch8", "ch9"]

        self.setup()

    def choose_O(self):
        self.player_ch = "Images/O_image.png"
        self.bot_choice = "Images/X_image.png"

    def choose_X(self):
        self.player_ch = "Images/X_image.png"
        self.bot_choice = "Images/O_image.png"

    def Button_1(self):
        self.p1 = self.player_ch
        self.b1 = self.bot_choice

        self.Button1.setIcon(QIcon(os.path.join(self.p1)))
        self.Button1.setIconSize(QSize(80, 80))
        if self.p2 and self.p3 or self.p5 and self.p9 or self.p4 and self.p7 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_2(self):
        self.p2 = self.player_ch
        self.b2 = self.bot_choice

        self.Button2.setIcon(QIcon(self.p2))
        self.Button2.setIconSize(QSize(80, 80))
        if self.p1 and self.p3 or self.p5 and self.p8 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_3(self):
        self.p3 = self.player_ch
        self.b3 = self.bot_choice

        self.Button3.setIcon(QIcon(self.p3))
        self.Button3.setIconSize(QSize(80, 80))
        if self.p1 and self.p2 or self.p5 and self.p7 or self.p6 and self.p9 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_4(self):
        self.p4 = self.player_ch
        self.b4 = self.bot_choice

        self.Button4.setIcon(QIcon(self.p4))
        self.Button4.setIconSize(QSize(80, 80))

        if self.p5 and self.p6 or self.p1 and self.p7 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_5(self):
        self.p5 = self.player_ch
        self.b5 = self.bot_choice

        self.Button5.setIcon(QIcon(self.p5))
        self.Button5.setIconSize(QSize(80, 80))

        if self.p4 and self.p6 or self.p1 and self.p9 or self.p2 and self.p8 or self.p3 and self.p7 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_6(self):
        self.p6 = self.player_ch
        self.b6 = self.bot_choice

        self.Button6.setIcon(QIcon(self.p6))
        self.Button6.setIconSize(QSize(80, 80))

        if self.p5 and self.p4 or self.p3 and self.p9 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_7(self):
        self.p7 = self.player_ch
        self.b7 = self.bot_choice

        self.Button7.setIcon(QIcon(self.p7))
        self.Button7.setIconSize(QSize(80, 80))

        if self.p4 and self.p1 or self.p8 and self.p9 or self.p5 and self.p3 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        x = random.choice(self.ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_8(self):
        self.p8 = self.player_ch
        self.b8 = self.bot_choice

        self.Button8.setIcon(QIcon(self.p8))
        self.Button8.setIconSize(QSize(80, 80))

        if self.p5 and self.p2 or self.p7 and self.p9 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        ch = self.ch
        x = random.choice(ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def Button_9(self):
        self.p9 = self.player_ch
        self.b9 = self.bot_choice

        self.Button9.setIcon(QIcon(self.p9))
        self.Button9.setIconSize(QSize(80, 80))

        if self.p8 and self.p7 or self.p5 and self.p1 or self.p6 and self.p3 == self.player_ch:
            self.label1.setGeometry(80, 60, 100, 30)
            self.label1.setText("YOU Win")

        ch = self.ch
        x = random.choice(ch)
        if x == "ch1" and self.p1 == "" and self.b1 == "":
            self.Button1.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button1.setIconSize(QSize(80, 80))
        if x == "ch2" and self.p2 == "" and self.b2 == "":
            self.Button2.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button2.setIconSize(QSize(80, 80))
        if x == "ch3" and self.p3 == "" and self.b3 == "":
            self.Button3.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button3.setIconSize(QSize(80, 80))
        if x == "ch4" and self.p4 == "" and self.b4 == "":
            self.Button4.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button4.setIconSize(QSize(80, 80))
        if x == "ch5" and self.p5 == "" and self.b5 == "":
            self.Button5.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button5.setIconSize(QSize(80, 80))
        if x == "ch6" and self.p6 == "" and self.b6 == "":
            self.Button6.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button6.setIconSize(QSize(80, 80))
        if x == "ch7" and self.p7 == "" and self.b7 == "":
            self.Button7.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button7.setIconSize(QSize(80, 80))
        if x == "ch8" and self.p8 == "" and self.b8 == "":
            self.Button8.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button8.setIconSize(QSize(80, 80))
        if x == "ch9" and self.p9 == "" and self.b9 == "":
            self.Button9.setIcon(QIcon(os.path.join(self.bot_choice)))
            self.Button9.setIconSize(QSize(80, 80))

    def setup(self):
        self.setGeometry(self.x, self.y, self.width, self. height)
        self.setWindowTitle("tic tac toe")
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = game()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
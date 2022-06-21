from turtle import shape
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QCursor 


class HomeWidget(QWidget):
    def __init__(self):
        """ Main Widgets Class """
        super().__init__()
        self.setupScr()
        self.setupLayout()
        self.setupWidgets()

    def setupScr(self):
        """ Screen Setup """
        self.setWindowTitle('Game Manager')
        self.scr = self.screen().size()

        # calculating window pos ( centering the window - dividing height and width by 4 works)
        self.window_pos = (self.scr.width()/4, self.scr.height()/4)

        self.HEIGHT = 650
        self.WIDTH = 450

        self.setGeometry(*self.window_pos, self.HEIGHT, self.WIDTH)

    def setupLayout(self):
        """ Initilize a Vertical Layout """
        self.vlayout = QVBoxLayout(self)
        self.setLayout(self.vlayout)

    def setupWidgets(self):
        """ Makes and Adds Widgets to the vlayout """
        # Add Game Btn
        self.add_game_btn = QPushButton('Add Game')
        self.pointing_cursor = QCursor().shape().PointingHandCursor
        self.add_game_btn.setCursor(self.pointing_cursor)

        # Add Widgets to vlayout
        self.vlayout.addWidget(self.add_game_btn)

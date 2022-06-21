from PySide6.QtWidgets import QWidget


class HomeWidget(QWidget):
    def __init__(self):
        """ Main Widgets Class """
        super().__init__()

        # CONSTANTS
        self.HEIGHT = 650
        self.WIDTH = 450

        self.setup()

    def setup(self):
        """ Screen Setup """
        self.setWindowTitle('Game Manager')
        # screen size
        self.scr = self.screen().size() 
        # calculating window pos ( centering the window - dividing height and width by 4 works)
        self.window_pos = (self.scr.width()/4, self.scr.height()/4) 
        self.setGeometry(*self.window_pos, self.HEIGHT, self.WIDTH)

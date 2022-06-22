from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QCursor
from PySide6.QtCore import QUrl


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
        scr = self.screen().size()

        # calculating window position
        # ( centering the window - dividing height and width by 4 works )
        window_pos = (scr.width() / 4, scr.height() / 4)

        HEIGHT = 650
        WIDTH = 450

        self.setGeometry(*window_pos, HEIGHT, WIDTH)

    def setupLayout(self):
        """ Initilize a Vertical Layout """
        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

    def setupWidgets(self):
        """ Makes and Adds Widgets to the vlayout """
        # Vertical layout for adding game entries
        game_entries = QWidget()
        self.game_entries_layout = QVBoxLayout()
        game_entries.setLayout(self.game_entries_layout)

        # Horizontal layout for adding btns
        btns = QWidget()
        btns_layout = QHBoxLayout()
        btns.setLayout(btns_layout)

        # Cursors
        pointing_cursor = QCursor().shape().PointingHandCursor

        # Game Btn - Widget, Connectors
        add_game_btn = QPushButton('Add Game')
        add_game_btn.setCursor(pointing_cursor)
        add_game_btn.clicked.connect(self.add_game_entry)

        # Options Btn - Widget
        options_btn = QPushButton(':')
        options_btn.setCursor(pointing_cursor)

        # Play Btn - Widget
        play_btn = QPushButton('|>')
        play_btn.setCursor(pointing_cursor)

        # Add Widgets to btns_layout
        btns_layout.addWidget(add_game_btn, 3)
        btns_layout.addWidget(options_btn, 2)
        btns_layout.addWidget(play_btn, 5)

        # Add Widgets to vlayout
        self.vlayout.addWidget(game_entries, 1)
        self.vlayout.addWidget(btns, 0)

    def add_game_entry(self):
        """ Opens the game-executable file selector dialog """
        selected_file_url: QUrl = QFileDialog.getOpenFileUrl(filter="Executables (*exe)")[0]
        selected_file_name = selected_file_url.fileName()
        self.game_entries_layout.addWidget(QLabel(selected_file_name))


from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QCursor
from gameentry import GameEntry


class HomeWidget(QWidget):
    def __init__(self):
        """ Home Widget Class """
        super().__init__()
        self.game_entry_window = None # this window will be set when add_game_btn is clicked
        self.setupWindow()
        self.setupLayout()
        self.setupWidgets()

    def setupWindow(self):
        """ Window Setup """
        self.setWindowTitle('Game Manager')
        scr = self.screen().size()

        # calculating window position
        # ( centering the window - dividing height and width by 4 works )
        window_pos = (scr.width() / 4, scr.height() / 4)

        HEIGHT = 650
        WIDTH = 450

        self.setGeometry(*window_pos, HEIGHT, WIDTH)

    def setupLayout(self):
        """ Initialize a Vertical Layout """
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

        # Add Game Btn - Widget, Connectors
        add_game_btn = QPushButton('Add Game')
        add_game_btn.setCursor(pointing_cursor)
        add_game_btn.clicked.connect(self.new_game_entry)

        # Options Btn - Widget
        options_btn = QPushButton('Options')
        options_btn.setCursor(pointing_cursor)

        # Play Btn - Widget
        play_btn = QPushButton('Play')
        play_btn.setCursor(pointing_cursor)

        # Add Widgets to btns_layout
        btns_layout.addWidget(add_game_btn, 3)
        btns_layout.addWidget(options_btn, 2)
        btns_layout.addWidget(play_btn, 5)

        # Add Widgets to vlayout
        self.vlayout.addWidget(game_entries, 1)
        self.vlayout.addWidget(btns, 0)

    def new_game_entry(self):
        """ Shows a game entry window to add a game entry """
        self.game_entry_window = GameEntry(hw=self)
        self.game_entry_window.show()
        self.setEnabled(False)  # disabling the home widget

    def closeEvent(self, event):
        if self.game_entry_window:
            self.game_entry_window.close()
        event.accept()

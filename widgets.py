from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QFileDialog, QLineEdit
from PySide6.QtGui import QCursor
from PySide6.QtCore import QUrl


class GameEntry(QWidget):
    def __init__(self):
        """ This class helps to add new game entry """
        super().__init__()
        self.setupWindow()
        self.setupLayout()
        self.setupWidgets()

    def setupWindow(self):
        """ Window Setup """
        self.setWindowTitle('Add a Game')

        scr = self.screen().size()
        # calculating the position of the window 
        # centering it - dividing the screen height and width by some value(find by just experimenting)
        window_pos = (scr.width() / 2.7, scr.height() / 2.5)

        HEIGHT = 210
        WIDTH = 320

        self.setGeometry(*window_pos, WIDTH, HEIGHT)

    def setupLayout(self):
        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)

    def setupWidgets(self):
        # Name - Widget
        game_name = QLineEdit()
        game_name.setPlaceholderText("Game Name  *required")
        # Path - Widget, Layout 
        path_widget = QWidget()
        path_widget_layout = QHBoxLayout()
        path_widget.setLayout(path_widget_layout)

        game_path = QLineEdit()
        game_path.setPlaceholderText("Enter a valid Path  *required")
        game_path_browse = QPushButton("Browse")
    
        path_widget_layout.addWidget(game_path)
        path_widget_layout.addWidget(game_path_browse)

        # Game Add Btn
        add_btn = QPushButton('Add Game')

        self.vlayout.addWidget(game_name)
        self.vlayout.addWidget(path_widget)
        self.vlayout.addWidget(add_btn)


class HomeWidget(QWidget):
    def __init__(self):
        """ Home Widget Class """
        super().__init__()
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
        self.game_entry_window = GameEntry()
        self.game_entry_window.show()

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QFileDialog, QLineEdit, QLabel
from PySide6.QtCore import QUrl


class GameEntry(QWidget):
    def __init__(self, hw):
        """ This class helps to add new game entry """
        super().__init__()
        self.hw = hw
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
        self.game_name = QLineEdit()
        self.game_name.setPlaceholderText("Game Name  *required")
        # Path - Widget, Layout 
        path_widget = QWidget()
        path_widget_layout = QHBoxLayout()
        path_widget.setLayout(path_widget_layout)

        self.game_path = QLineEdit()
        self.game_path.setPlaceholderText("Enter a valid Path  *required")

        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.game_select_dialog)

        path_widget_layout.addWidget(self.game_path)
        path_widget_layout.addWidget(browse_btn)

        # Game Add Btn
        add_btn = QPushButton('Add Game')
        add_btn.clicked.connect(self.add_game)

        self.vlayout.addWidget(self.game_name)
        self.vlayout.addWidget(path_widget)
        self.vlayout.addWidget(add_btn)

    def game_select_dialog(self):
        game_file_url: QUrl = QFileDialog.getOpenFileUrl(filter="Game Executable (*exe)")[0]
        game_file_url = game_file_url.path()[1:] # [1:] is used to remove the first character ('/') in the str
        self.game_path.setText(game_file_url) 

    def add_game(self):
        game_name = self.game_name.text().strip()
        self.game_name.setText(game_name) # removing extra spaces to avoid confusion
        game_path = self.game_path.text().strip()
        self.game_path.setText(game_path)   # removing extra spaces to avoid confusion

        if game_name != "" and game_path != "": # .strip to remove spaces
            game_entry = QWidget()
            game_entry_layout = QHBoxLayout()
            game_entry.setLayout(game_entry_layout)
            game_entry_layout.addWidget(QLabel(f"Name: {game_name}"))
            game_entry_layout.addWidget(QLabel(f"Path: {game_path}"))

            self.hw.game_entries_layout.addWidget(game_entry)
            self.close()

        else:
            # changing the placholder value if the fields are empty
            self.game_name.setPlaceholderText("!! REQUIRED !!") if game_name == "" else None
            self.game_path.setPlaceholderText("!! REQUIRED !!") if game_path == "" else None




    def closeEvent(self, event):
        self.hw.setEnabled(True)  # enabling home widget
        self.hw.game_entry_window = None
        event.accept()
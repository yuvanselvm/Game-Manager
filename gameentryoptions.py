from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QFileDialog
from PySide6.QtCore import QUrl

class GameEntryOptions(QWidget):
    def __init__(self, hw):
        super().__init__()
        self.hw= hw
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
        self.game_name.setPlaceholderText("Edit Game Name  *required")
        # Path - Widget, Layout
        path_widget = QWidget()
        path_widget_layout = QHBoxLayout()
        path_widget.setLayout(path_widget_layout)

        self.game_path = QLineEdit()
        self.game_path.setPlaceholderText("Edit Path to a Executable *required")

        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.game_select_dialog)

        path_widget_layout.addWidget(self.game_path)
        path_widget_layout.addWidget(browse_btn)

        # Game Add Btn
        add_btn = QPushButton('Save Edit')

        self.vlayout.addWidget(self.game_name)
        self.vlayout.addWidget(path_widget)
        self.vlayout.addWidget(add_btn)

    def game_select_dialog(self):
        game_file_url: QUrl = QFileDialog.getOpenFileUrl(
            filter="Game Executable (*exe)")[0]
        # [1:] is used to remove the first character ('/') in the str
        game_file_url = game_file_url.path()[1:]
        self.game_path.setText(game_file_url)

    def closeEvent(self, event):
        self.hw.setEnabled(True)  # enabling home widget
        self.hw.ge_options = None
        event.accept()


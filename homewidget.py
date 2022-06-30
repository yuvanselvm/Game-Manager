from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem
from PySide6.QtGui import QCursor
from gameentry import GameEntry
import os.path as op
import json
import subprocess as sp


class HomeWidget(QWidget):
    def __init__(self):
        """ Home Widget Class """
        super().__init__()
        self.game_entry_window = None # it is declared here bcoz to close game_entry_window when app exits
        self.setupWindow()
        self.setupLayout()
        self.setupWidgets()
        self.load_entries()

    def setupWindow(self):
        """ Window Setup """
        self.setWindowTitle('Game Manager')
        self.setStyleSheet(''.join(line for line in open('./style.qss', 'r')))
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
        self.game_entries = QListWidget()

        # Horizontal layout for adding btns
        btns = QWidget()
        btns_layout = QHBoxLayout()
        btns.setLayout(btns_layout)

        # Cursors
        pointing_cursor = QCursor().shape().PointingHandCursor

        # Add Game Btn - Widget, Connectors
        add_game_btn = QPushButton('ADD')
        add_game_btn.setObjectName('bordered')
        add_game_btn.setCursor(pointing_cursor)
        add_game_btn.clicked.connect(self.new_game_entry)
        add_game_btn.setFixedSize(150, 60)

        # Options Btn - Widget
        options_btn = QPushButton(':')
        options_btn.setObjectName('bordered')
        options_btn.setCursor(pointing_cursor)
        options_btn.setFixedSize(40,60)

        # Play Btn - Widget
        play_btn = QPushButton('>')
        play_btn.setObjectName('defaultBtn')
        play_btn.setCursor(pointing_cursor)
        play_btn.clicked.connect(self.run_game)
        play_btn.setFixedSize(65, 70)

        # Add Widgets to btns_layout
        btns_layout.addWidget(add_game_btn)
        btns_layout.addStretch(25)
        btns_layout.addWidget(options_btn)
        btns_layout.addStretch(1)
        btns_layout.addWidget(play_btn)

        # Add Widgets to vlayout
        self.vlayout.addWidget(self.game_entries, 1)
        self.vlayout.addWidget(btns, 0)

    def load_entries(self):
        """ Reads and Add game_entries from json file """

        # remove previous entries
        self.game_entries.clear()

        db_name = 'gameentries.json'
        curr_dir = op.abspath(op.curdir)
        db_path = op.join(curr_dir, db_name)

        # creating db if not present
        if not op.exists(db_path):
            with open(db_path, 'w') as db:
                default_stucture = {"game_entries": []}
                default_stucture = json.dumps(default_stucture)
                db.write(default_stucture)

        with open(db_path, 'r') as db:
            game_entries: str = "".join(line for line in db.readlines())
            game_entries: dict = json.loads(game_entries)
            self.game_entries_list = game_entries['game_entries']

        for game_entry in self.game_entries_list:
            game_name = game_entry['game_name']
            game_path = game_entry['game_path']
            game_entry: QListWidgetItem = QListWidgetItem(f"{game_name[:60]}")
            game_entry.setData(1, game_path)
            self.game_entries.addItem(game_entry)

    def new_game_entry(self):
        """ Shows a game entry window to add a game entry """
        self.game_entry_window = GameEntry(hw=self)
        self.game_entry_window.show()
        self.setEnabled(False)  # disabling the home widget

    def run_game(self):
        # selected_game - sg
        sg: QListWidgetItem = self.game_entries.selectedItems()[0]
        sg_path = sg.data(1)
        sg_folder_path = op.split(sg_path)[0]
        # subprocess module - sp
        sp.Popen(args='', executable=sg_path, cwd=sg_folder_path)
        self.close()

    def closeEvent(self, event):
        if self.game_entry_window:
            self.game_entry_window.close()
        event.accept()

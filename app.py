import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
from homewidget import HomeWidget

app = QApplication()
QFontDatabase().addApplicationFont('./fonts/Inconsolata-VariableFont_wdth,wght.ttf')
home = HomeWidget()
home.show()
sys.exit(app.exec())

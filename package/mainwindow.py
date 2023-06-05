from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from package.widgets.titlebar import TitleBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        titlbar = TitleBar()
        self.layout.addWidget(titlbar)

        self.layout.addStretch()

        window = QWidget()
        window.setLayout(self.layout)
        self.setCentralWidget(window)
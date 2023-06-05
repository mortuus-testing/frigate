from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class TitleBar(QWidget):
    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFixedHeight(24)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background: #cccccc")

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(4, 0, 4, 0)
        self.layout.addStretch()

        close_button = QPushButton('x')
        close_button.setFixedSize(20, 20)
        self.layout.addWidget(close_button)
        
        self.setLayout(self.layout)
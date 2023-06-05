from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from package.windows.page import PageWindow
from package.widgets.titlebar import TitleBar

class VaultWindow(PageWindow):
    def __init__(self, parent=None):
        super(VaultWindow, self).__init__(parent)
        
        self.layout = QVBoxLayout()

        titlebar = TitleBar()
        titlebar.closeSignal.connect(self.close)
        titlebar.moveWindowSignal.connect(self.moveWindowSignal)
        self.layout.addWidget(titlebar)

        self.layout.addWidget(QLabel("Vault Page"))

        navigation_widget = QWidget()
        navigation_widget.layout = QHBoxLayout()
        navigation_widget.setLayout(navigation_widget.layout)
        self.layout.addWidget(navigation_widget)

        vault_button = QPushButton("Vault")
        vault_button.clicked.connect(lambda: self.navigate("vault"))
        navigation_widget.layout.addWidget(vault_button)
        
        welcome_button = QPushButton("Welcome")
        welcome_button.clicked.connect(lambda: self.navigate("welcome"))
        navigation_widget.layout.addWidget(welcome_button)

        dashboard_button = QPushButton("Dashboard")
        dashboard_button.clicked.connect(lambda: self.navigate("dashboard"))
        navigation_widget.layout.addWidget(dashboard_button)

        window = QWidget()
        window.setLayout(self.layout)
        self.setCentralWidget(window)
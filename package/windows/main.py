from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from package.windows.page import PageWindow
from package.windows.dashboard import DashboardWindow
from package.windows.vault import VaultWindow
from package.windows.welcome import WelcomeWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.configurePages()

    def configurePages(self):
        self.pages = {}        
        self.pages_widget = QStackedWidget()

        self.registerPage("dashboard", DashboardWindow())
        self.registerPage("welcome", WelcomeWindow())
        self.registerPage("vault", VaultWindow())
        self.onNavigate('welcome')

        self.setCentralWidget(self.pages_widget)

    def registerPage(self, page_id, page_widget):
        if isinstance(page_widget, PageWindow) == False:
            raise Exception("Failed to register page. Widget is not an instance of PageWindow")

        self.pages[page_id] = page_widget
        self.pages_widget.addWidget(page_widget)
        page_widget.navigateSignal.connect(self.onNavigate)
        page_widget.closeSignal.connect(self.onClose)
        page_widget.moveWindowSignal.connect(self.onMoveWindow)

    @Slot()
    def onNavigate(self, page_id):
        if page_id in self.pages:
            page_widget = self.pages[page_id]
            self.pages_widget.setCurrentWidget(page_widget)

    @Slot()
    def onClose(self):
        self.close()

    @Slot()
    def onMoveWindow(self, delta):
        pos = self.mapToGlobal(delta)
        self.setGeometry(pos.x(), pos.y(), self.width(), self.height())
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PageWindow(QMainWindow):
    navigateSignal = Signal(str)
    closeSignal = Signal()
    moveWindowSignal = Signal(QPoint)

    def navigate(self, page_name):
        self.navigateSignal.emit(page_name)

    def close(self):
        self.closeSignal.emit()

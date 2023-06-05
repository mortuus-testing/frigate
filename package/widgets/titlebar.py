from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class TitleBar(QWidget):
    closeSignal = Signal()
    moveWindowSignal = Signal(QPoint)

    def __init__(self, parent=None):
        super(TitleBar, self).__init__(parent)
        self.is_pressing = False
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
        close_button.pressed.connect(self.closeSignal)
        self.layout.addWidget(close_button)
        
        self.setLayout(self.layout)

    def mousePressEvent(self, event):
        self.is_pressing = True
        self.start_local = event.pos()
        self.start_global = self.mapToGlobal(event.pos())

    def mouseMoveEvent(self, event):
        if (self.is_pressing):
            print(event.pos() - self.start_local)
            print(self.mapFromGlobal(event.pos()) - self.start_global)
            print("-----")

    def mousePressEvent(self, event):
        self.start_pos = event.pos()
        self.is_pressing = True

    def mouseMoveEvent(self, event):
        if (self.is_pressing == True):
            end_pos = event.pos()
            delta = end_pos - self.start_pos
            self.moveWindowSignal.emit(delta)

    def mouseReleaseEvent(self, event):
        self.is_pressing = False
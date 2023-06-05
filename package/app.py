from PySide6.QtWidgets import QApplication
from package.mainwindow import MainWindow
from PySide6.QtGui import Qt

def start(argv=[]):
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec()
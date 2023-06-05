from PySide6.QtWidgets import QApplication
from package.windows.main import MainWindow

def start(argv=[]):
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    return app.exec()
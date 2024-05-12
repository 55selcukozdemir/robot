import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from customWidget.nav.NavigationWidget import NavigationWidget


class app(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app.ui", self)
        self.callNavbar()
    def callNavbar(self):
        NavigationWidget(self)
        pass
if __name__ == "__main__":
    app_ = QApplication(sys.argv)
    widget = app()
    widget.show()
    sys.exit(app_.exec())
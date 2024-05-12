# Ekranda görünecek grafik
from PyQt6.QtWidgets import *

class GraphWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout:QVBoxLayout = QVBoxLayout()
        layout.addWidget(QPushButton(text= "buton"))
        self.setLayout(layout)
        
# Ekranda görünecek grafik
from PyQt6.QtWidgets import *

import pyqtgraph as pg
import numpy as np

class GraphWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout:QVBoxLayout = QVBoxLayout()
        x = np.arange(1000)
        y = np.random.normal(size=(3, 1000))
        plotWidget = pg.plot(title="Three plot curves")
        for i in range(3):
            plotWidget.plot(x, y[i], pen=(i,3))  ## setting pen=(i,3) automaticaly creates three different-colored pens
        layout.addWidget(plotWidget)
        self.setLayout(layout)


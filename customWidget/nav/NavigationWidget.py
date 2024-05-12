from PyQt6.QtWidgets import *
from customWidget.nav.NavButtonWidget import NavButtonWidget

class NavigationWidget(QVBoxLayout):
    def __init__(self, context:QMainWindow):
        super().__init__(context)
        self.nav:QVBoxLayout = context.navLayout
        self.context = context
        self.start()
    def start(self):
        # self.nav.addWidget(QPushButton(text= "buton")) # İleride dinamik olarak buton eklenmek istenirse kullanılacak.
        nav = NavButtonWidget("Ana sayfa", "analysis", self.context)
        self.nav.addWidget(nav)
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.nav.addSpacerItem(spacer)
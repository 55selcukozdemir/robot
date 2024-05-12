from PyQt6.QtWidgets import QPushButton, QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QWidget
from log.CLogger import *
from customWidget.nav.Router import Router
from customWidget.content.GraphWidget import *

class NavButtonWidget(QPushButton):
    def __init__(self, text:str, route: str, context):
        super().__init__(text, context)
        self.context:QMainWindow = context
        self.route: str = route
        self.text = text
        self.clicked.connect(self.clickFunction)

    def clickFunction(self):
        try:
            self.setContent()
        except Exception as e:
            s = "Nav bar yönlendirmesinde hata oluştu. Hatalı buton: " + self.text + " : " + repr(e)
            logger = CLogger()
            logger.log(s, LogLevel.ERROR)

    def setContent(self):
        route = Router()
        instance:QWidget =  route.createInstance(self.route)
        content:QVBoxLayout = self.context.contentLayout
        self.clear_layout(content)
        content.addWidget(instance) 
        
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()


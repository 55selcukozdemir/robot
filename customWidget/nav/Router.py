from PyQt6.QtWidgets import QWidget
from customWidget.content.GraphWidget import GraphWidget
class Router(): 
    def __init__(self) -> None:
        self.routeDic = {
            "home": "home",
            "analysis" : "GraphWidget"
        }
    def createInstance(self, route: str) ->  QWidget:
        for key, value in self.routeDic.items():
            if route == key:
                evalContent = eval(value)()
                return evalContent

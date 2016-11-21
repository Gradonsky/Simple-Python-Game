from PySide.QtGui import QWidget, QApplication
__author__ = 'Gradonski Janusz'


class ControllerWindow(QWidget):
    def __init__(self, model):
        """
        Konstruktor von der Klasse Controller
        """
        self.model=model


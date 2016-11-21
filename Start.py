import sys

from PySide.QtGui import *
from PySide.QtCore import *
import random
import View
import Model
import Controller

__author__ = 'Gradonski Janusz'

from View import *
import Model
class Start(QMainWindow):
    """
    Die ausfuhrbare Klasse.
    """
    def __init__(self, parent=None):
        """
        Konstruktor
        :param parent:
        :return:
        """
        super(Start, self).__init__(parent)
        self.model= Model.Model()
        self.main_ctrl= Controller.ControllerWindow(self.model)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)



      #  self.ui.pushButton_19








if __name__=="__main__":
    app = QApplication(sys.argv)
    c = Start()
    c.show()
    sys.exit(app.exec_())

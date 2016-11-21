__author__ = 'Janusz Gradonski'
import random
import View
import Controller
from PySide import QtGui

class Model(object):
    def __init__(self):
        """
            Der Konstruktor der Klasse Model
        """
        self.gesamt=0
        self.wert=0
        self.spiele=1
        self.korrekt=0
        self.falsch=0
        self.offen=15
        self.zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.zumAuswahlen = 15
        self.listeRandomZahlen= random.sample(self.zahlen, self.zumAuswahlen)

    """
    Die Getter-Setter Methoden
    """
    def getZahlen(self):
        return self.zahlen
    def getListe(self):
        return self.list_of_random_item
    def getWert(self):
        return self.wert
    def getSpiele(self):
        return self.spiele
    def getOffen(self):
        return self.offen
    def getKorrekt(self):
        return self.korrekt
    def getFalsch(self):
        return self.falsch
    def getGesamt(self):
        return self.gesamt
    def getNumSelect(self):
        return self.zumAuswahlen


    def clickedButton(self,button):
        """
        Funktion die beim Klicken von button aufgerufen wird .. Parameter ist der tatsaechlich geklickte button
        :param button: 
        :return:
        """
        but=int(button.text())
        if not self.listeRandomZahlen:
            self.label.setText(QtGui.QApplication.translate("MainWindow", "Gewonnen mit %s " % self.korrekt, None, QtGui.QApplication.UnicodeUTF8))
        else:
            if but == self.listeRandomZahlen[0]:
                self.korrekt += 1
                self.label_5.setText(QtGui.QApplication.translate("MainWindow", str(self.korrekt), None, QtGui.QApplication.UnicodeUTF8))
                self.listeRandomZahlen.remove(but)
            else:
                self.falsch +=1
                self.label_7.setText(QtGui.QApplication.translate("MainWindow", str(self.falsch), None, QtGui.QApplication.UnicodeUTF8))
                self.listeRandomZahlen.remove(but)
            button.setEnabled(False)
            self.wert += 1
            self.offen -= 1
            self.gesamt += 1
            self.label_9.setText(QtGui.QApplication.translate("MainWindow", str(self.gesamt), None, QtGui.QApplication.UnicodeUTF8))
            self.label_3.setText(QtGui.QApplication.translate("MainWindow", str(self.offen), None, QtGui.QApplication.UnicodeUTF8))




    def newGame(self,buttonse):
        self.listeRandomZahlen= random.sample(self.zahlen, self.zumAuswahlen)
        self.spiele +=1
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", str(self.spiele), None, QtGui.QApplication.UnicodeUTF8))
        self.korrekt=0
        self.falsch=0
        self.gesamt=0
        self.offen=15
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", str(self.korrekt), None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", str(self.falsch), None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", str(self.gesamt), None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", str(self.offen), None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(str(self.listeRandomZahlen[0]))
        self.pushButton_2.setText(str(self.listeRandomZahlen[1]))
        self.pushButton_3.setText(str(self.listeRandomZahlen[2]))
        self.pushButton_4.setText(str(self.listeRandomZahlen[3]))
        self.pushButton_6.setText(str(self.listeRandomZahlen[4]))
        self.pushButton_7.setText(str(self.listeRandomZahlen[5]))
        self.pushButton_8.setText(str(self.listeRandomZahlen[6]))
        self.pushButton_9.setText(str(self.listeRandomZahlen[7]))
        self.pushButton_10.setText(str(self.listeRandomZahlen[8]))
        self.pushButton_11.setText(str(self.listeRandomZahlen[9]))
        self.pushButton_13.setText(str(self.listeRandomZahlen[10]))
        self.pushButton_14.setText(str(self.listeRandomZahlen[11]))
        self.pushButton_16.setText(str(self.listeRandomZahlen[12]))
        self.pushButton_17.setText(str(self.listeRandomZahlen[13]))
        self.pushButton_15.setText(str(self.listeRandomZahlen[14]))
        self.listeRandomZahlen.sort()
        for a in buttonse:
           a.setEnabled(True)


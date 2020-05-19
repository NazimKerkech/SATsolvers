import PySide2
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QDesktopWidget, \
    QMainWindow, QFrame, QSizePolicy, QGraphicsView, QGraphicsScene
from PySide2.QtGui import QIcon, QPixmap, QFont
import files_rc
import sys


class Traitements(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        """self.vbox = QtWidgets.QVBoxLayout()

        self.vbox.addWidget(QLabel("Procession : "))
        self.setLayout(self.vbox)"""

        self.scene = QGraphicsScene()
        self.scene.addText("Proceeding :")
        self.setScene(self.scene)

    def afficher(self, formule):
        print(formule.__str__())
        self.scene.addText(formule.__str__())
        self.setScene(self.scene)
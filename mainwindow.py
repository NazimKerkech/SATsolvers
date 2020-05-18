from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QFrame
from PySide2.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import QFile
from topui import TopUi
from bottomui import BottomUi
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Assistant graphique pour SAT")    # Initialisation du titre


        # Creation des Frames
        vbox = QtWidgets.QVBoxLayout()

        tramesup = TopUi(self)                                     # Frame supperieur
        tramesup.setMinimumSize(QtCore.QSize(0, 65))
        tramesup.setMaximumSize(QtCore.QSize(1700, 65))

        self.trameinf = BottomUi(self)                                  # Frame inferieur

        # Unification
        vbox.addWidget(tramesup)
        vbox.addWidget(self.trameinf)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        buff = QWidget()
        buff.setLayout(vbox)

        self.setCentralWidget(buff)


# Initialisation de la fiche de style qss
style = open("stylesheet.qss")
StyleSheet = style.read()

# Instanciation de QApp
myApp = QApplication(sys.argv)
myApp.setStyleSheet(StyleSheet)

window = MainWindow()

available_geometry = myApp.desktop().availableGeometry(window)
window.resize(available_geometry.width() * 2 / 3, available_geometry.height() * 2 / 3)

window.show()

myApp.exec_()
sys.exit()
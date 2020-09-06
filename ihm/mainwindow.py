from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from ihm.topui import TopUi
from ihm.bottomui import BottomUi
import sys
import global_module


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Assistant graphique pour SAT")  # Initialisation du titre
        self.setWindowIcon(QtGui.QIcon("ihm//icons/16x16/kangaroo-icon.png"))

        # Creation des Frames
        vbox = QtWidgets.QVBoxLayout()

        tramesup = TopUi(self, self)  # Frame supperieur
        tramesup.setMinimumSize(QtCore.QSize(0, 65))
        tramesup.setMaximumSize(QtCore.QSize(1700, 65))

        self.trameinf = BottomUi(self, self)  # Frame inferieur

        # Unification
        vbox.addWidget(tramesup)
        vbox.addWidget(self.trameinf)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)

        buff = QWidget()
        buff.setLayout(vbox)

        self.setCentralWidget(buff)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Initialisation de la fiche de style qss
        style = open("ihm/stylesheet.qss")
        StyleSheet = style.read()
        self.setStyleSheet(StyleSheet)

        global_module.wind = self




# Instanciation de QApp
myApp = QApplication(sys.argv)

window = MainWindow()

available_geometry = myApp.desktop().availableGeometry(window)
window.resize(available_geometry.width() * 2 / 3, available_geometry.height() * 2 / 3)

window.show()
myApp.exec_()
sys.exit()

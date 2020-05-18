from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QFrame
from PySide2.QtGui import QIcon, QPixmap, QFont
import sys

class MiddleUi(QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Home onglets
        affichage = QFrame()
        infos_heuristique = QFrame()

        home_onglets = QtWidgets.QTabWidget()
        home_onglets.addTab(affichage, "Affichage")
        home_onglets.addTab(infos_heuristique, "Informations heuristiques")

        box_onglets = QtWidgets.QGridLayout()                  # Creation du layout qui va contenir home_onglets
        box_onglets.addWidget(home_onglets)

        box_onglets.setContentsMargins(0, 0, 0, 0)
        box_onglets.setSpacing(0)

        # Interface_principale StackWidget
        home = QFrame()
        algorithmes_menu = QFrame()
        heuristiques_menu = QFrame()

        home.setLayout(box_onglets)                            # Enrobage des onglets home dans une frame

        interface_principale = QtWidgets.QStackedWidget()      # Creation de l'interface principale (StackWidget)

        interface_principale.addWidget(home)
        interface_principale.addWidget(algorithmes_menu)
        interface_principale.addWidget(heuristiques_menu)

        box_middleUi = QtWidgets.QGridLayout()                  # Layout de l'interface principale
        box_middleUi.addWidget(interface_principale)

        box_middleUi.setContentsMargins(0, 0, 0, 0)
        box_middleUi.setSpacing(0)

        self.setLayout(box_middleUi)
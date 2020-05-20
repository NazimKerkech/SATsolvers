from PySide2 import QtWidgets
from PySide2.QtWidgets import QFrame
from ihm.interfaces_principales.traitements import *
from ihm.interfaces_principales.home import *


class MiddleUi(QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        # Home
        self.home = Home(self, self)
        self.home.setObjectName("home")

        # Affichage onglets
        self.affichage = Traitements(self)
        self.affichage.setFrameShape(QFrame.NoFrame)
        infos_heuristique = QFrame()
        infos_heuristique.setFrameShape(QFrame.NoFrame)

        home_onglets = QtWidgets.QTabWidget()
        home_onglets.addTab(self.affichage, "Affichage")
        home_onglets.addTab(infos_heuristique, "Informations heuristiques")

        box_onglets = QtWidgets.QGridLayout()                  # Creation du layout qui va contenir home_onglets
        box_onglets.addWidget(home_onglets)

        box_onglets.setContentsMargins(0, 0, 0, 0)
        box_onglets.setSpacing(0)

        # Interface_principale StackWidget
        self.affichage_frame = QFrame()
        self.algorithmes_menu = QFrame()
        self.heuristiques_menu = QFrame()

        self.affichage_frame.setLayout(box_onglets)                            # Enrobage des onglets affichage_principal dans une frame

        self.interface_principale = QtWidgets.QStackedWidget()      # Creation de l'interface principale (StackWidget)

        self.interface_principale.addWidget(self.home)
        self.interface_principale.addWidget(self.affichage_frame)
        self.interface_principale.addWidget(self.algorithmes_menu)
        self.interface_principale.addWidget(self.heuristiques_menu)

        box_middleUi = QtWidgets.QGridLayout()                  # Layout de l'interface principale
        box_middleUi.addWidget(self.interface_principale)

        box_middleUi.setContentsMargins(0, 0, 0, 0)
        box_middleUi.setSpacing(0)

        self.setLayout(box_middleUi)

        self.setFrameShape(QFrame.NoFrame)

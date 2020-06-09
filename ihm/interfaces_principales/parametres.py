from PySide2 import QtWidgets, QtCore
from copy import deepcopy, copy
import global_module

class Parametres(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        algo_label = QtWidgets.QLabel("Algorithme : ")
        algo_label.setFixedHeight(50)
        heur_label = QtWidgets.QLabel("Heuristique : ")
        heur_label.setFixedHeight(50)

        # Algo combo box
        self.selection_algo = QtWidgets.QComboBox(self)
        self.selection_algo.setObjectName("selection_algo")
        self.selection_algo.addItem("selectionner un algorithme")
        self.selection_algo.addItem("dpll")
        self.selection_algo.addItem("ennumeration")
        self.selection_algo.currentTextChanged.connect(self.combo_changed)
        self.selection_algo.setFixedWidth(200)

        # Heuristique combo box
        self.selection_heuristique = QtWidgets.QComboBox(self)
        self.selection_heuristique.setObjectName("selection_heuristique")
        self.selection_heuristique.setFixedWidth(200)

        # Plus algo
        self.plus_algo = QtWidgets.QPushButton()
        self.plus_algo.setObjectName("plus_algo")
        self.plus_algo.setFixedSize(50, 50)
        self.plus_algo.clicked.connect(self.ajout_algo)



        hbox = QtWidgets.QHBoxLayout()

        self.vbox_alg = QtWidgets.QVBoxLayout()
        frame_alg = QtWidgets.QFrame()

        self.vbox_heur = QtWidgets.QVBoxLayout()
        frame_heur = QtWidgets.QFrame()

        self.vbox_alg.addWidget(algo_label)
        self.vbox_alg.addWidget(self.selection_algo)
        self.vbox_alg.addWidget(self.plus_algo)
        self.vbox_alg.setSpacing(5)
        self.vbox_alg.setContentsMargins(20, 20, 20, 20)
        frame_alg.setLayout(self.vbox_alg)

        vbgauche = QtWidgets.QVBoxLayout()
        vbgauche.addWidget(frame_alg)
        vbgauche.addWidget(QtWidgets.QFrame())
        frame_gauche = QtWidgets.QFrame()
        frame_gauche.setLayout(vbgauche)

        self.vbox_heur.addWidget(heur_label)
        self.vbox_heur.addWidget(self.selection_heuristique)
        self.vbox_heur.setSpacing(5)
        self.vbox_heur.setContentsMargins(20, 20, 20, 20)
        frame_heur.setLayout(self.vbox_heur)

        vbdroite = QtWidgets.QVBoxLayout()
        vbdroite.addWidget(frame_heur)
        vbdroite.addWidget(QtWidgets.QFrame())
        frame_droite = QtWidgets.QFrame()
        frame_droite.setLayout(vbdroite)

        hbox.addWidget(frame_gauche)
        hbox.addWidget(frame_droite)

        self.setLayout(hbox)

    def combo_changed(self):
        global algorithmes
        print(self.selection_algo.currentText())
        global_module.algorithmes.append(self.selection_algo.currentText())

    def ajout_algo(self):
        self.vbox_alg.removeWidget(self.plus_algo)
        self.vbox_alg.addWidget(QtWidgets.QComboBox())
        self.vbox_alg.addWidget(self.plus_algo)

        self.vbox_heur.addWidget(QtWidgets.QComboBox())

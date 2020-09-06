from PySide2 import QtWidgets, QtCore
from copy import deepcopy, copy
import global_module

class Parametres(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        layout = QtWidgets.QVBoxLayout()

        dpll_frame = QtWidgets.QFrame()
        dpll_frame.setMaximumHeight(100)
        dpll_layout = QtWidgets.QHBoxLayout()

        self.dpll_check_box = QtWidgets.QCheckBox("DPLL")
        dpll_layout.addWidget(self.dpll_check_box)

        heuristiques_layout = QtWidgets.QVBoxLayout()
        heuristiques_frame = QtWidgets.QFrame()

        self.vsid_check_box = QtWidgets.QCheckBox("VSID")
        self.mocms_check_box = QtWidgets.QCheckBox("Maximum occurences in clause of minimun size")

        heuristiques_layout.addWidget(self.vsid_check_box)
        heuristiques_layout.addWidget(self.mocms_check_box)

        heuristiques_frame.setLayout(heuristiques_layout)
        dpll_layout.addWidget(heuristiques_frame)

        dpll_frame.setLayout(dpll_layout)

        valid_button = QtWidgets.QPushButton("Valider")
        valid_button.setObjectName("valid_button")
        valid_button.setMaximumSize(200, 50)
        valid_button.clicked.connect(self.validation)

        layout.addWidget(dpll_frame, QtCore.Qt.AlignTop)
        layout.addWidget(valid_button)

        self.setLayout(layout)

    def validation(self):
        global_module.algo_dico['dpll'] = self.dpll_check_box.isChecked()
        global_module.dpll_heur_dico['vsid'] = self.vsid_check_box.isChecked()
        global_module.dpll_heur_dico['mocms'] = self.mocms_check_box.isChecked()

        #global_module.dpll_graph.add_node(1, Niveau = 0, Rang = 0, Formule = global_module.formule)

        #global_module.wind.trameinf.frame_principale.affichage.creation()
        global_module.wind.trameinf.frame_principale.interface_principale.setCurrentWidget(global_module.wind.trameinf.frame_principale.affichage_frame)
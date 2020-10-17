from PySide2 import QtWidgets, QtCore
from copy import deepcopy, copy
import global_module

class Parametres(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        layout = QtWidgets.QVBoxLayout()

        #DPLL Frame
        dpll_frame = QtWidgets.QFrame()
        dpll_frame.setMaximumHeight(100)
        dpll_layout = QtWidgets.QHBoxLayout()

        self.dpll_check_box = QtWidgets.QCheckBox("DPLL")
        dpll_layout.addWidget(self.dpll_check_box)

        #heuristiques_layout = QtWidgets.QVBoxLayout()
        #heuristiques_frame = QtWidgets.QFrame()

        #self.vsid_dpll_check_box = QtWidgets.QCheckBox("VSID")
        #self.mocms_dpll_check_box = QtWidgets.QCheckBox("Maximum occurences in clause of minimun size")

        #heuristiques_layout.addWidget(self.vsid_dpll_check_box)
        #heuristiques_layout.addWidget(self.mocms_dpll_check_box)

        #heuristiques_frame.setLayout(heuristiques_layout)
        #dpll_layout.addWidget(heuristiques_frame)

        dpll_frame.setLayout(dpll_layout)

        #CDLC Frame
        cdcl_frame = QtWidgets.QFrame()
        cdcl_frame.setMaximumHeight(100)
        cdcl_layout = QtWidgets.QHBoxLayout()

        self.cdcl_check_box = QtWidgets.QCheckBox("CDCL")
        cdcl_layout.addWidget(self.cdcl_check_box)

        #heuristiques_layout = QtWidgets.QVBoxLayout()
        #heuristiques_frame = QtWidgets.QFrame()

        #self.vsid_cdcl_check_box = QtWidgets.QCheckBox("VSID")
        #self.mocms_cdcl_check_box = QtWidgets.QCheckBox("Maximum occurences in clause of minimun size")

        #heuristiques_layout.addWidget(self.vsid_cdcl_check_box)
        #heuristiques_layout.addWidget(self.mocms_cdcl_check_box)

        #heuristiques_frame.setLayout(heuristiques_layout)
        #cdcl_layout.addWidget(heuristiques_frame)

        cdcl_frame.setLayout(cdcl_layout)

        # Genetique Frame
        genetique_frame = QtWidgets.QFrame()
        genetique_frame.setMaximumHeight(100)
        genetique_layout = QtWidgets.QHBoxLayout()

        self.genetique_check_box = QtWidgets.QCheckBox("Algorithme Genetique")
        genetique_layout.addWidget(self.genetique_check_box)

        genetique_frame.setLayout(genetique_layout)


        valid_button = QtWidgets.QPushButton("Valider")
        valid_button.setObjectName("valid_button")
        valid_button.setMaximumSize(200, 50)
        valid_button.clicked.connect(self.validation)

        layout.addWidget(dpll_frame, QtCore.Qt.AlignTop)
        layout.addWidget(cdcl_frame, QtCore.Qt.AlignTop)
        layout.addWidget(genetique_frame, QtCore.Qt.AlignTop)
        layout.addWidget(valid_button)

        self.setLayout(layout)

    def validation(self):
        global_module.algo_dico['dpll'] = self.dpll_check_box.isChecked()
        #global_module.dpll_heur_dico['vsid'] = self.vsid_dpll_check_box.isChecked()
        #global_module.dpll_heur_dico['mocms'] = self.mocms_dpll_check_box.isChecked()

        global_module.algo_dico['cdcl'] = self.cdcl_check_box.isChecked()
        #global_module.cdcl_heur_dico['vsid'] = self.vsid_cdcl_check_box.isChecked()
        #global_module.cdcl_heur_dico['mocms'] = self.mocms_cdcl_check_box.isChecked()

        #global_module.dpll_graph.add_node(1, Niveau = 0, Rang = 0, Formule = global_module.formule)

        #global_module.wind.trameinf.frame_principale.affichage.creation()
        global_module.wind.trameinf.frame_principale.interface_principale.setCurrentWidget(global_module.wind.trameinf.frame_principale.affichage_frame)
import os

from PySide2 import QtWidgets, QtGui, QtCore

import global_module
from  instance_creation import *

class Home(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        layout = QtWidgets.QHBoxLayout()

        open_file_button = QtWidgets.QPushButton(self)
        open_file_button.setText("open a file")
        open_file_button.setObjectName("open_file_button")
        open_file_button.setFixedSize(200, 50)
        open_file_button.clicked.connect(self.openFile)
        layout.addWidget(open_file_button)

        saisir_une_formule_button = QtWidgets.QPushButton(self)
        saisir_une_formule_button.setText("saisir une formule")
        saisir_une_formule_button.setObjectName("saisir_une_formule_button")
        saisir_une_formule_button.setFixedSize(200, 50)
        saisir_une_formule_button.clicked.connect(self.saisir_une_formule)
        layout.addWidget(saisir_une_formule_button)

        self.setLayout(layout)

    def openFile(self):
        global formule

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "open file", "",  "formule file (*.cnf)")
        self.appelant.interface_principale.setCurrentWidget(self.appelant.parametres_menu)
        global_module.formule = Formule(fileName[0])
        #self.appelant.affichage.afficher(global_module.formule.__str__())

        """global_module.graph.add_node(None, Niveau=None, Rang=None, Formule=None, Propagation=None,
                                     decision=None)
        self.appelant.affichage.plot()"""
    def saisir_une_formule(self):

        formule = QtWidgets.QInputDialog.getText(self, "Saisie de la formule", "Formule")[0]

        #TRAITEMENT DE LA FORMULE SAISIE
        formule = formule.replace(') AND (', ' 0\n')
        formule = formule.replace('OR', ' ')
        formule = formule.replace('NOT', '-')
        formule = formule.replace('- ', '-')
        formule = formule.replace('(', '')
        formule = formule.replace(')', ' 0\n')
        formule = formule.replace('   ', ' ')

        litteraux = set()
        for lettre in formule:
            if lettre <= 'Z' and lettre >= 'A':
                litteraux.add(lettre)

        litteraux = list(litteraux)

        for litteral in litteraux:
            formule = formule.replace(litteral, str(litteraux.index(litteral)+1))


        print(formule)

        file = open('formule.cnf', 'w')
        file.write(formule)
        file.close()

        file = open('formule.cnf', 'r')

        self.appelant.interface_principale.setCurrentWidget(self.appelant.parametres_menu)
        global_module.formule = Formule(os.path.realpath(file.name))
        #self.appelant.affichage.afficher(global_module.formule.__str__())

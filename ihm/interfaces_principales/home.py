from PySide2 import QtWidgets, QtGui, QtCore

import global_module
from  instance_creation import *

class Home(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        open_file_button = QtWidgets.QPushButton(self)
        open_file_button.setText("open a file")
        open_file_button.setObjectName("open_file_button")
        open_file_button.setFixedSize(200, 50)
        open_file_button.move(100, 50)
        open_file_button.clicked.connect(self.openFile)

    def openFile(self):
        global formule

        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "open file", "",  "formule file (*.cnf)")
        self.appelant.interface_principale.setCurrentWidget(self.appelant.affichage_frame)
        global_module.formule = Formule(fileName[0])
        self.appelant.affichage.afficher(global_module.formule.__str__())



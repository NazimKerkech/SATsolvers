from PySide2 import QtWidgets

class PlHeur(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        self.selection_heuristique = QtWidgets.QComboBox(self)
        self.selection_heuristique.setObjectName("selection_heuristique")
        self.selection_heuristique.setFixedSize(200, 50)
        self.selection_heuristique.move(100, 50)


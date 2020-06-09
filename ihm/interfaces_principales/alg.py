from PySide2 import QtWidgets
import global_module

class PlAlg(QtWidgets.QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.appelant = appelant

        self.selection_algo = QtWidgets.QComboBox(self)
        self.selection_algo.setObjectName("selection_algo")
        self.selection_algo.setFixedSize(200, 50)
        self.selection_algo.move(100, 50)

        self.selection_algo.addItem("dpll")
        self.selection_algo.addItem("ennumeration")

        self.selection_algo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        global algorithmes
        print(self.selection_algo.currentText())
        global_module.algorithmes.append(self.selection_algo.currentText())
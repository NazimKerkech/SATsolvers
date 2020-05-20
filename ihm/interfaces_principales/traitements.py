from PySide2.QtWidgets import QGraphicsView, QGraphicsScene


class Traitements(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        """self.vbox = QtWidgets.QVBoxLayout()

        self.vbox.addWidget(QLabel("Procession : "))
        self.setLayout(self.vbox)"""

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

    def afficher(self, formule):
        self.scene.addText(formule.__str__())

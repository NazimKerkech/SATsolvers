from PySide2 import QtGui
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout


class Traitements(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        """self.vbox = QtWidgets.QVBoxLayout()

        self.vbox.addWidget(QLabel("Procession : "))
        self.setLayout(self.vbox)"""
        """
        self.scene = QGraphicsScene()
        self.setScene(self.scene)"""
        self.text = QTextBrowser()
        self.text.setLineWrapMode(QTextBrowser.NoWrap)

        self.sdp = QTextBrowser()
        self.sdp.setMaximumHeight(150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.text)
        vbox.addWidget(self.sdp)

        self.setLayout(vbox)

    def afficher(self, formule):
        self.text.append(formule.__str__()+"\n\n")

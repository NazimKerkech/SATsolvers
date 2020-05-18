from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QFrame
from PySide2.QtGui import QIcon, QPixmap, QFont
from middleui import MiddleUi
import sys

class BottomUi(QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Barre laterale
        vbox_barreLater = QtWidgets.QVBoxLayout()

        vbox_barreLater.setContentsMargins(0, 0, 0, 0)          # Configuration du layout
        vbox_barreLater.setSpacing(0)

        self.barreLater_frame = QFrame()                             # Enrobage de la barre laterale dans une frame
        self.barreLater_frame.setLayout(vbox_barreLater)
        self.barreLater_frame.setFrameShape(QFrame.Box)

        self.barreLater_frame.setMaximumSize(65, 1700)
        self.barreLater_frame.setMinimumSize(65, 0)

        # Partie principale
        frame_principale = MiddleUi(self)
        frame_principale.setFrameShape(QFrame.Box)

        # Grip
        label_credits = QtWidgets.QLabel()
        label_credits.setText("Moi")
        label_version = QtWidgets.QLabel()
        label_version.setText("Version : 0.1")

        hbox_grip = QtWidgets.QHBoxLayout()
        hbox_grip.setContentsMargins(0, 0, 0, 0)                # Configuration du layout

        hbox_grip.addWidget(label_credits)
        hbox_grip.addWidget(label_version)

        grip_frame = QFrame()                                   # Enrobage de la grip dans une frame
        grip_frame.setLayout(hbox_grip)
        grip_frame.setMaximumSize(1700, 20)
        grip_frame.setFrameShape(QFrame.Box)

        # Unification de la partie centrale (partie principale + grip)
        vbox_centre = QtWidgets.QVBoxLayout()
        vbox_centre.addWidget(frame_principale)
        vbox_centre.addWidget(grip_frame)

        vbox_centre.setContentsMargins(0, 0, 0, 0)              # Configuration du layout
        vbox_centre.setSpacing(0)

        centre_frame = QFrame()                                 # Enrobage dans une frame
        centre_frame.setLayout(vbox_centre)

        centre_frame.setFrameShape(QFrame.Box)

        # Unification
        hbox_bottom = QtWidgets.QHBoxLayout()

        hbox_bottom.addWidget(self.barreLater_frame)
        hbox_bottom.addWidget(centre_frame)

        hbox_bottom.setContentsMargins(0, 0, 0, 0)              # Configuration du layout
        hbox_bottom.setSpacing(0)

        self.setLayout(hbox_bottom)
        self.setFrameShape(QFrame.Box)
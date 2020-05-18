import PySide2
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QToolTip, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QFrame, QSizePolicy
from PySide2.QtGui import QIcon, QPixmap, QFont
import files_rc
import sys

class TopUi(QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Barres superieur
        vbox_barresSup = QtWidgets.QVBoxLayout()

        barrePrincipale = QFrame()                              # Barre principale barre du titre

        hbox_title = QtWidgets.QHBoxLayout()                    # Bouttons

        hbox_title.setContentsMargins(0, 0, 0, 0)               # Configuration du layout
        vbox_barresSup.setSpacing(0)

        barrePrincipale.setLayout(hbox_title)
        vbox_barresSup.addWidget(barrePrincipale)

        barreDActions = QFrame()                                # Barre des actions
        barreDActions.setMinimumHeight(30)
        vbox_barresSup.addWidget(barreDActions)

        vbox_barresSup.setContentsMargins(0, 0, 0, 0)           # Configuration du layout
        vbox_barresSup.setSpacing(0)

        frame_barresSup = QFrame()                              # Enrobage dans une frame
        frame_barresSup.setObjectName("frame_barresSup")
        frame_barresSup.setLayout(vbox_barresSup)

        # Controle du menu
        button_toggle_menu = QPushButton()
        button_toggle_menu.setObjectName("button_toggle_menu")

        button_toggle_menu.clicked.connect(lambda: self.toggleMenu(250))

        button_toggle_menu.setSizePolicy(sizePolicy)
        sizePolicy.setHeightForWidth(button_toggle_menu.sizePolicy().hasHeightForWidth())

        box_toggle_menu = QtWidgets.QGridLayout()               # Enrobage du boutton dans une box
        box_toggle_menu.addWidget(button_toggle_menu)

        box_toggle_menu.setContentsMargins(0, 0, 0, 0)          # Configuration du layout
        box_toggle_menu.setSpacing(0)

        frame_toggle_menu = QFrame()                            # Enrobage du boutton dans une frame
        frame_toggle_menu.setLayout(box_toggle_menu)

        frame_toggle_menu.setMinimumSize(QtCore.QSize(0, 0))
        frame_toggle_menu.setMaximumSize(QtCore.QSize(65, 65))
        frame_toggle_menu.setFrameShape(QFrame.Box)

        # Unification
        frame_barresSup.setFrameShape(QFrame.Box)
        hbox_uiSup = QtWidgets.QHBoxLayout()
        hbox_uiSup.addWidget(frame_toggle_menu)
        hbox_uiSup.addWidget(frame_barresSup)

        hbox_uiSup.setContentsMargins(0, 0, 0, 0)               # Configuration du layout unifié
        hbox_uiSup.setSpacing(0)

        self.setFrameShape(QFrame.Box)

        self.setLayout(hbox_uiSup)

        self.setMinimumSize(QtCore.QSize(0, 100))

    def toggleMenu(self, maxWidth):
        width = self.parent().trameinf.barreLater_frame.width()
        maxExtend = maxWidth
        standard = 70

        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        self.animation = QtCore.QPropertyAnimation(self.parent().trameinf.barreLater_frame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
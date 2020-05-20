from PySide2 import QtWidgets
from PySide2.QtWidgets import QPushButton, QFrame
from ihm.middleui import MiddleUi


class BottomUi(QFrame):
    def __init__(self, parent, appelant):
        super().__init__(parent)

        self.mainWindow = appelant

        # Barre laterale
        vbox_barreLater = QtWidgets.QVBoxLayout()

        vbox_barreLater.setContentsMargins(0, 0, 0, 0)          # Configuration du layout
        vbox_barreLater.setSpacing(0)

        bouton_box = QtWidgets.QVBoxLayout()
        bouton_box.setContentsMargins(0, 0, 0, 0)
        bouton_box.setSpacing(0)

        button_frame = QFrame()

        # Bouttons
        self.home_button = QPushButton()                                     # Home
        self.home_button.setObjectName("home_button")
        self.home_button.setMaximumHeight(70)
        self.home_button.clicked.connect(self.go_to_home)
        bouton_box.addWidget(self.home_button)

        self.affichage_principal = QPushButton()                                     # Show
        self.affichage_principal.setObjectName("affichage_principal")
        self.affichage_principal.setMaximumHeight(70)
        self.affichage_principal.clicked.connect(self.aller_a_affichage_principal)
        bouton_box.addWidget(self.affichage_principal)

        self.algorithmes = QPushButton()                               # Algorithmes
        self.algorithmes.setObjectName("algorithmes")
        self.algorithmes.setMinimumHeight(70)
        self.algorithmes.clicked.connect(self.aller_a_algorithmes)
        bouton_box.addWidget(self.algorithmes)

        self.heuristiques = QPushButton()                                # Heuristiques
        self.heuristiques.setObjectName("heuristiques")
        self.heuristiques.setMinimumHeight(70)
        self.heuristiques.clicked.connect(self.aller_a_heuristiques)
        bouton_box.addWidget(self.heuristiques)

        button_frame.setLayout(bouton_box)
        button_frame.setMaximumHeight(280)

        button_frame_complementaire = QFrame()

        vbox_barreLater.addWidget(button_frame)
        vbox_barreLater.addWidget(button_frame_complementaire)

        self.barreLater_frame = QFrame()                             # Enrobage de la barre laterale dans une frame
        self.barreLater_frame.setFrameShape(QFrame.NoFrame)
        self.barreLater_frame.setLayout(vbox_barreLater)

        self.barreLater_frame.setMaximumSize(70, 1700)
        self.barreLater_frame.setMinimumSize(70, 0)

        # Partie principale
        self.frame_principale = MiddleUi(self, self)

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
        grip_frame.setFrameShape(QFrame.NoFrame)

        # Unification de la partie centrale (partie principale + grip)
        vbox_centre = QtWidgets.QVBoxLayout()
        vbox_centre.addWidget(self.frame_principale)
        vbox_centre.addWidget(grip_frame)

        vbox_centre.setContentsMargins(0, 0, 0, 0)              # Configuration du layout
        vbox_centre.setSpacing(0)

        centre_frame = QFrame()                                 # Enrobage dans une frame
        centre_frame.setLayout(vbox_centre)

        centre_frame.setFrameShape(QFrame.NoFrame)

        # Unification
        hbox_bottom = QtWidgets.QHBoxLayout()

        hbox_bottom.addWidget(self.barreLater_frame)
        hbox_bottom.addWidget(centre_frame)

        hbox_bottom.setContentsMargins(0, 0, 0, 0)              # Configuration du layout
        hbox_bottom.setSpacing(0)

        self.setLayout(hbox_bottom)

        self.setFrameShape(QFrame.NoFrame)

    def go_to_home(self):
        if self.frame_principale.interface_principale.currentWidget() != self.frame_principale.home:
            self.frame_principale.interface_principale.setCurrentWidget(self.frame_principale.home)

    def aller_a_affichage_principal(self):
        if self.frame_principale.interface_principale.currentWidget() != self.frame_principale.affichage_frame:
            self.frame_principale.interface_principale.setCurrentWidget(self.frame_principale.affichage_frame)

    def aller_a_algorithmes(self):
        if self.frame_principale.interface_principale.currentWidget() != self.frame_principale.algorithmes_menu:
            self.frame_principale.interface_principale.setCurrentWidget(self.frame_principale.algorithmes_menu)

    def aller_a_heuristiques(self):
        if self.frame_principale.interface_principale.currentWidget() != self.frame_principale.heuristiques_menu:
            self.frame_principale.interface_principale.setCurrentWidget(self.frame_principale.heuristiques_menu)
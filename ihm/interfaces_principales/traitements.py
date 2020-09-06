import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout
from PySide2.QtCore import QFile, QObject, Signal, Slot, QTimer
from PySide2.QtUiTools import QUiLoader
import networkx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from ihm.interfaces_principales.traitements_directory.dpll_traitement import Dpll_traitements
import networkx as nx
import matplotlib.pyplot as plt
from grave import plot_network
from grave.style import use_attributes

import global_module

import random

class Traitements(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

    def creation(self):
        if global_module.algo_dico['dpll']:
            if global_module.dpll_heur_dico['vsid']:
                self.dpll_vsid_frame = Dpll_traitements(heuristique='vsid')
                self.layout.addWidget(self.dpll_vsid_frame)
                self.layout = QtWidgets.QHBoxLayout()

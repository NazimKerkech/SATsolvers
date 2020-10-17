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

from ihm.interfaces_principales.traitements_directory.cdcl_traitement import Cdcl_traitements
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
            self.dpll_frame = Dpll_traitements(algorithme='dpll', heuristique='vsid')
            self.layout.addWidget(self.dpll_frame)
            #self.layout = QtWidgets.QHBoxLayout()

        if global_module.algo_dico['cdcl']:
            self.cdcl_frame = Cdcl_traitements(algorithme='cdcl', heuristique='vsid')
            self.layout.addWidget(self.cdcl_frame)
            #self.layout = QtWidgets.QHBoxLayout()
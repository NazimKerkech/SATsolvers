import networkx
import matplotlib.pyplot
from grave import plot_network
from grave.style import use_attributes


sdp = []
niveau_actuel = -1
formule = None
algorithmes = []
heuristiques = []
wind = None
dpll_graph = networkx.DiGraph()
cdcl_graph = networkx.DiGraph()
#fig, ax = matplotlib.pyplot.subplots()

algo_dico = {'dpll': False, 'cdcl': False, 'genetique': False}

#dpll_heur_dico = {'vsid': False, 'mocms': False}

#cdcl_heur_dico = {'vsid': False, 'mocms': False}
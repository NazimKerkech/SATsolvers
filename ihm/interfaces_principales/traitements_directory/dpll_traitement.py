import sys
from PySide2 import  QtCore,QtGui, QtWidgets, QtWebEngineWidgets
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout
from PySide2.QtCore import QFile, QObject, Signal, Slot, QTimer
from PySide2.QtUiTools import QUiLoader
import networkx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import inspect
import networkx as nx
import matplotlib.pyplot as plt
from grave import plot_network
from grave.style import use_attributes

from networkx.drawing.nx_agraph import write_dot, graphviz_layout

import global_module
import plotly.graph_objects as go

import random

class Dpll_traitements(QFrame):
    def __init__(self, heuristique, parent=None):
        super().__init__(parent)

        self.heuristique = heuristique

        self.layout = QtWidgets.QVBoxLayout()

        self.graph = DPLLMatplotlibWidget(self.heuristique)
        self.infos = Infos_frame()

        self.layout.addWidget(self.graph)
        self.layout.addWidget(self.infos)

        self.setLayout(self.layout)


class Infos_frame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        frame_formule = QFrame()
        layout_formule = QtWidgets.QHBoxLayout()
        f_label = QtWidgets.QLabel("Formule : ")
        self.formule_label = QtWidgets.QTextBrowser()
        layout_formule.addWidget(f_label)
        layout_formule.addWidget(self.formule_label)
        frame_formule.setLayout(layout_formule)

        frame_propagation = QFrame()
        layout_propagation = QtWidgets.QHBoxLayout()
        p_label = QtWidgets.QLabel("Sequence de propagation :")
        self.propagation_label = QtWidgets.QLabel()
        layout_propagation.addWidget(p_label)
        layout_propagation.addWidget(self.propagation_label)
        frame_propagation.setLayout(layout_propagation)

        frame_niveau = QFrame()
        layout_niveau = QtWidgets.QHBoxLayout()
        n_label = QtWidgets.QLabel("Niveau :")
        self.niveau_label = QtWidgets.QLabel()
        layout_niveau.addWidget(n_label)
        layout_niveau.addWidget(self.niveau_label)
        frame_niveau.setLayout(layout_niveau)

        frame_decision = QFrame()
        layout_decision = QtWidgets.QHBoxLayout()
        d_label = QtWidgets.QLabel("Decision :")
        self.decision_label = QtWidgets.QLabel()
        layout_decision.addWidget(d_label)
        layout_decision.addWidget(self.decision_label)
        frame_decision.setLayout(layout_decision)

        layout.addWidget(frame_niveau)
        layout.addWidget(frame_formule)
        layout.addWidget(frame_propagation)
        layout.addWidget(frame_decision)

        self.setLayout(layout)

class DPLLMatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, h, parent=None):
        super().__init__(parent)
        #Graphe

        self.fig, self.ax = plt.subplots()
        #nx.draw(global_module.dpll_graph, nx.get_node_attributes(global_module.dpll_graph, 'position'), with_labels=True, arrows=True)
        self.art = plot_network(global_module.dpll_graph,
                        layout=lambda x: nx.get_node_attributes(global_module.dpll_graph, 'position'),
                        ax=self.ax,
                        node_style=use_attributes(),
                        edge_style=use_attributes())

        self.art.draw
        self.art.set_picker(10)

        self.canvas = FigureCanvas(self.fig)

        self.toolbar = NavigationToolbar(self.canvas, self)


        #pos = graphviz_layout(global_module.dpll_graph, prog='dot')
        self.fig.canvas.mpl_connect('pick_event', hilighter)

        lay = QVBoxLayout(self)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)
        """

        Xe = []
        Ye = []
        Xn = [result[1] for result in networkx.get_node_attributes(global_module.dpll_graph, 'x').items()]
        Yn = [result[1] for result in networkx.get_node_attributes(global_module.dpll_graph, 'y').items()]

        for edge in global_module.dpll_graph.edges:
            Xe+=[networkx.get_node_attributes(global_module.dpll_graph, 'x')[edge[0]], networkx.get_node_attributes(global_module.dpll_graph, 'x')[edge[1]]]
            Ye+=[networkx.get_node_attributes(global_module.dpll_graph, 'y')[edge[0]], networkx.get_node_attributes(global_module.dpll_graph, 'y')[edge[1]]]

        print(Xe)
        print(Ye)
        print(Xn)
        print(Yn)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                                 y=Ye,
                                 mode='lines',
                                 line=dict(color='rgb(210,210,210)', width=1),
                                 hoverinfo='none'
                                 ))
        fig.add_trace(go.Scatter(x=Xn,
                                 y=Yn,
                                 mode='markers',
                                 name='bla',
                                 marker=dict(symbol='circle-dot',
                                             size=18,
                                             color='#6175c1',  # '#DB4551',
                                             line=dict(color='rgb(50,50,50)', width=1)
                                             ),
                                 hoverinfo='text',
                                 opacity=0.8
                                 ))
        axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                    zeroline=False,
                    showgrid=False,
                    showticklabels=False,
                    )

        fig.update_layout(title='Tree with Reingold-Tilford Layout',
                          font_size=12,
                          showlegend=False,
                          xaxis=axis,
                          yaxis=axis,
                          margin=dict(l=40, r=40, b=85, t=100),
                          hovermode='closest',
                          plot_bgcolor='rgb(248,248,248)'
                          )
        # we create html code of the figure
        html = '<html><body>'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        print(inspect.getfullargspec(QtWebEngineWidgets.QWebEngineView.setHtml))

        print(html)
        self.setContent(html='<h1>Blank Tab</h1><p>It is a blank tab!</p>', mimeType="text/html;charset=UTF-8", baseUrl=QtCore.QUrl('about:blank'))
        """
        @Slot(list)
        def update_plot(self):
            self.art = plot_network(global_module.dpll_graph, ax=self.ax)
            self.canvas = FigureCanvas(self.fig)
            self.canvas.draw()
            plt.show()
            """self.line.set_data(range(len(data)), data)

            self.ax.set_xlim(0, len(data))
            self.ax.set_ylim(min(data), max(data))
            self.canvas.draw()"""


def hilighter(event):
    # if we did not hit a node, bail
    if not hasattr(event, 'nodes') or not event.nodes:
        return
    print("here")
    # pull out the graph,
    global_module.dpll_graph = event.artist.graph

    # clear any non-default color on nodes
    for node, attributes in global_module.dpll_graph.nodes.data():
        attributes.pop('color', None)

    for u, v, attributes in global_module.dpll_graph.edges.data():
        attributes.pop('width', None)

    for node in event.nodes:
        global_module.dpll_graph.nodes[node]['color'] = 'C1'

        for edge_attribute in global_module.dpll_graph[node].values():
            edge_attribute['width'] = 3

    # update the screen
    event.artist.stale = True
    event.artist.figure.canvas.draw_idle()

    noeud = event.nodes[0]

    formule = networkx.get_node_attributes(global_module.dpll_graph, 'Formule')[noeud]
    propagation = networkx.get_node_attributes(global_module.dpll_graph, 'Propagation')[noeud]
    decision = networkx.get_node_attributes(global_module.dpll_graph, 'decision')[noeud]
    niveau = networkx.get_node_attributes(global_module.dpll_graph, 'Niveau')[noeud]

    global_module.wind.trameinf.frame_principale.affichage.dpll_vsid_frame.infos.formule_label.clear()
    global_module.wind.trameinf.frame_principale.affichage.dpll_vsid_frame.infos.formule_label.append(formule.__str__())
    global_module.wind.trameinf.frame_principale.affichage.dpll_vsid_frame.infos.propagation_label.setText(propagation.__str__())
    global_module.wind.trameinf.frame_principale.affichage.dpll_vsid_frame.infos.niveau_label.setText(niveau.__str__())
    global_module.wind.trameinf.frame_principale.affichage.dpll_vsid_frame.infos.decision_label.setText(decision.__str__())
from copy import deepcopy
import instance_creation
import algorithmes.resolution.propagation_unitaire as pu
import global_module


def dpll(f, niveau=0, rang=0):
    global formule
    global sdp                          # sdp est la sequence de decisio-propagation faite par l'algorithme

    #global_module.wind.trameinf.frame_principale.affichage.afficher(f.__str__())

    g = pu.propoagation_unitaire(f)     # Execution de la propagation unitaire
    global_module.sdp.append(g)         # Mise a jour de la SD-P apres la propagation de contraintes

    l = f.atm.index(max(f.atm)) + 1     # HEURISTIQUE : selection_algo de l'atome le plus occurent
    if f.atm_neg[l - 1] > f.atm_pos[l - 1]:
        l = -l

    global_module.dpll_graph.add_node(2**niveau + rang, Niveau=niveau, Rang=rang, Formule=f, Propagation=g,
                                      decision=l,
                                      position=((-2**(niveau-1) + rang + 0.5)*2**(4-niveau), -niveau))
    if niveau:
        print(niveau, rang)
        d = global_module.dpll_graph.nodes[2**(niveau-1) + ((rang- (rang%2))/2)]['decision']
        pater = 2**(niveau-1) + ((rang- (rang%2))/2)
        soit = 2 ** niveau + rang
        global_module.dpll_graph.add_edge(pater, soit, decision = (-2*(rang % 2) + 1) * d)

    #global_module.wind.trameinf.frame_principale.affichage.graph.initialiserGraph(global_module.graph)

    #global_module.wind.trameinf.frame_principale.affichage.graph.update_plot()
    #decision = (l,)

    if len(f.clauses) == 0:             # Verrification -triviale de la satisfiabilité de la formule obtenue aprés la PU
        return True
    for c in f.clauses:
        if len(c.litteraux) == 0:
            return False

    #global_module.sdp.append(decision)  # Mise a jour de la SD-P apres une decision

    #
    f1 = deepcopy(f)
    f1.clauses |= {instance_creation.Clause({l})}
    f2 = deepcopy(f)
    f2.clauses |= {instance_creation.Clause({-l})}

    return dpll(f1, niveau+1, 2*rang) or dpll(f2, niveau+1, 2*rang+1)

from copy import deepcopy
import instance_creation
import algorithmes.resolution.propagation_unitaire as pu
import global_module


def dpll(f, wind):
    global formule
    global sdp                          # sdp est la sequence de decisio-propagation faite par l'algorithme

    wind.trameinf.frame_principale.affichage.afficher(f.__str__())

    g = pu.propoagation_unitaire(f)     # Execution de la propagation unitaire
    global_module.sdp.append(g)         # Mise a jour de la SD-P apres la propagation de contraintes

    if len(f.clauses) == 0:             # Verrification -triviale de la satisfiabilité de la formule obtenue aprés la PU
        return True
    for c in f.clauses:
        if len(c.litteraux) == 0:
            return False

    l = f.atm.index(max(f.atm)) + 1     # HEURISTIQUE : selection_algo de l'atome le plus occurent
    if f.atm_neg[l - 1] > f.atm_pos[l - 1]:
        l = -l

    decision = (l,)

    global_module.sdp.append(decision)  # Mise a jour de la SD-P apres une decision

    #
    f1 = deepcopy(f)
    f1.clauses |= {instance_creation.Clause({l})}
    f2 = deepcopy(f)
    f2.clauses |= {instance_creation.Clause({-l})}

    return dpll(f1, wind) or dpll(f2, wind)
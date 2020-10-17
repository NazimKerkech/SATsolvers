import os
from instance_creation import Formule
from algorithmes.resolution.cdcl_SN3.fun import *
import global_module
import timeit

def cdcl(formule):
    back_tracking = False
    clauses_apprises = set()
    interpretation_partielle = set()
    niveau_de_decision = 0

    fun = Fun()
    fun.create_watch_list(formule)
    global_module.cdcl_graph.add_node(1, Niveau=0, Rang=0, Formule=formule,
                                      decision=0,
                                      position=(0, 0))
    while True:
        """print('\n' + '#' * 50 + '\n')
        print("sequence de decision : ", fun.sequence_de_decision, " niveau de decision : ", niveau_de_decision)
        print("sequence des sequences de propagation : ", fun.sequence_des_sequences_de_propagation)
        print("interpretation partielle : ", interpretation_partielle)
        print("garphe d'implications : ", fun.graphe_d_implication.nodes)"""
        clause_conflit, sequence_de_propagation = fun.pu(formule, clauses_apprises, interpretation_partielle)
        #print(niveau_de_decision, global_module.cdcl_graph.nodes)

        global_module.cdcl_graph.nodes[2**fun.pater[0] + fun.pater[1]]['Propagation'] = sequence_de_propagation

        if clause_conflit == None:
            interpretation_partielle |= set(sequence_de_propagation)
            if len(interpretation_partielle) == formule.nb_atomes:
                return True

            decision = fun.heuristique_de_branchement(formule, clauses_apprises, interpretation_partielle, niveau_de_decision)
            niveau_de_decision += 1
            interpretation_partielle.add(decision)

        else:
            #print("conflit")
            if niveau_de_decision == 0:
                return False

            nogood, niveau_de_decision = fun.analyse_de_conflit(formule, clauses_apprises, interpretation_partielle, clause_conflit)
            clauses_apprises |= {nogood}
            #print("clause apprise : ", nogood)

            interpretation_partielle, clauses_apprises = fun.retour_arriere(formule, clauses_apprises, interpretation_partielle, niveau_de_decision)
            fun.add_clause_to_watch_list(nogood, interpretation_partielle)


def main(nom_fichier):

    file = open(nom_fichier, 'r')
    formule = Formule(os.path.realpath(file.name))

    truc = cdcl(formule)
    print(truc)
    file.close()
    return truc

if __name__ == '__main__':
    t = timeit.Timer(stmt="main(\"/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000/uf50-011.cnf\")",
                     globals=globals())
    print(t.timeit(1))
    main("/home/thedoctor/Documents/Python/PycharmProjects/SN2/UF50-218-1000/uf50-011.cnf")

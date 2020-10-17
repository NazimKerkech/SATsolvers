import copy
import sys
from random import random, choice, randint

import networkx

import global_module
from instance_creation import Clause

class Fun:
    def __init__(self):
        self.sauter_une_decision = False
        self.graphe_d_implication = networkx.DiGraph()
        self.def_clause_vers_litteraux = {}
        self.def_litteal_vers_clauses = []
        self.sequence_de_decision = []
        self.sequence_des_sequences_de_propagation = []
        self.litt_compteur = []
        self.memento = None
        self.pater = (0, 0)
        self.memsuiv = False

    def heuristique_de_branchement(self, formule, clauses_apprises, interpretation_partielle, niveau_de_decision):
        if self.memento != None:
            result = self.memento
            self.memento = None
            self.memsuiv = True
            filus = self.pater
        else:
            while True:
                decision = randint(1, formule.nb_atomes)
                if decision in interpretation_partielle or -decision in interpretation_partielle:
                    continue
                else:
                    polarisation = choice([1, -1])
                    result = polarisation * decision
                    break

            if self.memsuiv:  # deviation
                filus = (self.pater[0] + 1, 2 * self.pater[1] + 1)
                self.memsuiv = False
            else:  # continuation du chemain droit
                filus = (self.pater[0] + 1, 2 * self.pater[1])

        self.sequence_de_decision.append(result)
        self.graphe_d_implication.add_node(result, niveau=len(self.sequence_de_decision),
                                           raison=Clause(set()), explication=set())



        global_module.cdcl_graph.add_node(2**filus[0] + filus[1], Niveau=filus[0], Rang=filus[1], Formule=formule,
                                      decision=result,
                                      position=((-2**(filus[0]-1) + filus[1] + 0.5)*2**(4-filus[0]), -filus[0]))
        global_module.cdcl_graph.add_edge(2**self.pater[0] + self.pater[1], 2**filus[0] + filus[1], decision=result)
        self.pater = filus
        return result

    def pu(self, formule, clauses_apprises, interpretation_partielle):
        file = []
        sequence_de_propagation = []

        if len(self.sequence_de_decision) > len(self.sequence_des_sequences_de_propagation) >= 0:
            file += [self.sequence_de_decision[-1]]

        for clause in formule.clauses | clauses_apprises:
            if len(clause.litteraux) == 1:
                A = next(iter(clause.litteraux))
                if not A in interpretation_partielle:
                    file.append(A)
                    self.graphe_d_implication.add_node(A, niveau=len(self.sequence_de_decision),
                                                       raison=clause,
                                                       explication=set())
        sequence_de_propagation += file
        while len(file) > 0:
            #print("sequence de propagation : ", sequence_de_propagation)
            litteral_a_propager = file.pop()
            #print('litteral a propager : ', litteral_a_propager, " apparait dans ", len(self.def_litteal_vers_clauses[-litteral_a_propager]), " clauses")

            ensemble_des_clauses = copy.deepcopy(self.def_litteal_vers_clauses[-litteral_a_propager])
            for clause in ensemble_des_clauses:
                if len(clause.litteraux) == 1:
                    self.graphe_d_implication.add_node(next(iter(clause.litteraux)), niveau=len(self.sequence_de_decision),
                                                       raison=clause,
                                                       explication=set())
                    self.sequence_des_sequences_de_propagation.append(sequence_de_propagation)
                    return next(iter(clause.litteraux)), None

                A, B = (self.def_clause_vers_litteraux[clause][0], self.def_clause_vers_litteraux[clause][1]) if self.def_clause_vers_litteraux[clause][0] == -litteral_a_propager else (self.def_clause_vers_litteraux[clause][1], self.def_clause_vers_litteraux[clause][0])
                if not B in interpretation_partielle | set(sequence_de_propagation):
                    status, new_A, unit = self.check_status(clause, interpretation_partielle, sequence_de_propagation, A, B)
                    #print('clause : ', clause.litteraux, 'status : ', status, unit, ' A_precedent : ', A, ' B_precedent : ', B, 'A : ', new_A, 'B : ', B)

                    if status == "Satisfaite":
                        continue
                    elif status == "Non_Resolue":
                        self.def_litteal_vers_clauses[A].remove(clause)
                        self.def_litteal_vers_clauses[new_A].add(clause)
                        self.def_clause_vers_litteraux[clause].remove(A)
                        self.def_clause_vers_litteraux[clause].append(new_A)
                        continue
                    elif status == "Empty":
                        self.graphe_d_implication.add_node(A, niveau=len(self.sequence_de_decision),
                                                           raison=clause, explication=set([-x for x in clause.litteraux if x != A]))
                        self.sequence_des_sequences_de_propagation.append(sequence_de_propagation)
                        return A, None
                    elif status == "Unitaire":
                        file.append(unit)
                        sequence_de_propagation.append(unit)
                        self.graphe_d_implication.add_node(unit, niveau=len(self.sequence_de_decision),
                                                           raison=clause, explication=set([-x for x in clause.litteraux if x != unit]))
                        for x in self.graphe_d_implication.nodes[unit]['explication']:
                            if not x in self.graphe_d_implication.nodes:
                                #print("node not in graph", litteral_a_propager)
                                sys.exit()
                            self.graphe_d_implication.add_edge(x, unit, raison=clause)
                #else:
                    #print('*clause : ', clause.litteraux, ' status : SAT')

        if len(sequence_de_propagation) > 0:
            self.sequence_des_sequences_de_propagation.append(sequence_de_propagation)
        return None, sequence_de_propagation


    def analyse_de_conflit(self, formule, clauses_apprises, interpretation_partielle, litteral_conflit):
        R = [self.graphe_d_implication.nodes[litteral_conflit]['raison']]

        while len([x for x in R[-1].litteraux if self.graphe_d_implication.nodes[-x]['niveau'] == len(self.sequence_de_decision)]) > 1:

            l = choice([x for x in R[-1].litteraux if self.graphe_d_implication.nodes[-x]['niveau'] == len(self.sequence_de_decision) and self.graphe_d_implication.nodes[-x]['raison'] != Clause(set())])
            R.append(Clause((R[-1].litteraux - {l}) | (self.graphe_d_implication.nodes[-l]['raison'].litteraux - {-l})))
            #print("resolution ( ", abs(l),", ", R[-2], ", ", self.graphe_d_implication.nodes[-l]['raison'], ") = ", R[-1])


        n = [self.graphe_d_implication.nodes[-x]['niveau'] for x in R[-1].litteraux if self.graphe_d_implication.nodes[-x]['niveau'] != len(self.sequence_de_decision)]
        if len(n) == 0 or max(n) == 0:
            return R[-1], 0
        return R[-1], max(n) - 1

    def retour_arriere(self, formule, clauses_apprises, interpretation_partielle, niveau_de_decision):
        #Supression des tetes de piles
        self.memento = self.sequence_de_decision[niveau_de_decision]
        self.sequence_de_decision = self.sequence_de_decision[:niveau_de_decision]
        self.sequence_des_sequences_de_propagation = self.sequence_des_sequences_de_propagation[:niveau_de_decision]

        #Maj des SDD
        interpretation_partielle = set()
        interpretation_partielle |= set(self.sequence_de_decision)
        for seq_propag in self.sequence_des_sequences_de_propagation:
            interpretation_partielle |= set(seq_propag)

        #Maj du graph d'implications
        liste_des_noeuds = copy.deepcopy(self.graphe_d_implication.nodes)
        for node in liste_des_noeuds:
            if self.graphe_d_implication.nodes[node]['niveau'] > niveau_de_decision:
                self.graphe_d_implication.remove_node(node)

        #
        for clause in self.def_clause_vers_litteraux:
            if len(self.def_clause_vers_litteraux[clause]) == 1:
                self.add_clause_to_watch_list(clause, interpretation_partielle)

        self.pater = (niveau_de_decision, max([global_module.cdcl_graph.nodes[x]['Rang'] for x in global_module.cdcl_graph.nodes if global_module.cdcl_graph.nodes[x]['Niveau'] == niveau_de_decision]))
        """print("###Retour arriere vers le niveau", niveau_de_decision)
        print("## Nouvelle sequence de decision : ", self.sequence_de_decision)
        print("## Nouvelle sequence de propagation : ", self.sequence_des_sequences_de_propagation)
        print("## Nouvelle interpretation partielle : ", interpretation_partielle)"""

        return interpretation_partielle, clauses_apprises

    def check_status(self, clause_affectee, interpretation_partielle, file, A_precedent, B_precedent):
        liste_litt_non_affectes = []

        for litteral in clause_affectee.litteraux:
            if litteral in interpretation_partielle | set(file):
                return 'Satisfaite', A_precedent, 0
            if not (-litteral in interpretation_partielle | set(file)):
                liste_litt_non_affectes.append(litteral)

        if len(liste_litt_non_affectes) == 1:  # Clause unitaire
            return 'Unitaire', A_precedent, liste_litt_non_affectes.pop()

        if len(liste_litt_non_affectes) == 0:  # Clause vide
            return 'Empty', A_precedent, 0

        if len(liste_litt_non_affectes) > 1:  # Clause non resolue
            for a in liste_litt_non_affectes:
                if a != B_precedent:
                    return 'Non_Resolue', a, 0

    def create_watch_list(self, formule):
        self.def_clause_vers_litteraux = {}
        self.def_litteal_vers_clauses = []

        for i in range(-formule.nb_atomes, formule.nb_atomes + 1):
            self.def_litteal_vers_clauses.append(set())

        for clause in formule.clauses:
            litteraux_surveilles = []
            itteration = 0

            for litteral in clause.litteraux:

                if itteration == 0:
                    A = litteral
                    itteration += 1
                else:
                    B = litteral
                    break

            litteraux_surveilles.append(A)
            litteraux_surveilles.append(B)

            self.def_clause_vers_litteraux[clause] = litteraux_surveilles

            self.def_litteal_vers_clauses[A].add(clause)
            self.def_litteal_vers_clauses[B].add(clause)

    def add_clause_to_watch_list(self, clause, ip): # Ajouter une clause assertive apres un back track
        litteraux_surveilles = []
        itteration = 0

        for litteral in clause.litteraux:
            if not -litteral in ip:
                if itteration == 0:
                    A = litteral
                    itteration += 1
                else:
                    B = litteral
                    itteration += 1
                    break
        if itteration == 0:
            #print("probleme add_clause_to_watch_list")
            sys.exit()
        elif itteration == 1:   # Unitaire
            litteraux_surveilles.append(A)

            self.def_clause_vers_litteraux[clause] = litteraux_surveilles

            self.def_litteal_vers_clauses[A].add(clause)

        else:
            litteraux_surveilles.append(A)
            litteraux_surveilles.append(B)

            self.def_clause_vers_litteraux[clause] = litteraux_surveilles

            self.def_litteal_vers_clauses[A].add(clause)
            self.def_litteal_vers_clauses[B].add(clause)



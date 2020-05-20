class Valuation:
    valuations_vector = []

    def __init__(self, x):
        while x > 0:
            self.valuations_vector.insert(0, x % 2)
            x = int(x / 2)
        while len(self.valuations_vector) < 20:
            self.valuations_vector.append(0)


class Clause:
    litteraux = set()

    def __init__(self, x):
        self.litteraux = x

    def __str__(self):
        return self.litteraux.__str__()

    def __eq__(self, other):
        if len(self.litteraux ^ other.litteraux) == 0:
            return True
        return False

    def __hash__(self):
        list = []
        for lit in self.litteraux:
            list.append(lit)
        list.sort()
        return hash(tuple(list))

    def est_satisfaite_par(self, x):
        v = Valuation(x)
        for litteral in self.litteraux:
            if litteral < 0:
                litteral = litteral * (-1)
            if v.valuations_vector[litteral] == 1:
                return True
        return False


class Formule:
    clauses = set()
    nb_atomes = 0
    atm_pos = []
    atm_neg = []
    atm = []

    def __init__(self, x):
        if x != 0:
            self.clauses = self.instance_creation(x)
            self.remplissage_atomes()

    def __str__(self):
        d = ""
        for c in self.clauses:
            d = d + " " + c.__str__()
        return d

    # Cette methode consiste a affecter un litteral -a- a vrai
    def atome_decision(self, a):
        indx_a = abs(a) - 1

        liste_des_clauses = list(self.clauses)

        for clause in self.clauses:
            if a in clause.litteraux:  # Si a appartient a la clause alors elle est satisfaite
                liste_des_clauses.remove(clause)

            elif -a in clause.litteraux:  # Dans le cas contraire, si non a y appartient :
                clause.litteraux.remove(-a)

        self.clauses = set(liste_des_clauses)

        self.atm[indx_a] = 0
        self.atm_pos[indx_a] = 0
        self.atm_neg[indx_a] = 0
        self.nb_atomes -= 1

    def remplissage_atomes(self):
        # Calcul du nombre d'atomes
        atomes = set()
        for clause in self.clauses:
            for litteral in clause.litteraux:
                atomes.add(abs(litteral))

        self.nb_atomes = len(atomes)

        self.atm_pos = [0] * self.nb_atomes
        self.atm_neg = [0] * self.nb_atomes
        self.atm = [0] * self.nb_atomes

        # Calcul du nombre d'instance pour chaque litteral
        for c in self.clauses:
            for lo in c.litteraux:
                l = abs(lo) - 1
                if lo < 0:
                    self.atm_neg[abs(l)] += 1
                else:
                    self.atm_pos[l] += 1
        for i in range(self.nb_atomes):
            self.atm[i] = self.atm_neg[i] + self.atm_pos[i]

    # Lecture a partir d'un fichier
    @staticmethod
    def instance_creation(x):
        inst = open(x, 'r')
        clauses_set = set()
        for line in inst:
            clause = set()
            if ('0' < line[0] <= '9') or line[0] == '-':
                ligne = line.split()
                if ligne[-1] == '0':
                    ligne = ligne[:-1]
                for lit in ligne:
                    clause.add(int(lit))
                nova_clause = Clause(clause)
                clauses_set.add(nova_clause)
        return clauses_set

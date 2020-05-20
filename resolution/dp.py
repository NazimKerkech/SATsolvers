from copy import deepcopy

from instance_creation import *
from resolution.techniques_de_resolution import *


def dp(f):
    f_x = Formule(0)
    f_nx = Formule(0)
    fn = Formule(0)
    j = 0
    while len(f.clauses) != 0 and j < 50:
        f_x.clauses = set()
        f_nx.clauses = set()
        fn.clauses = set()
        # i = iter(iter(f.clauses).__next__().litteraux).__next__()
        print(f.atm)
        print(f.atm_pos)
        print(f.atm_neg)
        at = f.atm
        i = f.atm.index(min(f.atm))
        print(str(j) + " " + str(i) + " " + str(f.atm[i]))
        i = abs(i) + 1
        fbuff = deepcopy(f.clauses)

        for clause in f.clauses:
            if i in clause.litteraux and -i in clause.litteraux:
                fbuff.remove(clause)
            elif i in clause.litteraux:
                f_x.clauses.add(clause)
                fbuff.remove(clause)
            elif -i in clause.litteraux:
                f_nx.clauses.add(clause)
                fbuff.remove(clause)

        f.clauses = deepcopy(fbuff)

        for c1 in f_x.clauses:
            for c2 in f_nx.clauses:
                g = resolution(i, c1, c2)
                fn.clauses.add(g)

        print(fn)
        f.clauses = f.clauses | fn.clauses

        f.atome_elimination(i)

        for c in f.clauses:
            if len(c.litteraux) == 0:
                return False
        j = j + 1
    return True

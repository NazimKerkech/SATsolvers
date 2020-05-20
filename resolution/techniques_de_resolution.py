from copy import deepcopy

from instance_creation import Clause


def resolution(x, c1o, c2o):
    c1 = deepcopy(c1o)
    c2 = deepcopy(c2o)
    if x in c1.litteraux:
        c1.litteraux.remove(x)
        c2.litteraux.remove(-x)
    elif -x in c1.litteraux:
        c1.litteraux.remove(-x)
        c2.litteraux.remove(x)

    r = c1.litteraux | c2.litteraux
    res = Clause(r)

    return res


def resolvable(c1, c2):
    for lit1 in c1.litteraux:
        for lit2 in c2.litteraux:
            if lit1 == -lit2:
                return abs(lit1)
    return None


def subsumption(c1, c2):
    if c1.litteraux <= c2.litteraux:
        return c1
    elif c2.litteraux <= c1.litteraux:
        return c2
    else:
        return None

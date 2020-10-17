import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from pprint import pprint
import timeit

#La fonction cnfReader prend en entrée le fichier cnf et retourne la liste des clauses de l'instace du SAT
def cnfReader(file):
    a = [list(map(int, line.split("\n")[0].split()[:-1])) for line in file if line and\
                              not (line.startswith("c") or line.startswith("p"))]
    a = list(filter(None, a))
    return np.array(a)

#La fonction getSize prend en entrée le fichier .cnf et retourne le nombre de variables dans l'instance du SAT
def getSize(file):
    return int([line.split("\n")[0].split()[2:] for line in file if line.startswith("p")][0][0])

#La fonction createInstance crée une instance SAT à partir du fichier .cnf en retournant les clauses et le nombre de variables
def createInstance(file):
    f = open(file)
    a = cnfReader(f)
    f.seek(0) # se repositionner au début du fichier
    b = getSize(f)
    f.close()
    return a, b

#################################################################################################

# Cette fonction transforme une clause sous forme de CNF en un vecteur de bits
def transform_clause(clause, nbVar):
    transformed_clause = np.full(nbVar, -1)
    pos = clause[clause > 0] - 1
    neg = (clause[clause < 0] * -1) - 1
    transformed_clause[pos] = 1
    transformed_clause[neg] = 0
    return transformed_clause


# transformer l'instance à l'aide de transformer la clause
def transform_instance(instance, nbVar):
    return np.array(list(map(transform_clause, instance, [size] * len(instance))))

###################################################################################################

# générer une clause SAT en donnant le nombre de varaibles
def generate_caluse(nbVar):
    return np.random.choice([-1, 0, 1], nbVar)


# générer aléatoirement une instance SAT en donnant le nombre de clauses et le nombre de variables
def generate_instance(nbclauses, nbVar):
    return np.array([generate_caluse(nbVar) for i in range(nbclauses)])

#################################################################################################

# Cette fonction est utilisé par la méthode sort afin de décider ke criètre de tri (qui est ici la valeur de fitness)
def tri(sol):
    return sol[1]

# La fonction du fitness(solution) : pourcentage des clauses satisfaites par cette solution (résultat arrodi à 4 chiffres)
def fitness(instance, solution):
    return  ((instance == solution).sum(axis = 1)>0).sum()/len(instance)

# La fonction de selection utilise un échantillonnage de la roulette (roulle wheel)
# à chaque solution de
def selection(population, k):
    sumfit = sum([p[1] for p in population])
    selection_prob = [p[1]/sumfit for p in population]
    sel = np.random.choice(len(population), k, replace = False, p=selection_prob)
    s = [population[i] for i in sel]
    s.sort(reverse= True, key = tri)
    return s

#une fonction qui implemente un crossover simple (un seul point)
def simpleCrossover(parentA, parentB):
    x = np.random.choice(len(parentA))
    return np.concatenate((parentA[:x], parentB[x:]), axis=None)

#une fonction qui implemente un crossover simple (2 points)
def crossover2points(parentA, parentB):
    points = np.random.choice(len(parentA),2)
    points.sort()
    return np.concatenate((parentA[:points[0]], parentB[points[0]:points[1]], parentA[points[1]:]), axis = None)

#un fonction de mutation et mise à jour de fitness après la mutation
def mutation(x, instance):
    pt = np.random.choice(len(x))
    x[0][pt] = abs(x[0][pt]-1)
    x[1] = fitness(instance, x[0])

# une fonction qui génère une population de N solution, évalue chaque solution et trie l'ensemble par rapport au fitness
# la solution ayant  la plus grande valeur de fitness se trouve en premier
def generate_population(instance, N, nbVar):
    pop = []
    for i in range(N):
            sol = np.random.choice([0, 1], nbVar)
            fit = fitness(instance, sol)
            pop.append([sol, fit])
            #print(sol, ":",  fit)
    pop.sort(reverse= True, key = tri)
    return pop

###########################################################################

def genetic_algorithm(instance, nbVar, popSize=100, selectionRate=0.2, crossRate=0.5, mutRate=0.03, nbIter=10,
                      elitRate=0.01):
    # generer aléatoirement une population de popSize solutions
    pop = generate_population(instance, popSize, nbVar)
    best_sol = pop[0]  # comme la population est triée la meilleure solution est en premier
    for i in range(nbIter):
        elites = pop[:int(len(pop) * elitRate)]
        selected = selection(pop, int(len(pop) * selectionRate))
        matingPool = []

        for parentA in selected:
            cross = np.random.rand()
            if cross > crossRate:
                parentB = selected[np.random.choice(len(selected))]
                child = simpleCrossover(parentA[0], parentB[0])
                matingPool.append([child, fitness(instance, child)])

        offsprings = elites + matingPool
        for solution in offsprings:
            mta = np.random.rand()
            if mta > mutRate:
                mutation(solution, instance)

        pop = pop + offsprings
        pop.sort(reverse=True, key=tri)
        pop = pop[: popSize]
        best = pop[0]
        if best[1] > best_sol[1]:
            best_sol = best

    return best_sol

################################################################################
def main():
    nbVar = 50
    nbClauses = 218
    instance = generate_instance(nbClauses, nbVar)
    popSize = 10
    selectionRate = 0.003
    crossRate = 0.001
    mutRate = 0.001
    eliteRate = 0.001
    nbIter = 20
    gs = genetic_algorithm(instance, nbVar, popSize, selectionRate, crossRate, mutRate, nbIter, eliteRate)
    print(gs)

if __name__ == '__main__':
    t = timeit.Timer(stmt="main()", globals=globals())
    print(t.timeit(1000))
    main()
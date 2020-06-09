import instance_creation


def propoagation_unitaire(f):
    # Verification initiale que f contient au moins une clause unitaire
    seq_prop = ()
    b = True
    """for clause in f.clauses:
        if len(clause.litteraux) == 1:
            b = True
            break

    if not b:
        return 0"""

    # Tant qu'il existera une clause unitaire dans la formule
    # On continuera a appliquer itterativement la propagation unitaire
    while b:

        # On verifie s'il existe une clause unitaire

        b = False
        for clause in f.clauses:
            if len(clause.litteraux) == 1:  # On sort de la boucle pour traiter la premiere clause unitaire qu'on trouve
                b = True
                lit = clause.litteraux.pop()
                seq_prop += (lit,)
                clause.litteraux.add(lit)
                break

        # Propagation de la contrainte induite par la clause unitaire trouvee
        if b:
            f.atome_decision(lit)

    return seq_prop

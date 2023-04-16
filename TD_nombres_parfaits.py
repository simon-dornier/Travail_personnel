def somme(tab):
    """
    données : tab, de type list, est un tableau de valeurs
    résultat : la somme des éléments de tab
    """
    s = 0
    for i in range(0,len(tab)):
        s += tab[i]
    return s


def estparfait(n):
    """
    données : n, de type int
    résultat : True ou False selon si le nombre 
    """
    l = []
    for i in range(1,n):
        if n % i == 0:  #test si i est diviseur de n
            l.append(i)
    return somme(l) == n  #test si n est parfait

print(estparfait(28))

def sominvdiv(n):
    """
    données : n, de type int
    résultat : renvoie la somme des inverses des diviseurs de n
    """
    assert n > 0, "Il faut un entier naturel non nul"  #assertion 
    l = []
    for i in range(1,n):
        if n % i == 0:  #test si i est diviseur de n
            l.append(1/i)
    return somme(l)

print(sominvdiv(100))

def trouve_nb_parfait():
    """renvoie le seul nombre parfait à trois chiffres et la somme des inverses de ses diviseurs"""
    l = []
    for i in range(100,1000):
        if estparfait(i):
            nb_parfait = i
    return f"Le nombre à trouver est {nb_parfait} et la somme des inverses de ses diviseurs est {sominvdiv(nb_parfait)}"

print(trouve_nb_parfait())
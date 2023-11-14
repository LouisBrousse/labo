'''
Les opérations sur le laboratoire sans interactions avec l'utilisateur.
Pas de input, pas de print.
Backend.
Partie réutilisable entre les différentes IHM.
python labo_cmd.py add Xavier F305
'''

# Définir ce qu'est un laboratoire ? Quel type ?

# Réponse : dictionnaire, clé = personne, valeur = bureau

# Créations des exceptions
class PresentException(Exception):
    pass
class AbsentException(Exception):
    pass
class MemeBureauException(Exception):
    pass

# Les choix faits ici, ne devraient pas être utilisés à l'extérieur.


def laboratoire():
    return {}

def enregistrer_arrivee(labo, nom, bureau):
    if nom in labo:
        raise PresentException
    labo[nom] = bureau

def enregistrer_depart(labo, nom):
    if nom not in labo:
        raise AbsentException
    del labo[nom]

def est_presente(labo, nom):
    return nom in labo

def modifier_bureau(labo, nom, n_bureau):
    if nom not in labo:
        raise AbsentException
    if labo[nom] == n_bureau:
        raise MemeBureauException
    labo[nom] = n_bureau

def modifier_nom(labo, nom, n_nom):
    if nom not in labo:
        raise AbsentException
    bureau = labo.pop(nom)
    labo[n_nom] = bureau



# Les opérations qui permettent de manipuler les données du labo.

def main():
    print('test')

if __name__ == '__main__':
    main()

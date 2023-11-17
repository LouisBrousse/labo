'''
Les opérations sur le laboratoire sans interactions avec l'utilisateur.
Pas de input, pas de print.
Backend.
Partie réutilisable entre les différentes IHM.
python labo_cmd.py add Xavier F305
'''
import json
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

def bureau_occupe(labo, nom):
    return labo[nom]

def modifier_bureau(labo, nom, n_bureau):
    labo[nom] = n_bureau

def modifier_nom(labo, nom, n_nom):
    bureau = labo.pop(nom)
    labo[n_nom] = bureau

def lister_occupants(labo):
    liste_occupants = {}
    for occupant, bureau in labo.items():
        if occupant not in liste_occupants:
            liste_occupants[occupant] = [bureau]
        else:
            liste_occupants[occupant].append(bureau)

    return liste_occupants

def sauvegarde (labo, fichier_sauvegarde):
    fichier_sauvegarde="sauvegarde.txt"
    with open(fichier_sauvegarde,'w') as file:
        json.dump(labo, file)
    print("fichier sauvegardé!")
    
def lire_la_sauvegarde():
    


# Les opérations qui permettent de manipuler les données du labo.

def main():
    print('test')

if __name__ == '__main__':
    main()

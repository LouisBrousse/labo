from laboratoire import *
from menu import *

'''quitter = False
    labo = laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        print(labo)
        quitter = choix == 0
Interface sur la labo avec menu textuel.
'''

def gerer_arrivee(labo):
    try:
        nom = input("Nom ? ")
        bureau = input("Bureau ? ")
        enregistrer_arrivee(labo, nom, bureau)
    except PresentException as e:
        print(f"{e}: Impossible, déja là")

def gerer_depart(labo):
    try:
        nom = input("Nom ? ")
        enregistrer_depart(labo, nom)
    except AbsentException as e:
        print(f"{e}: Impossible, personne inconnue")

def gerer_modifier_bureau(labo):
    nom = input('Nom ?')
    n_bureau = input('Nouveau bureau?')
    modifier_bureau(labo, nom, n_bureau)
  

def gerer_modifier_nom(labo):
        nom = input("Nom ? ")
        n_nom = input("Nouveau nom?")
        reponse=est_presente(labo, nom)
        if reponse:
            modifier_nom(labo, nom, n_nom)
        else:
            'Nom inconnue'

def gerer_presence(labo):
    nom = input("Nom ? ")
    reponse = est_presente(labo, nom)
    print('Oui présent' if reponse else 'Nom inconnue')

def bureau_occupant(labo):
    nom = input("Nom ? ")
    reponse = est_presente(labo, nom )
    if reponse:
        reponse2 = bureau_occupe(labo, nom)
        print(f'Le bureau de {nom} est le {reponse2}')
    else:
        print('personne inconnue')

def liste_personnel(labo):
    for nom in labo:
        print(f'{nom} => {labo[nom]}')


def occupants_bureau(labo):
    occupants_par_bureau = lister_occupants(labo)
    for bureau, occupants in occupants_par_bureau.items():
        print (f'{bureau}:')
        for occupant in occupants:
            print(f'-{occupant}')



def main():
    labo = laboratoire()
    enregistrer_arrivee(labo, 'Louis', 'C310')
 
    mp = Menu()     # menu principal
    ajouter_entree(mp, 'Enregistrer une arrivée', gerer_arrivee, [labo])
    ajouter_entree(mp, 'Enregistrer un départ', gerer_depart, [labo])
    ajouter_entree(mp, 'Modifier un bureau', gerer_modifier_bureau, [labo])
    ajouter_entree(mp, 'Modifier un Nom', gerer_modifier_nom, [labo])
    ajouter_entree(mp, 'Présence d\'une personne', gerer_presence, [labo])
    ajouter_entree(mp, "Vérifier l'occupant d'un bureau", bureau_occupant, [labo])
    ajouter_entree(mp, "Afficher la liste du personnel", liste_personnel, [labo])
    ajouter_entree(mp, "Afficher les occupants d'un bureau", occupants_bureau, [labo])

    ajouter_entree(mp, 'Nouvelle opération', print, ['Labo :', labo])
    
    gerer_menu(mp)


if __name__ == '__main__':
    main()



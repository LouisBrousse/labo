from laboratoire import *

'''
Interface sur la labo avec menu textuel.
'''

def afficher_menu():
    print('1- Enregistrer une arrivée')
    print('2- Enregistrer un départ')
    print('3- Modifier le bureau d\'une personne')
    print('4- Modifier le nom d\'une personne')
    print('5- Présence d\'une personne')
    print('6- Obtenir le bureau d\'une personne')
    print('7- Obtenir la liste du personnel avec le bureau')
    print('0- Quitter')

def demander_choix():
    return int(input("Votre choix: "))

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
    try:
        nom = input('Nom ?')
        n_bureau = input('Nouveau bureau?')
        modifier_bureau(labo, nom, n_bureau)
    except AbsentException as e:
        print(f"{e}: Impossible, personne inconnue")       
    except MemeBureauException as e:                          #déplacement dans le même bureau
        print(f"{e}: Impossible, la personne est déjà dans ce bureau") 

def gerer_modifier_nom(labo):
    try:
        nom = input("Nom ? ")
        n_nom = input("Nouveau nom?")
        modifier_nom(labo, nom, n_nom)
    except AbsentException as e:
        print(f"{e}: Impossible, personne inconnue")
    

def traiter_choix(choix, labo):
    nom=''
    if choix == 1:
        gerer_arrivee(labo)    
    elif choix == 2:
        gerer_depart(labo)
    elif choix == 3:
        gerer_modifier_bureau(labo)
    elif choix == 4:
        gerer_modifier_nom(labo)
    elif choix == 5:
        nom = input("Nom ? ")
        reponse = est_presente(labo, nom)
        print('Oui présent' if reponse else 'Nom inconnue')
    elif choix == 6:
        nom = input("Nom ? ")
        reponse = est_presente(labo, nom)
        print(f'Le bureau de {nom} est le {labo[nom]}'if reponse else 'personne inconnue')
    elif choix == 7:
        for nom in labo:
            print(f'{nom} => {labo[nom]}')

def main():
    quitter = False
    labo = laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        print(labo)
        quitter = choix == 0


if __name__ == '__main__':
    main()


